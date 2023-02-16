from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import kuajing_227_pool
# pymysql.converters.escape_string()  新规范


class AmazonUk(object):
    def __init__(self):
        self.session_227_kj = DataBaseSession(kuajing_227_pool)
        self.data_time = ''
        self.data_list = []
        self.company_list = dict()

    def query_dict(self, dd):
        query_sql = "SELECT * FROM `amazonuk_shopinfo_{}`".format(dd)
        sql_data = self.session_227_kj.query_dict_fetchall(query_sql)
        return sql_data

    def insertion_data_list(self, columns, qmarks):
        insertion_sql = "insert into amazonuk_shopinfo_%s_all (%s) VALUES (%s)" % (self.data_time, columns, qmarks)
        self.session_227_kj.insertion_data_list(insertion_sql, self.data_list)

    def data_data(self, data_dict_list):
        file_write = open(r"C:\Users\Administrator\Desktop\data\amazonuk_shopinfo_{}_all.txt".format(self.data_time), "w", encoding="utf-8")
        num = 0
        for data in data_dict_list:
            num += 1
            data_list = list(data.values())
            registration_id = data_list[4]
            data_list[-5] = ''
            data_list[-4] = ''
            data_list[-3] = ''
            data_list[-2] = ''
            data_list[-1] = ''
            pca_data = self.company_list.get(registration_id)
            if pca_data != None:
                companys = pca_data[1]
                company_address = pca_data[2]
                province = pca_data[3]
                city = pca_data[4]
                county = pca_data[5]
                data_list[-5] = companys
                data_list[-4] = company_address
                data_list[-3] = province
                data_list[-2] = city
                data_list[-1] = county
                file_write.write(','.join(data_list) + '\n')
                file_write.flush()
            else:
                file_write.write(','.join(data_list) + '\n')
                file_write.flush()
            if num % 1000 == 0:
                print(num)

    def comapany_data(self, database_name):
        query_sql = "SELECT 统一社会信用代码,company,company_address,所属省份,所属城市,所属区县 FROM `{}`".format(database_name)
        # query_sql = "SELECT 统一社会信用代码,company,company_address,所属省份,所属城市,所属区县 FROM `{}` WHERE `company` = '（有效期至2030年7月24日）（依法须经批准的项目，经相关部门批准后方可开展经营活动）'".format(database_name)
        sql_data = self.session_227_kj.query_tuple_data(query_sql)
        for data in sql_data:
            s_id = data[0]
            if s_id == None or len(s_id) == 0:
                print(data)
            else:
                self.company_list[s_id] = data

    def run_spider(self):
        database_name = 'company_cross_qichacha_uk_all'
        self.comapany_data(database_name)
        for self.data_time in range(202210, 202211):
            data_dict = self.query_dict(self.data_time)
            self.data_data(data_dict)


def run_amazon_uk():
    run = AmazonUk()
    run.run_spider()


if __name__ == '__main__':
    run_amazon_uk()




# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot,redis
from xbot import print, sleep
from .import package
from .package import variables as glv

def main(args):
    pass

def redis_data():
    r = redis.Redis(host='192.168.1.8', port=6379, db=0, decode_responses=True,password="nriat.123456")
    shop_id = r.spop('smt_pzinfo')
    url = 'https://sellerjoin.aliexpress.com/credential/showcredential.htm?storeNum={}'.format(shop_id)
    return url









