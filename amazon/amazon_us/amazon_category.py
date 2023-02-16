import requests
import re
import redis
from lxml import etree
from fake_useragent import UserAgent


class AmazonSpiderShop(object):
    def __init__(self):
        '''//span[@data-component-type="s-search-results"]/div[2]/div[2]/div/div/div/div/div/div/div/span/a/@href'''
        self.r = redis.Redis(host='192.168.1.4', port=6776, db=0, decode_responses=True)
        self.cache_queue = 'amazon_category_url'
        self.amazon_url = ''
        self.category_url = open(r'X:\数据库\速卖通\seed\amazon_category_url.txt', 'a', encoding='utf-8')

    def am_request(self):
        location = r'C:\Users\Administrator\Desktop\测试\amazon\amazon_us\fake_useragent_0.1.11.json'
        ua = UserAgent(path=location).random
        headers = {
                      'authority': 'www.amazon.com',
                      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                      'accept-language': 'zh-CN,zh;q=0.9',
                      'user-agent': ua,
                      'cookie': 'session-id=137-0489966-7453666; i18n-prefs=USD; ubid-main=132-2961476-4810337; session-id-jp=355-9057861-4050835; ubid-acbjp=357-3763949-7715242; s_pers=%20s_fid%3D227B8ED09C84DAE8-27437224EA0E76B0%7C1807154523899%3B%20s_dl%3D1%7C1649389923899%3B%20gpv_page%3DSC%253AJP%253AWP-Welcome%7C1649389923900%3B%20s_ev15%3D%255B%255B%2527SCJPWPDirect%2527%252C%25271649388123902%2527%255D%255D%7C1807154523902%3B; _msuuid_jniwozxj70=51330998-3131-4986-A668-C134D7FD8B2B; s_nr=1666168416409-Repeat; s_vnum=2098149743861%26vn%3D2; s_dslv=1666168416410; skin=noskin; av-timezone=Asia/Shanghai; sp-cdn="L5Z9:CN"; lc-main=zh_CN; session-id-time=2082787201l; session-token="LPyOjZNgItBfvhcuyHm4wl/dkMTujEa+7arIvc3i9zWtbwv0EPWHvaZO/rT9Qy9ka1N1tgfX1yW4vkDHPMaZrqRCsqEZz0cvMUaPXbkt7K6xijuOB01/1+RQRoVqJTe/XlX7Oz65cLK7/1b80YDcHcYWPYgAks/V8jvYEVtKKR4HjVEKnFu1gAh2Ta8n6G9AjSaqnGX6zZXQshWRdor9rtnbyLXmFr3iSfE71yU+uWQ="; csm-hit=tb:KKXB9GWHQDYCAN4C4VY6+s-KKXB9GWHQDYCAN4C4VY6|1666849312175&t:1666849312175&adb:adblk_no'
        }
        print(self.amazon_url)
        r = requests.get(url=self.amazon_url, headers=headers)
        return r.text

    def am_data(self, response_data):
        # amazon_html = etree.HTML(response_data)
        # amazon_goods_url_list = amazon_html.xpath('//span[@data-component-type="s-search-results"]/div[2]/div/div/div/div/div/div/div/div/span/a/@href')
        page_num = re.search(r'aria-disabled="true">(\d+)<', response_data)
        if page_num == None:
            self.r.sadd(self.cache_queue, self.amazon_url)
        else:
            int_page_num = int(page_num.group(1))+1
            for num in range(1, int_page_num):
                amazon_category_url = self.amazon_url.strip('\n') + '&page={}'.format(num)
                self.r.sadd(self.cache_queue, amazon_category_url)
                self.category_url.write(amazon_category_url + '\n')
                self.category_url.flush()

    def run_amazon_spider(self):
        # with open(r'amazon_shopinfo.txt', 'r', encoding='utf-8') as url_list:
        #     for url in url_list:
        #         self.amazon_url = 'https://www.amazon.com' + url
        #         response_data = self.am_request()
        #         re_response_data = self.am_data(response_data)
        #     self.category_url.close()
        # for page in range(3, 401):
        #     amazon_url = 'https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A281407&page={}&qid=1666181786&ref=sr_pg_{}'.format(page, page)
        #     response_data = self.am_request(amazon_url)
        #     re_response_data = self.am_data(response_data)
        with open(r'X:\数据库\美国亚马逊\us_seed\amazon_category_url.txt', 'r', encoding='utf-8') as url_list:
            for url in url_list:
                amazon_category_url = url.strip('\n')
                self.r.sadd(self.cache_queue, amazon_category_url)


def am_run_spider():
    run_amazon = AmazonSpiderShop()
    run_amazon.run_amazon_spider()


if __name__ == '__main__':
    am_run_spider()






