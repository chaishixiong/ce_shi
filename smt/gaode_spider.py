#!/usr/bin/env python
# coding=utf-8
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import kjoridata_1_4_pool, kj_1_4_pool
import requests, json
company_mysql = DataBaseSession(kj_1_4_pool)
company_mysql_oridata = DataBaseSession(kjoridata_1_4_pool)


def company_namenew():
    #  处理速卖通公司名称中的英文和未匹配公司名称的店铺
    company_dict = dict()

    comapny_name_sql = "SELECT company_address,province,city,county FROM `oridata`.`company_cross_221201` WHERE `company` <> '' AND `province` <> ''"
    company_data = company_mysql_oridata.query_tuple_data(comapny_name_sql)
    for data in company_data:
        # comapny_namelist = data[0].split('      ')
        # if len(comapny_namelist) == 2:
        #     company_dict[data[1]] = comapny_namelist[0]
        # else:
        company_dict[data[0]] = data
    sql = "SELECT shop_id,address FROM `smt_shopinfo_202212_new` WHERE `province` = '' AND `shui_id` <> '' AND `sales_month` <> '' AND `address` <> ''"
    company_shop = company_mysql.query_tuple_data(sql)
    for i in company_shop:
        shop_id = i[0]
        address = i[1]
        com_name = company_dict.get(address)
        if com_name != None:
            province = com_name[1]
            city = com_name[2]
            county = com_name[3]
            update_smt_province(province, city, county, shop_id)


def update_smt_province(province, city, county, shop_id):
    updata_sql = 'UPDATE smt_shopinfo_202212_new set province = "{}",city = "{}",county = "{}" where shop_id = "{}"'.format(
        province, city, county, shop_id)
    company_mysql.updata_data(updata_sql)


def smt_province_request(shop_id, company_addres):
    url = 'https://restapi.amap.com/v3/geocode/geo?address={}&output=json&key=4217249ade242a808a9cae42a38bea24&output=json'.format(company_addres)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    r = requests.get(url, headers=header)
    data_dict = json.loads(r.text)
    if data_dict['info'] == "OK":
        geocodes = data_dict.get('geocodes')[0]
        province = geocodes['province']
        city = geocodes['city']
        county = geocodes['district']
        update_smt_province(province, city, county, shop_id)
        print([province, city, county, shop_id])


if __name__ == '__main__':
    sql = "SELECT shop_id,address FROM `smt_shopinfo_202212_new` WHERE `province` = '' AND `shui_id` <> '' AND `sales_month` <> '' AND `address` <> ''"
    company_shop = company_mysql.query_tuple_data(sql)
    for i in company_shop:
        shop_id = i[0]
        address = i[1]
        smt_province_request(shop_id, address)

