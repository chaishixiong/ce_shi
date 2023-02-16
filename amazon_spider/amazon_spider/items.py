# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    deatils_url = scrapy.Field()


class AmazonContentItem(scrapy.Item):
    asin = scrapy.Field()
    review_id = scrapy.Field()
    reviewer_name = scrapy.Field()
    reviewer_url = scrapy.Field()
    review_title = scrapy.Field()
    review_url = scrapy.Field()
    content = scrapy.Field()
    review_level = scrapy.Field()
    review_date = scrapy.Field()
    produt_size = scrapy.Field()
    produt_color = scrapy.Field()
    image = scrapy.Field()
    video = scrapy.Field()
    spider_flag = scrapy.Field()


