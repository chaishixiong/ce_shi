import scrapy
import redis
from amazon_spider.amazon_spider.items import AmazonContentItem
import json
import time
from amazon_spider.amazon_spider.dbsetting import Url_r, port_r, passwd_r
"""
从redis数据库中获取详情评论页并解析获取数据，并翻页获取。构造分布式的消费者。
"""


class ContentSpider(scrapy.Spider):
    name = 'content'

    def start_requests(self):
        # 连接redis数据库，从redis中获取详情页URL，并移除数据库。
        r = redis.Redis.from_url("redis://:{}@{}:{}/5".format(passwd_r, Url_r, port_r),
                                 decode_responses=True)
        # r = redis.Redis.from_url("redis://127.0.0.1:6379", decode_responses=True)
        if "deatils_url" in r.keys():
            # while True:
            for i in range(1):
                if "deatils_url" in r.keys():
                    url = r.spop('deatils_url')  # spop(self, name, count=None):移除并返回集合中的一个随机元素
                    print(url)
                    yield scrapy.Request(
                        url=url,
                        method="GET",
                        callback=self.parse,
                        dont_filter=True,
                    )
                else:
                    print("redis数据库中URL已经取完")
                    break

    def parse(self, response):
        # 页面解析，数据提取
        date_time = time.strftime("%Y-%m-%d")

        amazom_review_item = AmazonContentItem()
        amazom_review_item['spider_flag'] = date_time
        amazom_review_list = response.xpath('//div[@data-hook="review"]')
        try:
            for amazon_review in amazom_review_list:
                if amazon_review.xpath('//*[@id="cm_cr-rvw_summary"]/script/text()'):
                    amazom_review_item['asin'] = \
                        json.loads(amazon_review.xpath('//*[@id="cm_cr-rvw_summary"]/script/text()').extract_first())[
                            "asin"]
                else:
                    amazom_review_item['asin'] = None
                amazom_review_item["review_id"] = amazon_review.xpath('./@id').extract_first()
                if amazon_review.xpath('.//span[@class="a-profile-name"]/text()'):
                    amazom_review_item["reviewer_name"] = amazon_review.xpath(
                        './/span[@class="a-profile-name"]/text()').extract_first()
                if amazon_review.xpath('.//div[@data-hook="genome-widget"]/a/@href'):
                    amazom_review_item["reviewer_url"] = "https://www.amazon.com" + amazon_review.xpath(
                        './/div[@data-hook="genome-widget"]/a/@href').extract_first()
                if amazon_review.xpath(
                        './/span[@class="a-icon-alt"]/text()'):
                    amazom_review_item["review_level"] = amazon_review.xpath(
                        './/span[@class="a-icon-alt"]/text()').extract_first()[:3]
                if amazon_review.xpath(
                        './/a[@data-hook="review-title"]/span/text()'):
                    amazom_review_item["review_title"] = amazon_review.xpath(
                        './/a[@data-hook="review-title"]/span/text()').extract_first()
                review_url = amazon_review.xpath('.//a[@data-hook="review-title"]/@href')
                if review_url:
                    amazom_review_item["review_url"] = "https://www.amazon.com" + amazon_review.xpath(
                        './/a[@data-hook="review-title"]/@href').extract_first()
                    if amazom_review_item['asin'] == None:
                        amazom_review_item['asin'] = review_url[0][review_url.extract_first().find('ASIN') + 5:]
                if amazon_review.xpath(
                        './/span[@data-hook="review-date"]/text()'):
                    amazom_review_item["review_date"] = amazon_review.xpath(
                        './/span[@data-hook="review-date"]/text()').extract_first()[:-6]
                amazom_review_item["content"] = "\n".join(
                    amazon_review.xpath('.//span[@data-hook="review-body"]//span/text()').extract()).strip()
                if len(amazon_review.xpath('.//a[@data-hook="format-strip"]/text()').extract()) == 1:
                    if "Size" in amazon_review.xpath('.//a[@data-hook="format-strip"]/text()').extract()[0]:
                        amazom_review_item["produt_size"] = \
                            amazon_review.xpath('.//a[@data-hook="format-strip"]/text()').extract()[0]
                        amazom_review_item["produt_color"] = []
                    elif "Color" in amazon_review.xpath('.//a[@data-hook="format-strip"]/text()').extract()[0]:
                        amazom_review_item["produt_color"] = \
                            amazon_review.xpath('.//a[@data-hook="format-strip"]/text()').extract()[0]
                        amazom_review_item["produt_size"] = []
                elif len(amazon_review.xpath('.//a[@data-hook="format-strip"]/text()').extract()) == 2:
                    amazom_review_item["produt_size"] = \
                        amazon_review.xpath('.//a[@data-hook="format-strip"]/text()').extract()[0]
                    amazom_review_item["produt_color"] = \
                        amazon_review.xpath('.//a[@data-hook="format-strip"]/text()').extract()[1]
                else:
                    amazom_review_item["produt_size"] = []
                    amazom_review_item["produt_color"] = []
                amazom_review_item["video"] = set(amazon_review.xpath(
                    './/span[@data-hook="review-body"]//source/@src').extract())
                if not amazom_review_item["video"]:
                    amazom_review_item["video"] = []

                # amazom_review_item["image"] = set(amazon_review.xpath(
                #     './/img[@alt="review image"]/@src').extract())

                image_list = []
                for image in amazon_review.xpath('.//img[@alt="review image"]/@src').extract():
                    image = image[:-9] + "jpg"
                    image_list.append(image)
                amazom_review_item["image"] = set(image_list)

                if not amazom_review_item["image"]:
                    amazom_review_item["image"] = []
                yield amazom_review_item
        except Exception as e:
            print("错误信息：{}".format(e))

        # 下一页的URL提取
        if response.xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a/@href').extract_first():
            next_url = "https://www.amazon.com" + response.xpath(
                '//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a/@href').extract_first()

            yield scrapy.Request(
                url=next_url,
                method="GET",
                callback=self.parse,
                meta={"item": amazom_review_item},

                dont_filter=True
            )
