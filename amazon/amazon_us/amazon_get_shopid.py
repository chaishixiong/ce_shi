import requests
import re
import time
import redis
from lxml import etree
from fake_useragent import UserAgent


class AmazonSpiderShop(object):
    def __init__(self):
        '''//span[@data-component-type="s-search-results"]/div[2]/div[2]/div/div/div/div/div/div/div/span/a/@href'''
        self.r = redis.Redis(host='192.168.1.4', port=6776, db=0, decode_responses=True)
        # self.amazon_goods_url = 'amazon_sortshop\\amazon_sortshop:requests'
        self.amazon_category_url = 'amazon_category_url'
        self.dsdsdd = open(r'W:\scrapy_seed\amazon_cat_url\amazon_cat_url_8_1.txt', 'a', encoding='utf-8')

    def am_request(self):
        location = r'C:\Users\Administrator\Desktop\测试\amazon\amazon_us\fake_useragent_0.1.11.json'
        ua = UserAgent(path=location).random
        headers = {
                      'authority': 'www.amazon.com',
                      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                      'accept-language': 'zh-CN,zh;q=0.9',
                      'user-agent': ua,
        }
        r = requests.get(url=self.amazon_url, headers=headers)
        return r.text

    def am_data(self, response_data):
        amazon_html = etree.HTML(response_data)
        amazon_goods_url_list = amazon_html.xpath('//span[@data-component-type="s-search-results"]/div[1]/div/@data-asin')
        for amazon_goods_url in amazon_goods_url_list:
            if len(amazon_goods_url) > 0:
                self.dsdsdd.write(amazon_goods_url + '\n')
                self.dsdsdd.flush()
                # self.r.sadd(self.amazon_goods_url, all_amazon_goods_url)
                print(amazon_goods_url)

    def run_amazon_spider(self):
        while True:
            try:
                if self.r.exists(self.amazon_category_url):
                    self.amazon_url = self.r.spop(self.amazon_category_url)
                    response_data = self.am_request()
                    re_response_data = self.am_data(response_data)
                else:
                    print('------未找到任务队列--------')
                    self.dsdsdd.close()
                    time.sleep(60)
                    break
            except Exception as e:
                print(e)


def am_run_spider():
    run_amazon = AmazonSpiderShop()
    run_amazon.run_amazon_spider()


if __name__ == '__main__':
    am_run_spider()






