import requests
import re, socket
import time
import redis
from lxml import etree
from fake_useragent import UserAgent


class AmazonUKSpiderShop(object):
    def __init__(self):
        '''//span[@data-component-type="s-search-results"]/div[2]/div[2]/div/div/div/div/div/div/div/span/a/@href'''
        self.r = redis.Redis(host='192.168.1.4', port=6776, db=0, decode_responses=True)
        # self.amazon_goods_url = 'amazon_sortshop\\amazon_sortshop:requests'
        self.amazon_uk_category_url = 'amazon_uk_category_url'
        self.dsdsdd = open(r'X:\数据库\欧洲亚马逊\goods_id\amazon_uk_goodsid_{}_1.txt'.format(self.get_ip()), 'a', encoding='utf-8')

    def amuk_request(self):
        location = r'W:\fake\fake_useragent_0.1.11.json'
        ua = UserAgent(path=location).random
        headers = {
                      'authority': 'www.amazon.co.uk',
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

    def run_amazonuk_spider(self):
        while True:
            try:
                if self.r.exists(self.amazon_uk_category_url):
                    self.amazon_url = self.r.spop(self.amazon_uk_category_url)
                    # self.amazon_url = 'https://www.amazon.co.uk/b/?_encoding=UTF8&node=15488758031&bbn=560798&ref_=Oct_d_odnav_d_4085731_0&pd_rd_w=lUl57&content-id=amzn1.sym.d191d14d-5ea3-4792-ae6c-e1de8a1c8780&pf_rd_p=d191d14d-5ea3-4792-ae6c-e1de8a1c8780&pf_rd_r=3CW9PVM1RPX00B0NXX0G&pd_rd_wg=KHuRd&pd_rd_r=fe2deef8-f2d7-44dd-8763-d34d6d79888c&page=261'
                    response_data = self.amuk_request()
                    re_response_data = self.am_data(response_data)
                else:
                    print('------未找到任务队列--------')
                    self.dsdsdd.close()
                    time.sleep(60)
                    break
            except Exception as e:
                print(e)

    def get_ip(self):
        addrs = socket.getaddrinfo(socket.gethostname(), "")
        match = re.search("'192.168.(\d+.\d+)'", str(addrs))
        ip_num = "0.000"
        if match:
            ip_num = match.group(1)
        return ip_num


def am_run_spider():
    run_amazon_uk = AmazonUKSpiderShop()
    run_amazon_uk.run_amazonuk_spider()
    # run_amazon_uk.amuk_request()


if __name__ == '__main__':
    am_run_spider()






