import pandas as pd
from sqlalchemy import create_engine
import os
import sys
from openpyxl import load_workbook

path = r"D:\JupyterProject"
sys.path.append(path)

engine = create_engine(
    'mysql+pymysql://{user}:{pw}@192.168.0.228:9228/{db}?charset=utf8'.format(user='drop', pw='135gdfg228@DROP5',
                                                                              db='e_commerce', ), encoding='utf-8')
engine_tmall = create_engine(
    'mysql+pymysql://{user}:{pw}@192.168.0.227:9227/{db}?charset=utf8'.format(user='drop', pw='227#*gdwkDROP12',
                                                                              db='oridata_tmall', ), encoding='utf-8')

cidlist = pd.read_excel("淘宝天猫类目表CPI划分1.25.xlsx", usecols=[0, 14])
# 去重
cidlist = cidlist.drop_duplicates('cid', keep='first')
cidlist['cid'] = cidlist['cid'].astype("str")
cidlist = cidlist.loc[(cidlist.CPI1.notnull())]


def get_result(goods_list, shop_list):
    shop_goods = pd.merge(goods_list, shop_list, on=['shop_id', 'date'], how='inner')
    shop_goods = pd.merge(shop_goods, cidlist, on='cid', how='inner')
    return shop_goods


pingtai = ['tmall']
year = 2018
# 计算起始月
first_month = 1
# 计算结束月
last_month = 12

# 取出商品数据
final_goods = pd.DataFrame()
for month in range(first_month, last_month + 1):
    goods = pd.DataFrame()
    goods = pd.read_sql(
        "select shop_id,goods_id,cid,sales_month+0 as sales_month,discount_price+0 as discount_price,'tmall' as plat,'{0}{1}' as date from tmall_goodsmobile_{0}{1} where discount_price<=100000".format(
            year, "%02d" % month), con=engine_tmall)
    goods = goods.drop_duplicates(['goods_id'], keep='first')
    print(year, "%02d" % month, len(goods))

    # 取出企业店
    shop = pd.DataFrame()
    shop = pd.read_sql("select shop_id,'{0}{1}' as date from tmall_shopinfo_{0}{1} where province = '浙江省'".format(year, "%02d" % month),
                       con=engine)
    print(year, "%02d" % month, len(shop))
    shop = shop.drop_duplicates('shop_id', keep='last')

    # 得到目标商品
    shop_goods = get_result(goods, shop)
    shop_goods['sales_money'] = (shop_goods['discount_price'] * shop_goods['sales_month'])
    shop_goods.sort_values(by=['date', 'cid', 'sales_money'], ascending=[True, True, False], inplace=True)
    top_goods = shop_goods.groupby(['date', 'cid']).head(10)
    final_goods = final_goods.append(top_goods)

final = top_goods.groupby(['plat', 'CPI1'])[['sales_money', 'sales_month']].sum().reset_index()
final_sum = top_goods.groupby(['plat'])[['sales_money', 'sales_month']].sum().reset_index()
final = final.append(final_sum)
final['price'] = final['sales_money'] / final['sales_month']
final.to_excel(r'{}年CPI商品.xlsx'.format(year), index=False)