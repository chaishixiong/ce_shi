import requests
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import kuajing_227_pool
import json


class OpenStore(object):
    def __init__(self):
        self.smt_227_shop = DataBaseSession(kuajing_227_pool)

    def request(self, url):

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        r = requests.get(headers=headers, url=url)
        return r

    def data_data(self, data_dict):
        result = data_dict.get("result")
        data = result.get("data")
        shopInfo = data.get("shopInfo")
        shop_id = shopInfo.get("shopId")
        seller_id = shopInfo.get("sellerId")
        open_time = shopInfo.get("shopCreatedAt")
        data_tuple = (shop_id, seller_id, open_time)
        self.insertion(data_tuple)

    def insertion(self, data_tuple):
        sql = "insert into smt_shop_open_time_copy1 (shop_id, seller_id, open_time) VALUES (%s,%s,%s)"
        self.smt_227_shop.insertion_data(sql, data_tuple)

    def re_str_data(self, data_str):
        try:
            data = data_str.content.decode()
            str_data = json.loads(data)
        except Exception as e:
            print(e)
            str_data = {}
        return str_data

    def run_spider(self):
        # t = int(time.time() * 1000)
        # jsonp = 'jsonp_{}'.format(t)
        url = 'https://shoprenderview.aliexpress.com/async/execute?componentKey=pcShopHead&country=US&site=esp&sellerId=239000689&callback'
        data_str = self.request(url)
        data_dict = self.re_str_data(data_str)
        self.data_data(data_dict)


def run_open_store():
    run = OpenStore()
    run.run_spider()


if __name__ == '__main__':
    run_open_store()













