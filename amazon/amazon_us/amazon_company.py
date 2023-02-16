import requests
import re, time
import redis
from lxml import etree
from fake_useragent import UserAgent


class AmazonSpiderCompany(object):
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
                    "authority": "www.qcc.com",
                    "accept": "*/*",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "cookie": "qcc_did=0d209acd-6f78-421d-92ef-3dc92fec2300; QCCSESSID=2c260be2cce452a6ac8742c788; UM_distinctid=184f0fce65b308-01e7f2e2db6484-26021151-240000-184f0fce65cc41; _uab_collina=167100804458975311643895; CNZZDATA1254842228=411718242-1654741486-https%253A%252F%252Ftop.qcc.com%252F%7C1671090124; acw_tc=3da4731816710926636767096e6a70f94a3aa16933d6849db0266e3ac4",
                    "referer": "https://www.qcc.com/web/search?key=shanghaiyuanfandianzishangwuyouxiangongsi",
                    "sec-ch-ua": '^\^"Not?A_Brand^\^";v=^\^"8^\^", ^\^"Chromium^\^";v=^\^"108^\^", ^\^"Google Chrome^\^";v=^\^"108^\^"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '^\^"Windows^\^"',
                    "sec-fetch-dest": "script",
                    "sec-fetch-mode": "no-cors",
                    "sec-fetch-site": "same-origin",
                    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        }
        # print(self.amazon_url)
        r = requests.get(url=self.amazon_url, headers=headers)
        return r.text

    def am_data(self, response_data):
        amazon_html = etree.HTML(response_data)
        legal_person = re.search(r'window.__INITIAL_STATE__=(.*);\(function', response_data).group(1)
        print(legal_person)
        # page_num = re.search(r'aria-disabled="true">(\d+)<', response_data)
        # if page_num == None:
        #     self.r.sadd(self.cache_queue, self.amazon_url)
        # else:
        #     int_page_num = int(page_num.group(1))+1
        #     for num in range(1, int_page_num):
        #         amazon_category_url = self.amazon_url.strip('\n') + '&page={}'.format(num)
        #         self.r.sadd(self.cache_queue, amazon_category_url)
        #         self.category_url.write(amazon_category_url + '\n')
        #         self.category_url.flush()

    def run_amazon_company_spider(self):
        while True:
            self.amazon_url = 'https://www.qcc.com/web/search?key=Xiangchengshiyuefafazhipinyouxiangongsi&isTable=true'
            response_data = self.am_request()
            re_response_data = self.am_data(response_data)
            # time.sleep(10)


def am_run_spider():
    run_amazon = AmazonSpiderCompany()
    run_amazon.run_amazon_company_spider()


if __name__ == '__main__':
    am_run_spider()






