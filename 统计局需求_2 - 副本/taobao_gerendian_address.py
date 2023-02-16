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

    def geren_address(self, i, shop_list_list):
        num = 0
        for shop_list in shop_list_list:
            sql = "select * from `taobao_goodsmobile_{}` where seller_id in {}".format(i, tuple(shop_list))

            # 需要更换查询的库名：session_104  session_227_tb
            daima_res = self.session_104_tb.query_tuple_data(sql)
            # daima_res = self.session_227_tb.query_tuple_data(sql)
            for daima_tm in daima_res:
                num += 1
                data = list(daima_tm)
                cid_tm = data[7]
                data[0] = str(data[0])
                data[1] = str(data[1])
                data[2] = str(data[2])
                data[3] = str(data[3])
                data[4] = str(data[4])
                data[5] = str(data[5])
                data[6] = str(data[6])
                data[7] = str(data[7])
                data[8] = str(data[8])
                data[9] = str(data[9])
                data[10] = str(data[10])
                data[11] = str(data[11])
                data[12] = str(data[12])
                data[13] = str(data[13])
                data[14] = str(data[14])
                data[15] = str(data[15])
                data[16] = str(data[16])
                data[17] = str(data[17])
                data[18] = str(data[18])
                data[19] = str(data[19])
                data[20] = str(data[20])
                data[21] = str(data[21])
                data[22] = str(data[22])
                data[23] = str(data[23])
                data[24] = str(data[24])
                data[25] = str(data[25])
                # data[26] = str(data[26])
                sales_vague = data[2]
                data.insert(2, sales_vague)
                daima_add = self.addres_dict_all.get(cid_tm)
                if daima_add != None:
                    data.append(daima_add)
                else:
                    g_a = 'E324'
                    data.append(g_a)
                data_tuple = tuple(data)
                self.data_list.append(data_tuple)
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
        insertion_sql = "insert into taobao_goodsmobile_{}_E_zj_all (update_date, goods_id, sales_month, sales_month1, comment_count, inventory, collect_num, address, cid, bid, bc_type, goods_name, seller_id, shop_id, advertising, discount_price, earnest, earnest_desc, price_name, price, ship_cost, assurance, promotion, promotion_desc, rewards, image_url, goods_info, E_daima) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)

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
        sql = "SELECT seller_id FROM `taobao_shopinfo_{}` WHERE `company` = '' AND `address` LIKE '%浙江%'".format(i)
        all_res = self.session_228.query_tuple_data(sql)
        for tuple_shopid in all_res:
            shopid = tuple_shopid[0]
            shop_id_list.append(shopid)

    def taobao_228_qiye_shop_id(self, i, shop_id_list):
        sql = "SELECT seller_id FROM `taobao_qiye_shopinfo_{}` WHERE `province` = '浙江省'".format(i)
        all_res = self.session_228.query_tuple_data(sql)
        for tuple_shopid in all_res:
            shopid = tuple_shopid[0]
            shop_id_list.append(shopid)

    def run_spdier(self):
        self.taobao_all_address()
        num = 10000
        for i in range(201911, 201913):
        # for i in range(201909, 201913):
            shop_id_list = []
            self.taobao_228_qiye_shop_id(i, shop_id_list)
            self.taobao_228_geren_shop_id(i, shop_id_list)
            shop_id_list_list = [shop_id_list[i:i+num] for i in range(0, len(shop_id_list), num)]
            self.geren_address(i, shop_id_list_list)


def run_r():
    r = GerenAddress()
    r.run_spdier()


if __name__ == '__main__':
    run_r()


