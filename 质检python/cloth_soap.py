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
import json


def load_data():
    host = 'localhost'  # 数据库的ip地址
    user = 'root'  # 数据库的账号
    password = 'Data228or7Root715#'  # 数据库的密码
    port = 3306  # mysql数据库通用端口号
    database = 'quality_supervision'

    db = pymysql.connect(host=host, user=user, password=password, port=port, db=database)

    sql = ''' 

select * from
(select t.date,ifnull(100*(1-(c.value+d.value)/(a.value+b.value)),0) as value from 
(select left(approval_date,7) as date, count(1) as value  from dwd_zj_taskitem where (test_basis like '%GB/T 22854-2009%'  or test_basis like '%GB/T 23328-2009%' or test_basis like '%GB/T 31888-2015%')  and item_l1 = '耐皂洗色牢度（级）' group by left(approval_date,7)) t
left join

(select left(approval_date,7) as date, count(1) as value  from dwd_zj_taskitem where (test_basis like '%GB/T 22854-2009%'  or test_basis like '%GB/T 23328-2009%' or test_basis like '%GB/T 31888-2015%') and measured_value != 'NULL' and item_l1 = '耐皂洗色牢度（级）' and above_scale_flag = 0 group by left(approval_date,7)) a on t.date = a.date
left join
(select left(approval_date,7) as date, 3*count(1) as value  from dwd_zj_taskitem where (test_basis like '%GB/T 22854-2009%'  or test_basis like '%GB/T 23328-2009%' or test_basis like '%GB/T 31888-2015%') and measured_value != 'NULL' and item_l1 = '耐皂洗色牢度（级）' and above_scale_flag = 1 group by left(approval_date,7)) b on t.date = b.date
left join

(select left(approval_date,7) as date, count(1) as value  from dwd_zj_taskitem where (test_basis like '%GB/T 22854-2009%'  or test_basis like '%GB/T 23328-2009%' or test_basis like '%GB/T 31888-2015%') and measured_value != '3' and measured_value not like '%2%' and (measured_value like '%3%' or measured_value like '%4%' or measured_value like '%5%') and item_l1 = '耐皂洗色牢度（级）' and above_scale_flag = 0 group by left(approval_date,7)) c on t.date = c.date
left join
(select left(approval_date,7) as date, 3*count(1) as value  from dwd_zj_taskitem where (test_basis like '%GB/T 22854-2009%'  or test_basis like '%GB/T 23328-2009%' or test_basis like '%GB/T 31888-2015%') and measured_value != '3' and measured_value not like '%2%' and (measured_value like '%3%' or measured_value like '%4%' or measured_value like '%5%') and item_l1 = '耐皂洗色牢度（级）' and above_scale_flag = 1 group by left(approval_date,7)) d on t.date = d.date

order by a.date desc limit 22) t order by t.date 
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
        if(data[i]==None):
            data_list.append(data[i])
        else:
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
    data_train = data.iloc[0:21]
    # print(data_train)
    # print('111111111111111111111111111111111111111111111',len(data_train))
    data_test = data.iloc[21:22]
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

    # print(cal_MSE(y_true, y_pre))
    # print(cal_R2(y_true, y_pre))

    data_test = data.iloc[20:22]
    data_pred = pd.DataFrame()
    data_pred['date'] = data_test['date']
    pred_list = []
    pred_list.append(data_test['value'].values[0])
    pred_list.append(round(y_pre[0],2))
    data_pred['value'] = pred_list
    data_train1 = data.iloc[0:21]

    data_standard = pd.DataFrame()
    data_standard['date'] = data['date'].iloc[0:22]
    standard_list = []
    for i in range(len(data_standard)):
        standard_list.append(60) #标准值不低于60
    data_standard['value'] = standard_list


    y_train = []
    for i in range(len(data_train1['value'])):
        y_train.append(data_train1['value'].values.tolist()[i])
    y_train.append(None)
    print(y_train)

    data_zero1 = []
    data_zero2 = []
    for i in range(20):
        data_zero1.append(None)
        data_zero2.append(None)
    for i in range(2):
        data_zero1.append(data_test['value'].values.tolist()[i])
        data_zero2.append(data_pred['value'].values.tolist()[i])







    return  item(y_train)\
        , item(data_zero1), item(data_zero2), item(data_train1['date'].values.tolist())[-1], item(data_train1['value'].values.tolist())[-1]\
        , item(data_test['date'].values.tolist())[-1], item(data_test['value'].values.tolist())[-1], item(data_pred['date'].values.tolist())[-1] \
        , item(data_pred['value'].values.tolist())[-1]\
        , item(data['date'].values.tolist())




if __name__ == "__main__":
    data = load_data()
    XGBoost(data)
