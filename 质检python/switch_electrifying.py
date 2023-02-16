import pymysql
import numpy as np
import pandas as pd
import xgboost as xgb
# import lightgbm as lgbm
# from fbprophet import Prophet
from datetime import datetime
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, KFold
from sklearn.model_selection import GridSearchCV


def load_data():
    host = 'localhost'  # 数据库的ip地址
    user = 'root'  # 数据库的账号
    password = 'Data228or7Root715#'  # 数据库的密码
    port = 3306  # mysql数据库通用端口号
    database = 'quality_supervision'

    db = pymysql.connect(host=host, user=user, password=password, port=port, db=database)

    sql = ''' 

select * from
(select a.date,ifnull(100*(1-b.value/a.value),0) as value from 
(select left(approval_date,7) as date, count(1) as value from dwd_zj_taskitem  where sample_name like '%开关%' and item_l1 = '防触电保护' and measured_value != '——'  and measured_value != 'NULL' group by left(approval_date,7))a

left join (
select left(approval_date,7) as date, count(1) as value from dwd_zj_taskitem  where sample_name like '%开关%' and item_l1 = '防触电保护' and measured_value like '%符合%'  group by left(approval_date,7))b on a.date = b.date order by a.date desc limit 20) t order by t.date 
'''
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    columnDes = cursor.description  # 获取连接对象的描述信息
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]
    df = pd.DataFrame([list(i) for i in data], columns=columnNames)
    # print(df)
    return df


def cal_MSE(y_true, y_pre):
    return mean_squared_error(y_true, y_pre)


def cal_R2(y_true, y_pre):
    return r2_score(y_true, y_pre)

def item(data):
    data_list = []
    for i in range(len(data)):
        data_list.append(str(data[i]))
    return data_list

def create_features(df, label=None):
    date_info = [datetime.strptime(d, "%Y-%m") for d in df['date'].values.tolist()]
    df['date'] = date_info
    df['hour'] = df['date'].dt.hour
    df['dayofweek'] = df['date'].dt.dayofweek
    df['quarter'] = df['date'].dt.quarter
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['dayofyear'] = df['date'].dt.dayofyear
    df['dayofmonth'] = df['date'].dt.day
    df['weekofyear'] = df['date'].dt.weekofyear

    X = df[['hour', 'dayofweek', 'quarter', 'month', 'year',
            'dayofyear', 'dayofmonth', 'weekofyear']]
    if label:
        y = df[label]
        return X, y
    return X


def XGBoost(data):
    # data = pd.read_csv('time.csv',index_col=[0], parse_dates=[0])
    y_pre = []
    y_true = []
    data_train = data.iloc[0:19]
    # print(data_train)
    # print('111111111111111111111111111111111111111111111',len(data_train))
    data_test = data.iloc[19:20]
    # print(data_test)
    # print(data_test)
    X_train, y_train = create_features(data_train, label='value')
    X_test, y_test = create_features(data_test, label='value')

    reg = xgb.XGBRegressor(n_estimators=600)
    reg.fit(X_train, y_train, eval_set=[(X_train, y_train), (X_test, y_test)], early_stopping_rounds=300)
    y_pre.append(reg.predict(X_test)[0])
    y_true.append(y_test.tolist()[0])
    # print(y_true)
    # print(y_pre)
    #
    # print(cal_MSE(y_true, y_pre))
    # print(cal_R2(y_true, y_pre))

    data_test = data.iloc[18:20]
    data_pred = pd.DataFrame()
    data_pred['date'] = data_test['date']
    pred_list = []
    pred_list.append(data_test['value'].values[0])
    pred_list.append(round(y_pre[0],2))
    data_pred['value'] = pred_list
    data_train1 = data.iloc[0:19]

    data_standard = pd.DataFrame()
    data_standard['date'] = data['date'].iloc[0:20]
    standard_list = []
    for i in range(len(data_standard)):
        standard_list.append(60) #标准值不低于60
    data_standard['value'] = standard_list


    return item(data_train1['date'].values.tolist()), item(data_train1['value'].values.tolist()), item(data_test['date'].values.tolist())\
        , item(data_test['value'].values.tolist()), item(data_pred['date'].values.tolist()), item(data_pred['value'].values.tolist())\
        , item(data_train1['date'].values.tolist())[-1], item(data_train1['value'].values.tolist())[-1], item(data_test['date'].values.tolist())[-1]\
        , item(data_test['value'].values.tolist())[-1], item(data_pred['date'].values.tolist())[-1], item(data_pred['value'].values.tolist())[-1]




if __name__ == "__main__":
    data = load_data()
    XGBoost(data)
