from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import shop_1_4_pool
import re

data_dict = {}
life_server_227 = DataBaseSession(shop_1_4_pool)


def opne_data():
#     cx_sql = """SELECT shop_id,postcode,province,city,county from
# (
# Select shop_id,postcode,province,city,county from  amazonus_shopinfo_202101_sales WHERE `postcode` <> ''
# UNION ALL
# Select shop_id,postcode,province,city,county from  amazonus_shopinfo_202102_sales WHERE `postcode` <> ''
# UNION ALL
# Select shop_id,postcode,province,city,county from  amazonus_shopinfo_202103_sales WHERE `postcode` <> ''
# UNION ALL
# Select shop_id,postcode,province,city,county from  amazonus_shopinfo_202104_sales WHERE `postcode` <> ''
# UNION ALL
# Select shop_id,postcode,province,city,county from  amazonus_shopinfo_202105_sales WHERE `postcode` <> ''
# UNION ALL
# Select shop_id,postcode,province,city,county from  amazonus_shopinfo_202106_sales WHERE `postcode` <> ''
# UNION ALL
# Select shop_id,postcode,province,city,county from  amazonus_shopinfo_202107_sales WHERE `postcode` <> ''
# UNION ALL
# Select shop_id,postcode,province,city,county from  amazonus_shopinfo_202108_sales WHERE `postcode` <> ''
# UNION ALL
# Select shop_id,postcode,province,city,county from  amazonus_shopinfo_202109_sales WHERE `postcode` <> ''
# UNION ALL
# Select shop_id,postcode,province,city,county from  amazonus_shopinfo_202110_sales WHERE `postcode` <> ''
# UNION ALL
# Select shop_id,postcode,province,city,county from  amazonus_shopinfo_202111_sales WHERE `postcode` <> ''
# UNION ALL
# Select shop_id,postcode,province,city,county from  amazonus_shopinfo_202112_sales WHERE `postcode` <> ''
# )   as a
# GROUP BY shop_id"""
    cx_sql = "select shop_id,postcode,province,city,county from  amazonus_shopinfo_202210_sales WHERE `city` <> ''"
    address_list = life_server_227.query_tuple_data(cx_sql)
    # quest = 'select shop_id from meituan_wenzhou_new'
    # shop_id_list = life_server.query_tuple_data(quest)
    for shop_id_t in address_list:
        shop_id = shop_id_t[0]
        data_dict[shop_id] = shop_id_t


def insertion_data(data_list, i):
    # 无farm_flag字段：2021-1-3   20201-10
    insertion_sql = "insert into amazonus_shopinfo_{}_sales_new (shop_id, shop_name, shop_info, company, company_address, country, postcode, html, goodrate_month, middlerate_month, badrate_month, comment_month, goodrate_quarterly, middlerate_quarterly, badrate_quarterly, comment_quarterly, goodrate_year, middlerate_year, badrate_year, comment_year, goodrate_total, middlerate_total, badrate_total, comment_total, province, city, county, main_sales, average_price, sales, sales_money,sales_y,sales_money_y) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)
    # 插入库名： session_227_tb
    life_server_227.insertion_data_list(insertion_sql, data_list)


if __name__ == '__main__':
    opne_data()
    number = 0
    dayt_list = []
    for num in range(202201, 202210):
        kj_sql = 'SELECT * from  amazonus_shopinfo_{}_sales'.format(num)
        kj_data = life_server_227.query_tuple_data(kj_sql)
        for kj_da in kj_data:
            kj_da_list = list(kj_da)
            shop_id = kj_da_list[0]
            data_data = data_dict.get(shop_id)
            if data_data:
                kj_da_list[6] = data_data[1]
                kj_da_list[24] = data_data[2]
                kj_da_list[25] = data_data[3]
                kj_da_list[26] = data_data[4]
                dayt_list.append(kj_da_list)
                number += 1
            else:
                dayt_list.append(kj_da_list)
                number += 1
            if number % 10000 == 0:
                insertion_data(dayt_list, num)
                dayt_list = []
                print(number)
        if len(dayt_list) > 0:
            insertion_data(dayt_list, num)
            dayt_list = []
            print(number)



