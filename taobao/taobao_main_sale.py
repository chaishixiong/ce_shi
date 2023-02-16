from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import tm_228_pool


class TBMainSale(object):
    def __init__(self):
        self.session_227_tb = DataBaseSession(tm_228_pool)
        self.addres_dict_all = {}
        self.data_list = []

    def geren_address(self, b):
        num = 0
        sql = "select shop_id,main_sale from tmall_shopinfo_{}  where province = '浙江省'".format(b)
        daima_res = self.session_227_tb.query_tuple_data(sql)
        for daima_tm in daima_res:
            num += 1
            data = list(daima_tm)
            shop_id = data[0]
            main_sale_7 = self.addres_dict_all[shop_id]
            main_sale = data[1]
            if len(main_sale) > 0:
                if main_sale_7 != main_sale:
                    print(str(shop_id) + ':' + '7月：' + main_sale_7 + '8月：' + main_sale)

    def taobao_all_address(self, i):
        sql = "select shop_id,main_sale from tmall_shopinfo_{} where province = '浙江省'".format(i)
        all_res = self.session_227_tb.query_tuple_data(sql)
        for address_data in all_res:
            shop_id = address_data[0]
            main_sale = address_data[1]
            self.addres_dict_all[shop_id] = main_sale

    def run_spdier(self):
        i = 202207
        b = 202208
        self.taobao_all_address(i)
        self.geren_address(b)


def run_r():
    r = TBMainSale()
    r.run_spdier()


if __name__ == '__main__':
    run_r()


