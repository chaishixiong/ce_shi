from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import kjoridata_1_4_pool, kj_1_4_pool


def company_crossname():
    company_cross_dict = set()
    registration_mysql = DataBaseSession(kjoridata_1_4_pool)
    sql = "SELECT company FROM `company_cross_221201`"
    cx_sql = "SELECT * FROM `company_crossname_2212` WHERE `company` <> '' AND `company_address` <> ''"
    company_cross_data = registration_mysql.query_tuple_data(sql)
    for data_1 in company_cross_data:
        company_cross_dict.add(data_1[0])
    company_crossname_data = registration_mysql.query_tuple_data(cx_sql)
    for data_2 in company_crossname_data:
        data_name = data_2[0]
        if data_name not in company_cross_dict:
            insertion_sql = "insert into company_crossname_2212_1 (company,company_address) VALUES (%s,%s)"
            registration_mysql.insertion_data(insertion_sql, data_2)
            company_cross_dict.add(data_name)


def company_namenew():
    #  处理速卖通公司名称中的英文和未匹配公司名称的店铺
    company_dict = dict()
    company_mysql = DataBaseSession(kj_1_4_pool)
    company_mysql_oridata = DataBaseSession(kjoridata_1_4_pool)
    # for many in ['202211', '202212']:
    #     comapny_name_sql = "select shop_id, company from smt_shopinfo_{}_new where company <> ''".format(many)
    #     # comapny_name_sql = "select shop_id, company from smt_shopinfo_202211_new where shop_id in ('1102271495','1102210154','1102214241')"
    #     company_data = company_mysql.query_tuple_data(comapny_name_sql)
    #     for data in company_data:
    #         comapny_namelist = data[1].split('      ')
    #         if len(comapny_namelist) == 2:
    #             company_dict[data[0]] = comapny_namelist[0]
    #         else:
    #             company_dict[data[0]] = data[1]
    # for a, b in company_dict.items():
    #     data_2 = [a, b]
    #     insertion_sql = "insert into smt_shop_company (shop_id,company_name) VALUES (%s,%s)"
    #     company_mysql.insertion_data(insertion_sql, data_2)
    comapny_name_sql = "select * from company_crossname_2212"
    # comapny_name_sql = "select shop_id, company from smt_shopinfo_202211_new where shop_id in ('1102271495','1102210154','1102214241')"
    company_data = company_mysql_oridata.query_tuple_data(comapny_name_sql)
    for data in company_data:
        comapny_namelist = data[0].split('      ')
        if len(comapny_namelist) == 2:
            company_dict[data[1]] = comapny_namelist[0]
        else:
            company_dict[data[1]] = data[0]
    sql = "SELECT address FROM `smt_shopinfo_202212_new` WHERE `company` = '' AND `shui_id` <> ''"
    company_shop = company_mysql.query_tuple_data(sql)
    for i in company_shop:
        address = i[0]
        com_name = company_dict.get(address, '')
        updata_sql = 'UPDATE smt_shopinfo_202212_new set company = "{}" where address = "{}"'.format(com_name, address)
        company_mysql.updata_data(updata_sql)


def updata_company():
    company_mysql = DataBaseSession(kj_1_4_pool)
    company_dict = dict()
    query_sql = 'select shop_id, company_name from smt_shop_company'
    data_compay = company_mysql.query_tuple_data(query_sql)
    for company_name in data_compay:
        company_dict[company_name[0]] = company_name[1]
    sql = "SELECT * FROM `smt_shopinfo_202301` WHERE `shui_id` <> '' AND `company` = ''"
    shop_id_data = company_mysql.query_tuple_data(sql)
    for shop_list in shop_id_data:
        shop_id = shop_list[0]
        company_n = company_dict.get(shop_id)
        if company_n != None:
            updata_sql = 'UPDATE smt_shopinfo_202301 set company = "{}" where shop_id = "{}"'.format(company_n, shop_id)
            company_mysql.updata_data(updata_sql)


def smt_paizhao_shop():
    #  速卖通牌照店铺ID去重
    company_mysql = DataBaseSession(kj_1_4_pool)
    pc_shop_id = open(r'X:\数据库\速卖通\seed\smt_company_seed.txt', 'a', encoding='utf-8')
    company_dict = set()
    ssads_seed = set()
    query_sql = 'select shop_id from smt_shopinfo_202301'
    data_compay = company_mysql.query_tuple_data(query_sql)
    for company_name in data_compay:
        company_dict.add(company_name[0])
    with open(r'W:\scrapy_seed\smt_goodsid_order.txt', 'r', encoding='utf-8') as smt_shop_seed:
        for shop in smt_shop_seed:
            shop_seed = shop.strip().split(',')
            if shop_seed[0] not in company_dict:
                company_dict.add(shop_seed[0])
                pc_shop_id.write(shop_seed[0] + '\n')
                pc_shop_id.flush()
    with open(r'X:\数据库\速卖通\速卖通_拍照信息\新建文件夹 (2)_合并.txt', 'r', encoding='utf-8') as smt_shop_seed_3:
        for shop_3 in smt_shop_seed_3:
            shop_seed_3 = shop_3.strip().split(',')
            ssads_seed.add(shop_seed_3[0])
    with open(r'X:\数据库\速卖通\seed\shop_id.txt', 'r', encoding='utf-8') as smt_shop_seed_2:
        for shop_2 in smt_shop_seed_2:
            shop_seed_2 = shop_2.strip().split(',')
            if shop_seed_2[0] not in ssads_seed:
                ssads_seed.add(shop_seed_2[0])
                pc_shop_id.write(shop_seed_2[0] + '\n')
                pc_shop_id.flush()
    pc_shop_id.close()


if __name__ == '__main__':
    smt_paizhao_shop()




