import pandas as pd
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import tb_pool


class TaoBaoAddress(object):
    def __init__(self):
        self.session = DataBaseSession(tb_pool)
        self.address_dict_all = {}
        self.one_address = ''
        self.address_list_list = []

    def for_sql_data(self, num, data_list):
        yue_nym = 0
        for data in data_list:
            yue_nym += 1
            if len(data[1]) == 0 and len(data[2]) > 0:
                shop_id = data[0]
                address = data[2]
                address_list = self.address_dict_all.get(shop_id) if self.address_dict_all.get(shop_id) != None else []
                address_list.append(address)
                self.address_dict_all[shop_id] = address_list
            if yue_nym % 1000000 == 0:
                    print(num, yue_nym)

    def for_address_dict_all(self, shop_id, addres_ll):
        if len(addres_ll) == 0:
            return None
        data_l = pd.value_counts(addres_ll)
        num_list = data_l.values
        addres_list = data_l.keys()
        number = 0
        for addres, num in zip(addres_list, num_list):
            if len(addres_ll) <= 3:
                param = (shop_id, addres)
                return param
            elif num > 3:
                param = (shop_id, addres)
                return param
            elif num == 3 and len(addres_ll) > 3:
                number += num
                self.one_address = addres
                if number == 6:
                    param = (shop_id, addres)
                    return param
            elif num == 2:
                number += num
                if number == 6:
                    param = (shop_id, addres)
                    return param
                elif number == 5:
                    param = (shop_id, addres)
                    return param
                elif number == 4:
                    param = (shop_id, addres)
                    return param
            else:
                param = (shop_id, addres)
                return param

    def insertion_data(self):
        print(len(self.address_list_list))
        for i in range(0, len(self.address_list_list), 100):
            aa = self.address_list_list[i:i + 100]
            insertion_sql = "insert into taobao_address_all_2022 (shop_id, address) VALUES (%s,%s)"
            self.session.insertion_data(insertion_sql, aa)

    def query_data(self, query_sql):
        res = self.session.query_tuple_data(query_sql)
        return res

    def run_spider(self):
        aa_num = 0
        num_list = [202111, 202112, 202201, 202202, 202203]
        for num in num_list:
            sql = "select shop_id,company,address from taobao_shopinfo_{}".format(num)
            res = self.session.query_tuple_data(sql)
            self.for_sql_data(num, res)
        for shop_id, addres_ll in zip(self.address_dict_all.keys(), self.address_dict_all.values()):
            aa_num += 1
            if aa_num % 100000 == 0:
                print(aa_num)
            param = self.for_address_dict_all(shop_id, addres_ll)
            if param != None:
                self.address_list_list.append(param)
        self.insertion_data()


def run_run():
    r = TaoBaoAddress()
    r.run_spider()


if __name__ == '__main__':
    run_run()
    import numpy

    # 7是分成几个小的列表
    # hum_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 5, 21, 32, 45]
    # for i in range(0, len(hum_list), 4):
    #     aa = hum_list[i:i + 4]
    #     print(aa)
    # l = [i for i in range(15)]
    # n = 3  # 大列表中几个数据组成一个小列表
    # print([l[i:i + n] for i in range(0, len(l), n)])
    # l = [i for i in range(10002)]
    # n = 1000
    # print([l[i:i + n] for i in range(0, len(l), n)])
    # for i in range(0, len(l), n):
    #     print(l[i:i + n])







