from 数据查询sql.统计局需求.sql_pool.pymysql_pool import DataBaseSession


class GerenAddress(object):
    def __init__(self):
        self.session = DataBaseSession()
        self.addres_dict_all = {}
        self.data_list = []

    def geren_address(self):
        num = 0
        sql = "select * from tmall_goodsmobile_202110"
        daima_res = self.session.query_tuple_data(sql)
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
            if num % 10000 == 0:
                self.insertion_data()
                self.data_list = []
                print(num)
        if len(self.data_list) > 0:
            self.insertion_data()

    def insertion_data(self):
        insertion_sql = "insert into tmall_goodsmobile_202110_E (update_date, goods_id, sales_vague, sales_month, comment_count, inventory, collect_num, address, cid, bid, bc_type, goods_name, seller_id, shop_id, advertising, discount_price, earnest, earnest_desc, price_name, price, ship_cost, assurance, promotion, promotion_desc, rewards, image_url, goods_info, E_daima) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.session.insertion_data(insertion_sql, self.data_list)

    def taobao_all_address(self):
        sql = "select * from all_goodsinfo_daima"
        all_res = self.session.query_tuple_data(sql)
        for address_data in all_res:
            cid = address_data[0]
            E_daima = address_data[1]
            self.addres_dict_all[cid] = E_daima

    def run_spdier(self):
        self.taobao_all_address()
        self.geren_address()


def run_r():
    r = GerenAddress()
    r.run_spdier()


if __name__ == '__main__':
    run_r()

