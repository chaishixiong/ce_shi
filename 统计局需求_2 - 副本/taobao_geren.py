from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import tb_pool, shop_228_pool, tb_104_pool, e_commerce_104


class GerenAddress(object):
    def __init__(self):
        self.session_228 = DataBaseSession(shop_228_pool)
        self.session_227_tb = DataBaseSession(tb_pool)
        self.session_104_tb = DataBaseSession(tb_104_pool)
        self.e_commerce_104_tm = DataBaseSession(e_commerce_104)
        self.addres_dict_all = {}
        self.data_list = []

    def geren_address(self, i):
        num = 0
        sql = "select * from `taobao_goodsmobile_{}`".format(i)

        # 需要更换查询的库名：session_104  session_227_tb
        daima_res = self.session_104_tb.query_tuple_data(sql)
        # daima_res = self.session_227_tb.query_tuple_data(sql)
        for daima_tm in daima_res:
            num += 1
            self.data_list.append(daima_tm)
            if num % 10000 == 0:
                self.insertion_data(i)
                self.data_list = []
                print(num)
        if len(self.data_list) > 0:
            print(num)
            self.insertion_data(i)
            self.data_list = []

    def insertion_data(self, i):
        # 无farm_flag字段：2021-1-3   20201-10
        insertion_sql = "insert into taobao_goodsmobile_{} (update_date, goods_id, sales_month, sales_month1, comment_count, inventory, collect_num, address, cid, bid, bc_type, goods_name, seller_id, shop_id, advertising, discount_price, earnest, earnest_desc, price_name, price, ship_cost, assurance, promotion, promotion_desc, rewards, image_url, goods_info) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)

        # 有farm_flag字段：2020-11-12
        # insertion_sql = "insert into taobao_goodsmobile_20210{}_E_zj (update_date, goods_id, sales_month, sales_month1, comment_count, inventory, collect_num, address, cid, bid, bc_type, goods_name, seller_id, shop_id, advertising, discount_price, earnest, earnest_desc, price_name, price, ship_cost, assurance, promotion, promotion_desc, rewards, image_url, goods_info,farm_flag, E_daima) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)

        # 插入库名： session_227_tb
        self.session_227_tb.insertion_data_list(insertion_sql, self.data_list)

    def taobao_all_address(self):
        sql = "select * from all_goodsinfo_daima"
        all_res = self.session_227_tb.query_tuple_data(sql)
        for address_data in all_res:
            cid = address_data[0]
            E_daima = address_data[1]
            self.addres_dict_all[cid] = E_daima

    def taobao_228_geren_shop_id(self, i, shop_id_list):
        sql = "SELECT seller_id FROM `taobao_shopinfo_{}` WHERE `company` = '' AND `province` LIKE '江苏'".format(i)
        all_res = self.session_228.query_tuple_data(sql)
        for tuple_shopid in all_res:
            shopid = tuple_shopid[0]
            shop_id_list.append(shopid)

    def taobao_228_qiye_shop_id(self, i, shop_id_list):
        sql = "SELECT seller_id FROM `taobao_qiye_shopinfo_{}` WHERE `province` = '江苏省'".format(i)
        all_res = self.session_228.query_tuple_data(sql)
        for tuple_shopid in all_res:
            shopid = tuple_shopid[0]
            shop_id_list.append(shopid)

    def run_spdier(self):
        # self.taobao_all_address()
        for i in range(201901, 201904):
            self.geren_address(i)


def run_r():
    r = GerenAddress()
    r.run_spdier()


if __name__ == '__main__':
    run_r()


