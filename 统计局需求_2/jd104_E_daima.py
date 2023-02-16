from 数据查询sql.统计局需求.sql_pool.pymysql_pool import DataBaseSession
from 数据查询sql.统计局需求.sql_pool.dbpool import jd_104_pool


class GerenAddress(object):
    def __init__(self):
        self.session = DataBaseSession(jd_104_pool)
        self.addres_dict_all = {}
        self.data_list = []

    def geren_address(self, i):
        num = 0
        # sql = "select * from jd_goodsinfo_20210{} limit 10000".format(i)
        sql = "select * from jd_goodsinfo_20210{}".format(i)
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
            if num % 30000 == 0:
                self.insertion_data(i)
                self.data_list = []
                print(num)
        if len(self.data_list) > 0:
            pass
            self.insertion_data(i)
            self.data_list = []



    def insertion_data(self, i):
        # 202001-202012-202102
        insertion_sql = "insert into jd_goodsinfo_20210{}_E (shop_id, VID, PID, mian_goods_id, goods_id, bid, brand_name, CID1, CID2, CID3, c_name1, c_name2, c_name3, is_ebook, price, comment, realcomment, goods_name, data_month, E_daima) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)


    def taobao_all_address(self):
        sql = "select * from all_jd_goodsinfo_daima"
        all_res = self.session.query_tuple_data(sql)
        for address_data in all_res:
            cid = address_data[0]
            E_daima = address_data[1]
            self.addres_dict_all[cid] = E_daima

    def run_spdier(self):
        self.taobao_all_address()
        # for i in range(202101, 202113):
        for i in range(4, 5):
            self.geren_address(i)


def run_r():
    r = GerenAddress()
    r.run_spdier()


if __name__ == '__main__':
    run_r()


