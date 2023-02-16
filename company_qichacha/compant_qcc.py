from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import company_pool


class GerenAddress(object):
    def __init__(self):
        self.session_227 = DataBaseSession(company_pool)
        self.addres_dict_all = {}
        self.data_list = []

    def geren_address(self, i, shop_list):
        num = 0
        sql = "select * from `tmall_goodsmobile_{}` where seller_id in {}".format(i, shop_list)

        # 需要更换查询的库名：session_104  session_227_tm
        daima_res = self.session_227.query_tuple_data(sql)
        for daima_tm in daima_res:
            num += 1
            data = list(daima_tm)
            # sales_vague = data[2]
            # data.insert(2, sales_vague)
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
                self.data_list = []
                print(num)
        if len(self.data_list) > 0:
            self.data_list = []

    def insertion_data(self):
        insertion_sql = "insert into company_qichacha_202210 (company, 经营状况, 法定代表人, 注册资本, 成立日期, 核准日期, 所属省份, 所属城市, 所属区县, 电话, 更多电话, 邮箱, 更多邮箱, 统一社会信用代码, 纳税人识别号, 注册号, 组织机构代码, 参保人数, 企业类型, 所属行业, 曾用名, 英文名, 网址,company_address, 最新年报, 经营范围) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.session_227.insertion_data_list(insertion_sql, self.data_list)

    def taobao_all_address(self):
        sql = "select * from company_qichacha_202210"
        all_res = self.session_227.query_tuple_data(sql)
        for address_data in all_res:
            cid = address_data[0]
            self.addres_dict_all[cid] = address_data

    def tmall_228_shop_id(self):
        sql = "select * from company_qichacha_202210_last limit 1000"
        all_res = self.session_227.query_tuple_data(sql)
        num = 0
        for tuple_shopid in all_res:
            num += 1
            company = tuple_shopid[0]
            data = self.addres_dict_all.get(company)
            if data == None:
                with open('company_qichacha.txt', 'a', encoding='utf-8') as f:
                    f.write(company + '\n')
            else:
                self.data_list.append(data)
                if num % 10000 == 0:
                    self.insertion_data()
                    print(num)
                    self.data_list = []
        if len(self.data_list) > 0:
            print(num)
            self.insertion_data()
            self.data_list = []

    def run_spdier(self):
        self.taobao_all_address()
        self.tmall_228_shop_id()


def run_r():
    r = GerenAddress()
    r.run_spdier()


if __name__ == '__main__':
    run_r()



