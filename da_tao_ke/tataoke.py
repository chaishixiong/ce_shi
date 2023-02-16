import requests
import json
import time
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import tb_pool


class DaTaoKe(object):
    def __init__(self):
        self.session_227_tb = DataBaseSession(tb_pool)

    def dtk_resquest(self, url):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        return r.text

    def p_data(self, dict_data):
        data_list = dict_data.get('data').get('search').get('list')
        for data in data_list:
            goods_id = data['goodsid']
            seller_id = data['seller_id']
            shop_name = data['shop_name']
            data_tuple = (seller_id, shop_name, goods_id)
            self.insertion_data(data_tuple)

    def insertion_data(self, data_tuple):
        # 无farm_flag字段：2021-1-3   20201-10
        insertion_sql = "insert into dataoke_shopinfo_202208 (seller_id, shop_name, good_id) VALUES (%s,%s,%s)"

        # 插入库名： session_227_tb
        self.session_227_tb.insertion_data(insertion_sql, data_tuple)

    def run_spider(self):
        for i in range(1, 486):
            url = 'https://dtkapi.ffquan.cn/go_getway/proxy/search?platform=1&page={}&px=zh&version=1&api_v=1&flow_identifier=normal'.format(i)
            text_data = self.dtk_resquest(url)
            time.sleep(3)
            dict_data = json.loads(text_data)
            self.p_data(dict_data)


def run_dataoke():
    run_sp = DaTaoKe()
    run_sp.run_spider()


if __name__ == '__main__':
    run_dataoke()


















