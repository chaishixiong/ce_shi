import requests
import re
import redis
from lxml import etree
from fake_useragent import UserAgent


class AmazonUKSpiderShop(object):
    def __init__(self):
        '''//span[@data-component-type="s-search-results"]/div[2]/div[2]/div/div/div/div/div/div/div/span/a/@href'''
        self.r = redis.Redis(host='192.168.1.4', port=6776, db=0, decode_responses=True)
        self.cache_queue = 'amazon_uk_category_url'
        self.url = 'https://www.amazon.co.uk'
        self.amazon_url = 'https://www.amazon.co.uk/sp?ie=UTF8&isCBA=&language=en_ZH&seller=A3MJVHNETLQ0MC&tab=&vasStoreID='
        self.category_url = open(r'X:\数据库\欧洲亚马逊\uk_seed\amazon_category_url.txt', 'a', encoding='utf-8')

    def am_request(self):
        location = r'C:\Users\Administrator\Desktop\测试\amazon\amazon_us\fake_useragent_0.1.11.json'
        ua = UserAgent(path=location).random
        headers = {
                      'authority': 'www.amazon.co.uk',
                      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                      'accept-language': 'zh-CN,zh;q=0.9',
                      'user-agent': ua,
                      'cookie': 'session-id=257-4644140-0926029; i18n-prefs=GBP; sp-cdn="L5Z9:CN"; ubid-acbuk=258-7305290-4044847; lc-acbuk=en_GB; av-timezone=Asia/Shanghai; session-id-time=2082787201l; session-token="ubk66fjb2WfGTh8YhdZqW0A3rZvdKjDEcif9jAv8hVfC/aVQknd5hU7lvhDnmIBEmobe8xV/PSbOjOqNjidX9dW8ySd+Yyi5CwMbO9kLUKUz0nASVYdn7ShPvhXQTfAlyCMZ1H+fKO0pXdOlOnrBXPMGfkTlGe8/AzjzsXUhiVQ0X4zMPbLxwy0RlQEF+H0k2rJhdnv/giht1ShjDvXI4rQYOE2585ytIorfBNKMtiA="; csm-hit=tb:P5S6KQ75QHFNZRV7F2Z1+s-Y2K6J7EA7N8BXXPR0G86|1669364583813&t:1669364583813&adb:adblk_no'
        }
        # print(self.amazon_url)
        r = requests.get(url=self.amazon_url, headers=headers)
        data_text = r.text.replace('\n', '').replace(' ', '')
        return r.text

    def if_yuansu_html(self, response_data):
        featured_categories = re.search(r'Featured categories', response_data)
        department = re.search(r'dir = "auto" > Department < / span >', response_data)
        response_data_html = etree.HTML(response_data)
        if department:
            categories_url = response_data_html.xpath(r"//a[@class='a-color-base a-link-normal']/@href")
        elif featured_categories:
            categories_url = response_data_html.xpath(r"//li[@class='octopus-pc-category-card-v2-item']/span/div/a/@href")
        else:
            categories_url = response_data_html.xpath(r'//div[@class="a-cardui-body"]/a/@href')
        if len(categories_url) > 0:
            for cat_url in categories_url:
                # 加入 redis 队列
                catgory = self.url + cat_url
                self.r.sadd(self.cache_queue, catgory)

        else:
            self.amuk_data(response_data)

    def amuk_data(self, response_data):
        # amazon_html = etree.HTML(response_data)
        # amazon_goods_url_list = amazon_html.xpath('//span[@data-component-type="s-search-results"]/div[2]/div/div/div/div/div/div/div/div/span/a/@href')
        page_num = re.search(r'aria-disabled="true">(\d+)<', response_data)
        if page_num == None:
            self.r.sadd(self.cache_queue, self.amazon_url)
            self.category_url.write(self.amazon_url + '\n')
            self.category_url.flush()
        else:
            int_page_num = int(page_num.group(1))+1
            for num in range(1, int_page_num):
                amazon_category_url = self.amazon_url.strip('\n') + '&page={}'.format(num)
                self.r.sadd(self.cache_queue, amazon_category_url)
                self.category_url.write(amazon_category_url + '\n')
                self.category_url.flush()

    def run_amazonuk_spider(self):
        with open(r'X:\数据库\欧洲亚马逊\uk_seed\amazon_category_url.txt', 'r', encoding='utf-8') as url_list:
            for url in url_list:
                amazon_url = url.strip('\n')
                self.r.sadd(self.cache_queue, amazon_url)
                # amazon_url = self.url + url.strip('\n')
                # self.r.sadd(self.cache_queue, amazon_url)
                # self.amazon_url = 'https://www.amazon.co.uk/gp/browse.html?node=10745681&ref_=nav_em__furniture_t2_0_2_12_6'
        # while True:
        #     self.amazon_url = self.r.spop(self.cache_queue)
        #     if self.amazon_url != None:
        #         response_data = self.am_request()
        #         self.if_yuansu_html(response_data)
        #     else:
        #         break
        # self.category_url.close()


def amuk_run_spider():
    run_amazon_uk = AmazonUKSpiderShop()
    run_amazon_uk.run_amazonuk_spider()


if __name__ == '__main__':
    amuk_run_spider()






