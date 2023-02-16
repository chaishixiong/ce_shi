from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import jd_pool


class JData(object):
    def __init__(self):
        self.session_227_jd = DataBaseSession(jd_pool)
        self.data_list = []
        self.comment_dict = dict()

    def query_dict(self):
        jd_mysql = "SELECT * FROM `jd_goodsinfo_202201`"
        jd_data = self.session_227_jd.query_dict_fetchall(jd_mysql)
        if len(jd_data) > 0:
            qmarks = ','.join(['%s'] * len(jd_data[0]))
            columns = ', '.join(jd_data[0].keys()).split(',')
            # columns = ', '.join(jh_data[0].keys())
            columns_str = ''
            for column in columns:
                c_str = '`' + column + '`' + ','
                columns_str += c_str
            columns_str = columns_str.strip(',').replace(' ', '')
            num = 0
            for i in jd_data:
                num += 1
                data_list = list(i.values())
                goods_id = data_list[1]
                comment_11 = int(self.comment_dict.get(goods_id)) if self.comment_dict.get(goods_id) != None else 0
                comment_12 = int(data_list[7])
                comment_new = comment_12 - comment_11
                data_list[7] = str(comment_new)
                self.data_list.append(tuple(data_list))
                if num % 10000 == 0:
                    self.insert(columns_str, qmarks)
                    self.data_list = []
                    print(num)
            if len(self.data_list) > 0:
                print(num)
                self.insert(columns_str, qmarks)
                self.data_list = []

    def query_data(self, jd_mysql):
        jd_data = self.session_227_jd.query_tuple_data(jd_mysql)
        for item in jd_data:
            self.comment_dict[item[0]] = item[1]

    def insert(self, columns, qmarks):
        insertion_sql = "insert into jd_goodsinfo_202201_E_zj_ceshi (%s) VALUES (%s)" % (columns, qmarks)
        self.session_227_jd.insertion_data_list(insertion_sql, self.data_list)

    def run_spider(self):
        comment_sql = 'SELECT goods_id, `comment` FROM `jd_goodsinfo_202112`'
        self.query_data(comment_sql)
        self.query_dict()


def run_jd():
    r = JData()
    r.run_spider()


if __name__ == '__main__':
    run_jd()


