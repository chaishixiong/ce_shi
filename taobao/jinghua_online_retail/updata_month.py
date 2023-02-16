from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import jh_228_pool, kuajing_227_pool


class JHUpdataData(object):
    def __init__(self):
        self.session_228_jh = DataBaseSession(jh_228_pool)
        self.session_227_jh = DataBaseSession(kuajing_227_pool)
        self.data_list = []
        self.with_open = open(r"dm_county_shoplist.txt", "a", encoding="utf-8")
        self.num = 0
        self.y_num = 0
        self.mmm = 1

    def query_dict(self, mysql):
        jh_data = self.session_228_jh.query_tuple_data(mysql)
        for i in jh_data:
            self.y_num += 1
            data_tuple = list(i)
            month = data_tuple[2]
            data_tuple[0] = str(data_tuple[0])
            data_tuple[1] = str(data_tuple[1])
            data_tuple[2] = str(data_tuple[2])
            data_tuple[11] = ''
            data_tuple[8] = str(data_tuple[8])
            data_tuple[9] = str(data_tuple[9])
            if month == 0:
                self.mmm = 10
                data_tuple[2] = str(10)
            elif self.mmm == 10:
                if month == 1:
                    data_tuple[2] = str(11)
                elif month == 2:
                    data_tuple[2] = str(12)
            self.with_open.write(', '.join(data_tuple) + '\n')
            # else:
            #     if data_tuple[2] == 0:
            #         self.num = 10
            #         self.mmm = 10
            #     data_tuple[2] = str(self.num)
            #     data_tuple[0] = str(data_tuple[0])
            #     data_tuple[1] = str(data_tuple[1])
            #     data_tuple[6] = str(data_tuple[6])
            #     data_tuple[7] = str(data_tuple[7])
            #     data_tuple[8] = str(data_tuple[8])
            #     data_tuple[9] = ''
            #     self.with_open.write(', '.join(data_tuple) + '\n')
            if self.y_num % 10000 == 0:
                print(self.y_num)

    def insert(self, qmarks):
        insertion_sql = "insert into dm_city_shoplist_new (`id`,`year`,`month`,`city`,`shop_name`,`platform`,`sales`,`count_sales`,`create_time`,`update_time`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.session_228_jh.insertion_data(insertion_sql, qmarks)

    def run_spider(self):
        for d in range(2020, 2022):
            for i in range(1, 5):
                mysql = 'SELECT * FROM `dm_county_shoplist` where platform = {} and `year` = {}'.format(i, d)
                self.query_dict(mysql)
                self.num = 0


def run_jh_updata():
    r = JHUpdataData()
    r.run_spider()


if __name__ == '__main__':
    run_jh_updata()



