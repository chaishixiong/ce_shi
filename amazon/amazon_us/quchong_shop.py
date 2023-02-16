from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import kj_1_4_pool
# pymysql.converters.escape_string()  新规范


class AmazonUk(object):
    def __init__(self):
        self.session_227_kj = DataBaseSession(kj_1_4_pool)
        self.data_time = ''
        self.data_list = []
        self.company_list = dict()
        self.shop_set = set()
        self.new_shop = open(r'X:\数据库\美国亚马逊\amazon_shopseed.txt', 'w', encoding='utf-8')
        # self.new_shop = open(r'W:\scrapy_seed\amazon_sortshop.txt', 'w', encoding='utf-8')

    def goods_query_dict(self):
        query_sql = "SELECT goods_id FROM `amazonus_goodsinfo_202212`"
        sql_data = self.session_227_kj.query_tuple_data(query_sql)
        for id in sql_data:
            goods_id = id[0]
            self.company_list[goods_id] = 1
        return sql_data

    def shop_query_dict(self):
        query_sql = "SELECT shop_id FROM `amazonus_shopinfo_202212_sales`"
        sql_data = self.session_227_kj.query_tuple_data(query_sql)
        for id in sql_data:
            shop_id = id[0]
            self.shop_set.add(shop_id)
        # return sql_data

    def run_spider(self):
        self.shop_query_dict()
        with open(r'X:\数据库\美国亚马逊\us_seed\amazon_sortshop_data_合并.txt[F2].txt', 'r', encoding='utf-8') as r_shop_id:
            for shop in r_shop_id:
                shop_id = shop.strip('\n')
                if shop_id not in self.shop_set:
                    self.new_shop.write(shop)
                    self.new_shop.flush()
            self.new_shop.close()

        # self.goods_query_dict()
        # with open(r'X:\数据库\美国亚马逊\us_seed\amazon_goods_id\amazon_cat_url_合并.txt', 'r', encoding='utf-8') as c_goods_id:
        #     for cgoods in c_goods_id:
        #         cgoods_id = cgoods.strip('\n')
        #         c_data = self.company_list.get(cgoods_id)
        #         if c_data == None:
        #             self.new_shop.write(cgoods)
        #             self.new_shop.flush()
        #     self.new_shop.close()


def run_amazon_uk():
    run = AmazonUk()
    run.run_spider()


if __name__ == '__main__':
    run_amazon_uk()














