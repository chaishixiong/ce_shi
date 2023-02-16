from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import jd_104_pool, jd_228_pool, jd_pool


class GerenAddress(object):
    def __init__(self):
        self.session_104 = DataBaseSession(jd_104_pool)
        self.session_227_jd = DataBaseSession(jd_pool)
        self.session_228 = DataBaseSession(jd_228_pool)
        self.addres_dict_all = {}
        self.data_list = []

    def geren_address(self, i, shop_list):
        num = 0
        sql = "SELECT * FROM `jd_goodsinfo_{}` where shop_id in {}".format(i, shop_list)

        # 需要更换查询的库名：session_104  session_227_jd
        daima_res = self.session_227_jd.query_tuple_data(sql)
        for daima_tm in daima_res:
            num += 1
            data = list(daima_tm)
            # cid_tm = data[9]
            cid_tm = data[4]
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
        # 202103
        # insertion_sql = "insert into jd_goodsinfo_2020{}_E_zj (shop_id, VID, PID, mian_goods_id, goods_id, bid, brand_name, CID1, CID2, CID3, c_name1, c_name2, c_name3, is_ebook, price, comment, realcomment, goods_name, data_month, E_daima) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)

        # 202104
        # insertion_sql = "insert into jd_goodsinfo_20210{}_E_zj (shop_id, goods_id, picture_url, goods_name, CID3, CID2, CID1, comment, price, favorable, realcomment, E_daima) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)

        # 202105-202110
        insertion_sql = "insert into jd_goodsinfo_{}_E_zj (shop_id, goods_id, mian_goods_id, goods_name, CID3, CID2, CID1, comment, price, good_comment, realcomment, c_name1, c_name2, c_name3, bid, brand_name, data_month, E_daima) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)
        self.session_227_jd.insertion_data(insertion_sql, self.data_list)

    def taobao_all_address(self):
        sql = "select * from all_jd_goodsinfo_daima"
        all_res = self.session_227_jd.query_tuple_data(sql)
        for address_data in all_res:
            cid = address_data[0]
            E_daima = address_data[1]
            self.addres_dict_all[cid] = E_daima

    def jd_228_shop_id(self, i):
        sql = "SELECT shop_id FROM `jd_shopinfo_{}` where province = '浙江省'".format(i)
        all_res = self.session_228.query_tuple_data(sql)
        shop_id_list = []
        for tuple_shopid in all_res:
            shopid = tuple_shopid[0]
            shop_id_list.append(shopid)
        tuple_shop_list = tuple(shop_id_list)
        return tuple_shop_list

    def run_spdier(self):
        self.taobao_all_address()
        # for i in range(202101, 202113):
        for i in range(202108, 202111):
            tuple_shop_list = self.jd_228_shop_id(i)
            self.geren_address(i, tuple_shop_list)


def run_r():
    r = GerenAddress()
    r.run_spdier()


if __name__ == '__main__':
    run_r()
