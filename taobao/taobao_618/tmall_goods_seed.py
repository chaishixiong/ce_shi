from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import tm_104_pool, tm_pool, shop_228_pool


class GerenAddress(object):
    def __init__(self):
        self.session_228 = DataBaseSession(shop_228_pool)
        self.session_227_tm = DataBaseSession(tm_pool)
        self.session_104_tm = DataBaseSession(tm_104_pool)
        self.addres_dict_all = {}
        self.data_list = []
        self.file_write = open(r"C:\Users\Administrator\Desktop\taobao_seed\tmall_618_look_seed.txt", "w", encoding="utf-8")

    def geren_address(self, i, shop_list):
        num = 0
        for shop_list in shop_list:
            sql = "select goods_id,seller_id from `tmall_goodsmobile_{}` where sales_month > 12 and seller_id in {}".format(i, shop_list)

            # 需要更换查询的库名：session_104  session_227_tm
            daima_res = self.session_227_tm.query_tuple_data(sql)
            for daima_tm in daima_res:
                num += 1
                data = list(daima_tm)
                self.file_write.write(",".join(data) + "\n")
                if num % 10000 == 0:
                    print(num)
                    self.file_write.flush()

    def insertion_data(self, i):
        insertion_sql = "insert into tmall_goodsmobile_{}_E_zj_all (update_date, goods_id, sales_vague, sales_month, comment_count, inventory, collect_num, address, cid, bid, bc_type, goods_name, seller_id, shop_id, advertising, discount_price, earnest, earnest_desc, price_name, price, ship_cost, assurance, promotion, promotion_desc, rewards, image_url, goods_info, E_daima) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)
        self.session_227_tm.insertion_data_list(insertion_sql, self.data_list)

    def taobao_all_address(self):
        sql = "select * from all_goodsinfo_daima"
        all_res = self.session_227_tm.query_tuple_data(sql)
        for address_data in all_res:
            cid = address_data[0]
            E_daima = address_data[1]
            self.addres_dict_all[cid] = E_daima

    def tmall_228_shop_id(self, i):
        sql = "SELECT seller_id FROM `tmall_shopinfo_{}` where province = '浙江省'".format(i)
        all_res = self.session_228.query_tuple_data(sql)
        shop_id_list = []
        for tuple_shopid in all_res:
            shopid = tuple_shopid[0]
            shop_id_list.append(shopid)
        tuple_shop_list = tuple(shop_id_list)
        return tuple_shop_list

    def run_spdier(self):
        self.taobao_all_address()
        for i in range(202205, 202206):
            num = 10000
            shop_list = self.tmall_228_shop_id(i)
            shop_id_list_list = [shop_list[i:i + num] for i in range(0, len(shop_list), num)]
            self.geren_address(i, shop_id_list_list)


def run_r():
    r = GerenAddress()
    r.run_spdier()


if __name__ == '__main__':
    run_r()



