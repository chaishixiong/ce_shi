from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import tb_pool, tm_pool


class NewShop(object):
    def __init__(self):
        self.tb_new_shop227 = DataBaseSession(tb_pool)
        self.tm_new_shop227 = DataBaseSession(tm_pool)
        self.shop_id_dict = {}
        self.data_list = []

    def new_shop_id(self):
        num = 0
        sql = """SELECT * from(
SELECT * from taobao_shopinfo_202207_add where shop_id <> ''
union
SELECT * from taobao_shopinfo_202208_add where shop_id <> ''
)
as a GROUP BY shop_id"""
        # 需要更换查询的库名：session_104  session_227_tm
        daima_res = self.tb_new_shop227.query_tuple_data(sql)
        for daima_tm in daima_res:
            num += 1
            data = list(daima_tm)
            shop_id = data[0]
            daima_add = self.shop_id_dict.get(shop_id)
            if daima_add == None:
                self.data_list.append(daima_tm)
            if num % 10000 == 0:
                self.insertion_data()
                self.data_list = []
                print(num)
        if len(self.data_list) > 0:
            self.insertion_data()
            self.data_list = []

    def insertion_data(self):
        insertion_sql = "insert into taobao_shopinfo_202208_add_new_shop (shop_id, seller_id, shop_name, shop_type, address, shop_hpl, shop_url, good_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        self.tb_new_shop227.insertion_data_list(insertion_sql, self.data_list)

    def all_shop_id(self):
        tb_sql = "select shop_id from taobao_shopinfo_202206"
        tb_all_shop = self.tb_new_shop227.query_tuple_data(tb_sql)
        tm_sql = 'select shop_id from tmall_shopinfo_202206'
        tm_all_shop = self.tm_new_shop227.query_tuple_data(tm_sql)
        for tbone_shop in tb_all_shop:
            self.shop_id_dict[tbone_shop[0]] = tbone_shop[0]
        for tmone_shop in tm_all_shop:
            self.shop_id_dict[tmone_shop[0]] = tmone_shop[0]

    def run_spdier(self):
        self.all_shop_id()
        self.new_shop_id()


def run_r():
    r = NewShop()
    r.run_spdier()


if __name__ == '__main__':
    run_r()



