from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import shop_228_pool


class TmallShop(object):
    def __init__(self):
        self.session_228_jd = DataBaseSession(shop_228_pool)
        self.insertion_data_list = []
        self.p_c_c = dict()
        self.hangzhou_data = dict()

    def query_sql_data(self, i):
        jd_cp_sql = 'SELECT shop_id,company,company_address,province,city,county FROM `tmall_shopinfo_{}_cp`'.format(i)
        jd_cp_data = self.session_228_jd.query_tuple_data(jd_cp_sql)
        jd_hangzhou_sql = 'SELECT * FROM `tmall_shopinfo_{}_hangzhou`'.format(i)
        jd_hangzhou_sql = self.session_228_jd.query_tuple_data(jd_hangzhou_sql)
        return jd_cp_data, jd_hangzhou_sql

    def insertion_sql_data(self, i):
        insertion_sql = "insert into tmall_shopinfo_{} (shop_id,seller_id,bc_type,main_sale,company,sales_count,sales_money,address,seller_name,seller_lv,shop_hpl,shop_name,weitao_id,shop_fans_num,open_shop_date,goods_num,new_goods_num,guanzhu_num,shop_money,shop_iocn,gold_shop,shop_type,shop_url,tmall_province,tmall_city,phone_ext,tmall_shop_type2,shop_age,tmall_shop_type3,ww_jm,xid,company_address,province,city,county,street,last_sales_money,vix,xinyong,describe_rate,service_rate,logistics_rate,main_sale_count,main_sale_all,main_sale_top5,township) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)
        self.session_228_jd.insertion_data(insertion_sql, self.insertion_data_list)

    def data_updata(self, i, p_c_c_list, hangzhou_data_list):
        num = 0
        for p_c_c in p_c_c_list:
            if None not in p_c_c:
                p_c_c_l = list(p_c_c)
                p_shop_id = p_c_c_l[0]
                p_shop_data = p_c_c_l
                self.p_c_c[p_shop_id] = p_shop_data
        for hangzhou_data in hangzhou_data_list:
            num += 1
            hangzhou_data_l = list(hangzhou_data)
            h_z_shop_id = hangzhou_data_l[0]
            p_c_c_data = self.p_c_c.get(h_z_shop_id)
            if p_c_c_data != None:
                hangzhou_data_l[4] = p_c_c_data[1]
                hangzhou_data_l[31] = p_c_c_data[2]
                hangzhou_data_l[32] = p_c_c_data[3]
                hangzhou_data_l[33] = p_c_c_data[4]
                hangzhou_data_l[34] = p_c_c_data[5]
            hangzhou_tuple = tuple(hangzhou_data_l)
            self.insertion_data_list.append(hangzhou_tuple)
            if num % 10000 == 0:
                self.insertion_sql_data(i)
                self.insertion_data_list = []
                print(num)
        if len(self.insertion_data_list) > 0:
            print(num)
            self.insertion_sql_data(i)
            self.insertion_data_list = []

    def run_spider(self):
        for i in range(202104, 202109):
            p_c_c_list, hangzhou_data_list = self.query_sql_data(i)
            self.data_updata(i, p_c_c_list, hangzhou_data_list)


def run_tmall_spider():
    run = TmallShop()
    run.run_spider()


if __name__ == '__main__':
    run_tmall_spider()






