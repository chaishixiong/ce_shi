from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import oridata_pool


class CompanyUpdata(object):
    def __init__(self):
        self.company_oridata227 = DataBaseSession(oridata_pool)
        self.company_dict_all = {}
        self.data_list = []

    def company_address(self):
        num = 0
        sql = "select * from `company_qichacha_202209_add`"
        # 需要更换查询的库名：session_104  session_227_tm
        daima_res = self.company_oridata227.query_tuple_data(sql)
        for daima_tm in daima_res:
            num += 1
            data = list(daima_tm)
            company_name = data[0]
            daima_add = self.company_dict_all.get(company_name)
            if daima_add != None:
                data_tuple = tuple(daima_add)
                self.data_list.append(data_tuple)
            else:
                with open(r'company_name_not.txt', 'a', encoding='utf-8') as f:
                    f.write(company_name + '\n')
                    f.flush()
                    f.close()
            if num % 10000 == 0:
                self.insertion_data()
                self.data_list = []
                print(num)
        if len(self.data_list) > 0:
            self.insertion_data()
            self.data_list = []

    def insertion_data(self):
        insertion_sql = "insert into company_ad_20220930_add (company, company_address, lat, lng, country, province, city, county, township, street, direction, distance, streetNumber, adcode, citycode, towncode, formatted_address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.company_oridata227.insertion_data_list(insertion_sql, self.data_list)

    def company_all_address(self):
        sql = "select * from company_ad_20220831_add"
        all_res = self.company_oridata227.query_tuple_data(sql)
        for address_data in all_res:
            self.company_dict_all[address_data[0]] = address_data

    def run_spdier(self):
        self.company_all_address()
        self.company_address()


def run_r():
    r = CompanyUpdata()
    r.run_spdier()


if __name__ == '__main__':
    run_r()



