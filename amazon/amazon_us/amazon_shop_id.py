import requests
import re
import time
import redis
import os
from lxml import etree
from fake_useragent import UserAgent


class AmazonSpiderShopId(object):
    def __init__(self):
        '''//span[@data-component-type="s-search-results"]/div[2]/div[2]/div/div/div/div/div/div/div/span/a/@href'''
        self.r = redis.Redis(host='192.168.1.4', port=6776, db=0, decode_responses=True)
        self.amazon_goods_url = 'amazon_goods_url'
        self.amazon_so = open(r'amazon_shop_id.txt', 'a', encoding='utf-8')
        self.ADSL_name = '057147489118'
        self.ADSL_pwd = '622375'

    def am_request(self):
        location = r'C:\Users\Administrator\Desktop\测试\amazon\amazon_us\fake_useragent_0.1.11.json'
        ua = UserAgent(path=location).random
        headers = {
                      'authority': 'www.amazon.com',
                      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                      'accept-language': 'zh-CN,zh;q=0.9',
                      'user-agent': ua,
        }
        r = requests.get(url='https://www.amazon.com/dp/B0BB6NZT7R', headers=headers)
        aa = r.text
        return r.text

    def am_data(self, response_data):
        amazon_shop = re.search(r'seller=(.*?)(">|&amp)', response_data)
        if amazon_shop != None:
            amazon_shop_id = amazon_shop.group(1)
            self.amazon_so.write(amazon_shop_id + '\n')
            self.amazon_so.flush()
            print(amazon_shop_id)
            return amazon_shop_id

    def connect(self):
        name = "kdlj"
        username = '{}'.format(self.ADSL_name)
        password = '{}'.format(self.ADSL_pwd)
        cmd_str = "rasdial %s %s %s" % (name, username, password)
        res = os.system(cmd_str)
        if res == 0:
            print("连接成功")
            time.sleep(5)
        else:
            print(res)

    def disconnect(self):
        name = "kdlj"
        cmdstr = "rasdial %s /disconnect" % name
        os.system(cmdstr)
        print('断开成功')

    def huan_ip(self):
        # 断开网络
        self.disconnect()
        # 开始拨号
        self.connect()

    def run_amazon_spider_id(self):
        while True:
            try:
                if self.r.exists(self.amazon_goods_url):
                    self.amazon_goods_i = self.r.spop(self.amazon_goods_url)
                    response_data = self.am_request()
                    re_response_data = self.am_data(response_data)
                    if re_response_data == None and "Type the characters you see in this image" in response_data:
                        self.huan_ip()
                        response_data = self.am_request()
                        re_response_data = self.am_data(response_data)
                else:
                    print('------未找到任务队列--------')
                    self.amazon_so.close()
                    time.sleep(1)
                    break

            except Exception as e:
                print(e)


def am_run_spider():
    run_amazon_id = AmazonSpiderShopId()
    aaa = run_amazon_id.am_request()
    run_amazon_id.am_data(aaa)


if __name__ == '__main__':
    am_run_spider()






