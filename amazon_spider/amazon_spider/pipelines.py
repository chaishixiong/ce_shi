# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import time
import pymysql
from amazon_spider.amazon_spider.dbsetting import host, port, user, passwd, db

# 详情页URL的存储
class AmazonPipeline(object):

        def __init__(self):
            self.conn = None
            self.cursor = None

        def open_spider(self, spider):
            self.start = time.time()
            try:
                self.conn = pymysql.connect(
                    host=host,
                    port=port,
                    user=user,
                    password=passwd,
                    db=db,
                    charset="utf8"
                )
                print("数据库连接成功<<")

            except Exception as e:
                print("数据库连接失败！！>>{}".format(e))
                exit()

        def process_item(self, item, spider):
            self.cursor = self.conn.cursor()
            value = (
                str(item["deatils_url"])
                )

            try:
                # 插入数据
                sql = 'insert into asin_deatils_url(deatils_url) values(%s)'

                self.cursor.execute(sql, value)
                # 提交到数据库
                print("数据提交数据库>>")
                self.conn.commit()
            except Exception as e:
                print(">>数据存储失败>>｜>>{}".format(e))
                # 回滚数据到什么都不做的状态  即撤销刚刚的操作
                self.conn.rollback()

            return item

        def close_spider(self, spider):
            self.end = time.time()
            print("数据存储完成！")
            # 先关闭游标
            # self.cursor.close()
            # 再关闭连接
            self.conn.close()
            total_time = self.end - self.start
            print("此次爬虫共计耗时{}".format(total_time))


# 评论数据存储
class AmazonspiderPipeline(object):

    def __init__(self):
        self.conn = None
        self.cursor = None

    def open_spider(self, spider):
        self.start = time.time()
        try:
            self.conn = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=passwd,
                db=db,
                charset="utf8"
            )
            print("数据库连接成功<<")

        except Exception as e:
            print("数据库连接失败！！>>{}".format(e))
            exit()

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        value = (
            str(item["asin"]), str(item["review_id"]), str(item["reviewer_name"]),
            str(item["reviewer_url"]),
            str(item["review_title"]), str(item["review_url"]),
            str(item["content"]), str(item["review_level"]), str(item["review_date"]), str(item["image"]),
            str(item["video"]), str(item["produt_size"]), str(item["produt_color"]), str(item["spider_flag"]))

        try:
            # 插入数据
            sql = 'insert into reviews_request(asin,review_id,reviewer_name,reviewer_url,review_title,review_url,content,review_level,review_date,image,video,produt_size,produt_color,spider_flag) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

            self.cursor.execute(sql, value)
            # 提交到数据库
            print("数据提交数据库>>")
            self.conn.commit()
        except Exception as e:
            print(">>数据存储失败>>｜>>{}".format(e))
            # 回滚数据到什么都不做的状态  即撤销刚刚的操作
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.end = time.time()
        print("数据存储完成！")
        # 先关闭游标
        # self.cursor.close()
        # 再关闭连接
        self.conn.close()
        total_time = self.end - self.start
        print("此次爬虫共计耗时{}".format(total_time))


