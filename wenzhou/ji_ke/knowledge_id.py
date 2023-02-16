import json
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import life_227_pool


class KnowLedgeId(object):
    def __init__(self):
        pass
        self.life_227 = DataBaseSession(life_227_pool)

    def withopen_txt(self):
        with open(r'data_dict.txt', 'r', encoding='utf-8') as f:
            for i in f:
                return i

    def data_dict(self, data_txt):
        data_dict = json.loads(data_txt)
        tree = data_dict.get('data').get('tree')
        tree_id = tree['tree_id']
        tree_name = tree['name']
        one_pid = 0
        tree_data = [tree_id, tree_name, one_pid]
        self.insertion_data(tree_data)
        points_list = tree.get('points')
        self.for_data(points_list, tree_id)

    def insertion_data(self, data_l):
        insertion_sql = "insert into qb_pid_knowledge_copy1 (pid, content_name, superior_pid) VALUES (%s,%s,%s)"
        self.life_227.insertion_data(insertion_sql, data_l)

    def for_data(self, data_list, tree_id):
        for data in data_list:
            self.pid = tree_id
            self.data_data_data(data)

    def data_data_data(self, data_dd):
        point_id = data_dd['point_id']
        content_name = data_dd['name']
        superior_pid = self.pid
        points_list = data_dd['points']
        data_data = [point_id, content_name, superior_pid]
        print(data_data)
        self.insertion_data(data_data)
        if len(points_list) > 0:
            self.pid = point_id
            self.for_data(points_list, point_id)

    def run_spider_k(self):
        with open(r'data_dict.txt', 'r', encoding='utf-8') as f:
            for data_txt in f:
                self.data_dict(data_txt)


def run_s_k():
    run_k = KnowLedgeId()
    run_k.run_spider_k()


if __name__ == '__main__':
    run_s_k()









