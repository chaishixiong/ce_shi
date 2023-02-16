from 数据查询sql.统计局需求.sql_pool.pymysql_pool import DataBaseSession
from 数据查询sql.统计局需求.sql_pool.dbpool import oridata_pool


class CompanyUpdata(object):
    def __init__(self):
        self.company_oridata227 = DataBaseSession(oridata_pool)
        self.company_dict_all = {}
        self.data_list = []

    def company_address(self):
        num = 0
        sql = "select * from `company_qichacha_202209` limit 1000"
        # 需要更换查询的库名：session_104  session_227_tm
        daima_res = self.company_oridata227.query_tuple_data(sql)
        for daima_tm in daima_res:
            num += 1
            data = list(daima_tm)
            company_name = data[0]
            daima_add = self.company_dict_all.get(company_name)
            if daima_add == None:
                data_tuple = tuple(daima_add)
                self.data_list.append(data_tuple)
            else:
                with open(r'company_name.txt', 'w', encoding='utf-8') as f:
                    f.write(company_name + '\n')
                    f.flush()
                    f.close()
            if num % 10 == 0:
                self.insertion_data()
                self.data_list = []
                print(num)
        if len(self.data_list) > 0:
            self.insertion_data()
            self.data_list = []

    def insertion_data(self):
        insertion_sql = "insert into company_ad_2022030 (company, company_address, lat, lng, country, province, city, county, township, street, direction, distance, streetNumber, adcode, citycode, towncode, formatted_address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.company_oridata227.insertion_data_list(insertion_sql, self.data_list)

    def company_all_address(self):
        sql = "select * from company_ad_20220831"
        all_res = self.company_oridata227.query_tuple_data(sql)
        for address_data in all_res:
            self.company_dict_all[address_data[0]] = address_data

    def company_228_shop_id(self, i):
        sql = "SELECT seller_id FROM `tmall_shopinfo_{}` where province = '安徽省'".format(i)
        all_res = self.company_oridata227.query_tuple_data(sql)
        shop_id_list = []
        for tuple_shopid in all_res:
            shopid = tuple_shopid[0]
            shop_id_list.append(shopid)
        tuple_shop_list = tuple(shop_id_list)
        return tuple_shop_list

    def run_spdier(self):
        # self.company_all_address()
        self.company_address()


def run_r():
    r = CompanyUpdata()
    r.run_spdier()


if __name__ == '__main__':
    run_r()



