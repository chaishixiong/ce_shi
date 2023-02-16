from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import tb_pool, tb_228_pool


class TBCompanyUpdata(object):
    def __init__(self):
        self.company_227 = DataBaseSession(tb_pool)
        self.company_228 = DataBaseSession(tb_228_pool)
        self.company_dict_all = {}
        self.data_list = []

    def tbcompany_address(self):
        num = 0
        sql = "SELECT shop_id,seller_id FROM `taobao_shopinfo_202109` WHERE `sales_money` > '0' and province = '浙江'"
        # 需要更换查询的库名：session_104  session_227_tm
        daima_res = self.company_228.query_tuple_data(sql)
        for daima_tm in daima_res:
            num += 1
            data = list(daima_tm)
            company_name = data[0]
            daima_add = self.company_dict_all.get(company_name)
            if daima_add == None:
                with open(r'company_name_not.txt', 'a', encoding='utf-8') as f:
                    f.write(company_name + '\n')
                    f.flush()
                    f.close()
            if num % 10000 == 0:
                # self.updata_data()
                self.data_list = []
                print(num)
        if len(self.data_list) > 0:
            # self.updata_data()
            self.data_list = []

    def updata_data(self, shop_id, company):
        updata_data_sql = "UPDATE taobao_shopinfo_202209 SET company = '{}' WHERE shop_id = '{}'".format(company, shop_id)
        self.company_227.updata_data(updata_data_sql)

    def tbcompany_all_address(self):
        sql = "SELECT shop_id,seller_id FROM `taobao_shopinfo_202209` WHERE `sales_money` > '0' and province = '浙江'"
        all_res = self.company_228.query_tuple_data(sql)
        for address_data in all_res:
            self.company_dict_all[address_data[0]] = address_data[1]

    def tbcom_withopen(self):
        with open(r'qiye_id_nema.txt', 'r', encoding='utf-8') as wr:
            for w in wr:
                str_w = w.strip('\n')
                w_list = str_w.split('\t')
                shop_id = w_list[0]
                company = w_list[1]
                seller_id = self.company_dict_all.get(shop_id)
                if seller_id != None:
                    self.updata_data(shop_id, company)

    def run_spdier(self):
        self.tbcompany_all_address()
        self.tbcompany_address()


def run_r():
    r = TBCompanyUpdata()
    r.run_spdier()


if __name__ == '__main__':
    run_r()



