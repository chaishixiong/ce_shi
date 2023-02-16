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
        for shop_list in shop_list_list:
            self.insertion_data(shop_list, i)

    def insertion_data(self, data_list, i):
        # 无farm_flag字段：2021-1-3   20201-10
        insertion_sql = "insert into taobao_shopinfo_{}_tj (shop_id, seller_id, bc_type, main_sale, company, sales_count, sales_money, address, seller_name, seller_lv, shop_hpl, shop_name, weitao_id, shop_fans_num, open_shop_date, goods_num, new_goods_num, guanzhu_num, shop_money, shop_iocn, gold_shop, shop_type, taobao_shop_type2, taobao_shop_type3, open_year, taobao_tel, company_change, last_sales_money,vix,province,city,xinyong,describe_rate,service_rate,logistics_rate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)

        # 有farm_flag字段：2020-11-12
        # insertion_sql = "insert into taobao_goodsmobile_20210{}_E_zj (update_date, goods_id, sales_month, sales_month1, comment_count, inventory, collect_num, address, cid, bid, bc_type, goods_name, seller_id, shop_id, advertising, discount_price, earnest, earnest_desc, price_name, price, ship_cost, assurance, promotion, promotion_desc, rewards, image_url, goods_info,farm_flag, E_daima) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)

        # 插入库名： session_227_tb
        self.session_228.insertion_data_list(insertion_sql, data_list)

    def taobao_all_address(self):
        sql = "select * from all_goodsinfo_daima"
        all_res = self.session_227_tb.query_tuple_data(sql)
        for address_data in all_res:
            cid = address_data[0]
            E_daima = address_data[1]
            self.addres_dict_all[cid] = E_daima

    def taobao_228_geren_shop_id(self, i, shop_id_list):
        sql = "SELECT * FROM `taobao_shopinfo_{}` WHERE `company` = '' AND `province` in ('上海','江苏','浙江','安徽')".format(i)
        all_res = self.session_228.query_tuple_data(sql)
        for tuple_shopid in all_res:
            shop_id_list.append(tuple_shopid)

    def run_spdier(self):
        self.taobao_all_address()
        num = 10000
        # for i in range(202205, 202206):
        for i in range(201901, 201913):
            data_list = []
            # self.taobao_228_qiye_shop_id(i, shop_id_list)
            self.taobao_228_geren_shop_id(i, data_list)
            print('taobao_shopinfo_{}'.format(i))
            shop_id_list_list = [data_list[i:i+num] for i in range(0, len(data_list), num)]
            self.geren_address(i, shop_id_list_list)


def run_r():
    r = GerenAddress()
    r.run_spdier()


if __name__ == '__main__':
    run_r()


