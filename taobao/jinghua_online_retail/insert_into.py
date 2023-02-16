from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import jh_228_pool, kuajing_227_pool


class JHData(object):
    def __init__(self):
        self.session_228_jh = DataBaseSession(jh_228_pool)
        self.session_227_jh = DataBaseSession(kuajing_227_pool)
        self.data_list = []

    def query_dict(self, m, d):
        jh_mysql = "SELECT '2021' as `year`,'{}' as `month`,'浙江省' as province,'金华市' as city,county,'2' as platform,shop_id,shop_name,sales_money as sales,sales_num as count_sales FROM ods_smt_shopinfo_{} WHERE shop_name is not null and sales_money>0 GROUP BY shop_name;".format(m, d)
        jh_data = self.session_228_jh.query_dict_fetchall(jh_mysql)
        if len(jh_data) > 0:
            qmarks = ','.join(['%s'] * len(jh_data[0]))
            columns = ', '.join(jh_data[0].keys()).split(',')
            # columns = ', '.join(jh_data[0].keys())
            columns_str = ''
            for column in columns:
                c_str = '`' + column + '`' + ','
                columns_str += c_str
            columns_str = columns_str.strip(',').replace(' ', '')
            num = 0
            for i in jh_data:
                num += 1
                data_list = list(i.values())
                # data_list[-5] = None
                self.data_list.append(tuple(data_list))
                if num % 1000 == 0:
                    self.insert(d, columns_str, qmarks)
                    self.data_list = []
                    print(num)
            if len(self.data_list) > 0:
                print(num)
                self.insert(d, columns_str, qmarks)
                self.data_list = []

    def insert(self, d, columns, qmarks):
        insertion_sql = "insert into dm_county_shoplist_kj_ceshi (%s) VALUES (%s)" % (columns, qmarks)
        self.session_228_jh.insertion_data_list(insertion_sql, self.data_list)

    def run_spider(self):
        for m, d in zip(range(2, 12), range(202102, 202112)):
        # for m, d in zip(range(2, 13), range(202002, 202013)):
        # for m in range(1, 12):
        #     d = 202012
            print('年月：' + str(d))
            self.query_dict(m, d)


def run_jh():
    r = JHData()
    r.run_spider()


if __name__ == '__main__':
    run_jh()


