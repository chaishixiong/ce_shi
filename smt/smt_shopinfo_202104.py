from sql_pool.pymysql_pool import DataBaseSession
from sql_pool.dbpool import pool_smt


class SmtShopInfo(object):
    def __init__(self):
        self.session = DataBaseSession(pool_smt)
        self.addres_dict_all = {}
        self.data_list = []

    def geren_address(self, i):
        num = 0
        sql = "select * from smt_shopinfo_202105"
        geren_res = self.session.query_tuple_data(sql)
        for geren_adders in geren_res:
            num += 1
            data = list(geren_adders)
            shop_id = data[0]
            geren_add = self.addres_dict_all.get(shop_id)
            if geren_add != None:
                data.append(geren_add)
            else:
                g_a = '企业店'
                data.append(g_a)
            data_tuple = tuple(data)
            self.data_list.append(data_tuple)
            if num % 20000 == 0:
                # self.insertion_data(i)
                self.data_list = []
                print(num)
        if len(self.data_list) > 0:
            # self.insertion_data(i)
            self.data_list = []

    def insertion_data(self, i):
        insertion_sql = "insert into taobao_shopinfo_20200%s_geren (shop_id, seller_id, bc_type, main_sale, company, sales_count, sales_money, address, seller_name, seller_lv, shop_hpl, shop_name, weitao_id, shop_fans_num, open_shop_date, goods_num, new_goods_num, guanzhu_num, shop_money, shop_iocn, gold_shop, shop_type, taobao_shop_type2, taobao_shop_type3, open_time, phone, company_change, geren_address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % i
        self.session.insertion_data(insertion_sql, self.data_list)

    def smt_all_shop(self):
        sql = "select shop_id,seller_id from smt_shopinfo_202209"
        all_res = self.session.query_tuple_data(sql)
        for address_data in all_res:
            shop_id = address_data[0]
            address = address_data[1]
            self.addres_dict_all[shop_id] = address

    def run_spdier(self):
        self.smt_all_shop()
        for i in range(6, 10):
            self.geren_address(str(i))

    def with_shop(self):
        self.smt_all_shop()
        writ_data = open(r'D:\data\smt_shop_data.txt', 'w', encoding='utf-8')
        with open(r'D:\data\1_1_速卖通_店铺信息_new_合并.txt_去重.txt', 'r', encoding='utf-8') as read:
            for data in read:
                smt_data = data.strip('\n').split(',')
                shop_id = smt_data[0]
                d_b = self.addres_dict_all.get(shop_id)
                if d_b == None:
                    writ_data.write(data)
                    writ_data.flush()
            writ_data.close()

def run_smt():
    r = SmtShopInfo()
    r.with_shop()


if __name__ == '__main__':
    run_smt()



