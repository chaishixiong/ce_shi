from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import tb_104_pool, jd_228_pool, tb_pool


class GerenAddress(object):
    def __init__(self):
        self.session_104 = DataBaseSession(tb_104_pool)
        self.session_228 = DataBaseSession(jd_228_pool)
        self.session_227 = DataBaseSession(tb_pool)
        self.addres_dict_all = {}
        self.data_list = []

    def geren_address(self, i):
        num = 0
        sql = "select * from taobao_goodsmobile_20200{}".format(i)
        daima_res = self.session_104.query_tuple_data(sql)
        for daima_tm in daima_res:
            num += 1
            data = list(daima_tm)
            cid_tm = data[8]
            daima_add = self.addres_dict_all.get(cid_tm)
            if daima_add != None:
                data.append(daima_add)
            else:
                g_a = ''
                data.append(g_a)
            data_tuple = tuple(data)
            self.data_list.append(data_tuple)
            if num % 30000 == 0:
                self.insertion_data(i)
                self.data_list = []
                print(num)
        if len(self.data_list) > 0:
            pass
            self.insertion_data(i)
            self.data_list = []



    def insertion_data(self, i):
        # 无farm_flag字段：2021-1-3   20201-10
        insertion_sql = "insert into taobao_goodsmobile_20200{}_E (update_date, goods_id, sales_month, sales_month1, comment_count, inventory, collect_num, address, cid, bid, bc_type, goods_name, seller_id, shop_id, advertising, discount_price, earnest, earnest_desc, price_name, price, ship_cost, assurance, promotion, promotion_desc, rewards, image_url, goods_info, E_daima) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)

        # 有farm_flag字段：2020-11-12
        # insertion_sql = "insert into taobao_goodsmobile_20210{}_E (update_date, goods_id, sales_month, sales_month1, comment_count, inventory, collect_num, address, cid, bid, bc_type, goods_name, seller_id, shop_id, advertising, discount_price, earnest, earnest_desc, price_name, price, ship_cost, assurance, promotion, promotion_desc, rewards, image_url, goods_info,farm_flag, E_daima) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)

        self.session_227.insertion_data(insertion_sql, self.data_list)

    def taobao_all_address(self):
        sql = "select * from all_goodsinfo_daima"
        all_res = self.session_228.query_tuple_data(sql)
        for address_data in all_res:
            cid = address_data[0]
            E_daima = address_data[1]
            self.addres_dict_all[cid] = E_daima

    def taobao_228_shop_id(self, i):
        sql = "SELECT shop_id FROM `jd_shopinfo_20210{}` where province = '浙江省'".format(i)
        all_res = self.session_228.query_tuple_data(sql)
        for tuple_shopid in all_res:
            shopid = tuple_shopid[0]
            E_daima = tuple_shopid[1]
            self.addres_dict_all[shopid] = E_daima

    def run_spdier(self):
        self.taobao_all_address()
        for i in range(202112, 202113):
        # for i in range(2, 8):
            self.session_228(i)
            self.geren_address(i)


def run_r():
    r = GerenAddress()
    r.run_spdier()


if __name__ == '__main__':
    run_r()

