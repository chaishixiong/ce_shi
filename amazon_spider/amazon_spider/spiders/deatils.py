
import scrapy
import pymysql
from amazon_spider.amazon_spider.items import AmazonItem
from amazon_spider.amazon_spider.dbsetting import host_test,port_test,user_test,passwd_test,db_test
"""
获取有效的详情评论页的URL
"""

class YmxSpider(scrapy.Spider):
    name = 'deatils'


    def start_requests(self):
        # 连接数据库获取asin，拼接URL
        conn = pymysql.Connect(
            host=host_test,
            port=port_test,
            user=user_test,
            password=passwd_test,
            db=db_test
        )
        cur = conn.cursor()
        sql = "select asin from ybs_sku"
        cur.execute(sql)
        result_asin = cur.fetchall()
        asin_list = []
        # 过滤重复的asin
        for asin in result_asin:
            if asin[0]:
                if asin[0] not in asin_list:
                    asin_list.append(asin[0])
        # 拼接目标URL
        for Asin in asin_list:
            if Asin:
                URL = 'https://www.amazon.com/dp/' + Asin
                yield scrapy.Request(
                    url=URL,
                    method="GET",
                    callback=self.parse,
                    dont_filter=True,
                )

    def parse(self, response):
        # 解析获取有效的详情评论页的URL
        title = response.xpath('//title/text()').extract_first()
        if "找不到页面" in title:
            return
        # if response.status == 200:
        try:
            deatils_url = AmazonItem()
            # if response.xpath('//*[@id="reviews-medley-footer"]/div[2]/a/@href'):
            deatils_url["deatils_url"] = "https://www.amazon.com/-/zh" + response.xpath(
                '//*[@id="reviews-medley-footer"]/div[2]/a/@href').extract_first()

            yield deatils_url
        except Exception as e:
            print("该{}页面发生错误{}".format(response.url, e))
