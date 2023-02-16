from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import kuajing_227_pool
# pymysql.converters.escape_string()  新规范

class AlbbGj(object):
    def __init__(self):
        self.pca_dict = dict()
        self.session_227_kj = DataBaseSession(kuajing_227_pool)
        self.data_time = ''
        self.data_list = []

    def query_dict(self, dd):
        query_sql = "SELECT * FROM `alibabagj_shopinfo_{}`".format(dd)
        sql_data = self.session_227_kj.query_dict_fetchall(query_sql)
        return sql_data

    def insertion_data_list(self, columns, qmarks):
        insertion_sql = "insert into alibabagj_shopinfo_%s_new (%s) VALUES (%s)" % (self.data_time, columns, qmarks)
        self.session_227_kj.insertion_data_list(insertion_sql, self.data_list)

    def data_data(self, data_dict_list):
        qmarks = ','.join(['%s'] * len(data_dict_list[0]))
        columns = ', '.join(data_dict_list[0].keys()).split(',')
        # columns = ', '.join(data_dict_list[0].keys())
        columns_str = ''
        for column in columns:
            c_str = '`' + column + '`' + ','
            columns_str += c_str
        columns_str = columns_str.strip(',').replace(' ', '')
        num = 0
        for data in data_dict_list:
            num += 1
            data_list = list(data.values())
            zip_id = data.get('zip')
            pca_data = self.pca_dict.get(zip_id)
            if pca_data != None:
                province_match = pca_data[1]
                city_match = pca_data[2]
                area_match = pca_data[3]
                # data_list[-5] = None
                data_list[-4] = province_match
                data_list[-3] = city_match
                data_list[-2] = area_match
                # data_list[18] = ''
                self.data_list.append(tuple(data_list))
            else:
                data_tuple = tuple((data.values()))
                self.data_list.append(data_tuple)
            if num % 10000 == 0:
                self.insertion_data_list(columns_str, qmarks)
                self.data_list = []
                print(num)
        if len(self.data_list) > 0:
            print(num)
            self.insertion_data_list(columns_str, qmarks)
            self.data_list = []

    def with_open_txt(self):
        with open('{地区邮编}[id,省,市,区].txt', 'r', encoding='utf-8') as f:
            for i in f:
                data = i.strip('\n').split(',')
                a_id = data[0]
                self.pca_dict[a_id] = data

    def run_spider(self):
        self.with_open_txt()
        for self.data_time in range(202011, 202012):
            data_dict = self.query_dict(self.data_time)
            self.data_data(data_dict)


def run_albbgj():
    run = AlbbGj()
    run.run_spider()


if __name__ == '__main__':
    run_albbgj()














