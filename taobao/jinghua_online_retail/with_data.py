from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import jh_228_pool, kuajing_227_pool


class JHData(object):
    def __init__(self):
        self.session_228_jh = DataBaseSession(jh_228_pool)
        self.session_227_jh = DataBaseSession(kuajing_227_pool)
        self.data_list = []
        self.with_open = open(r"dm_city_shoplist.txt", "a", encoding="utf-8")
        self.num = 0

    def query_dict(self, d):
        jh_mysql = "SELECT '2020' as `year`,'{}' as `month`,'金华市' as city,'2' as platform,shop_name,sales_money as sales,sales_count as count_sales, NOW() as create_time FROM ods_tmall_shopinfo_{} WHERE shop_name is not null and sales_money>0 GROUP BY shop_name;".format(str(d)[-1], d)
        jh_data = self.session_228_jh.query_dict_fetchall(jh_mysql)
        for i in jh_data:
            if self.num == 14960:
                print()
            self.num += 1
            data_tuple = list(i.values())
            data_tuple.insert(0, str(self.num))
            data_tuple[8] = str(data_tuple[8])
            self.with_open.write(",".join(data_tuple) + "\n")

    def insert(self, d, columns, qmarks):
        insertion_sql = "insert into dm_city_shoplist_copy1 (%s) VALUES (%s)" % (columns, qmarks)
        self.session_228_jh.insertion_data(insertion_sql, self.data_list)

    def run_spider(self):
        for d in range(202007, 202013):
            print('年月：' + str(d))
            self.query_dict(d)
        self.with_open.close()


def run_jh():
    r = JHData()
    r.run_spider()


if __name__ == '__main__':
    run_jh()
    # dsdf = ['2020', '3', '金华市', '2', '007詹士邦内衣旗舰店', '1700.6', '34', '2021-12-20 13:56:25']
    # with open('aa.txt', 'a', encoding='utf-8')as f:
    #     f.write(",".join(dsdf))
    #     f.close()


