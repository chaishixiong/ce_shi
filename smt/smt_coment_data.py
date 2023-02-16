import json
import re
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import kj_1_4_pool


def with_r():
    data_w = open(r'X:\数据库\速卖通\速卖通_拍照信息\{速卖通牌照信息_all}[店铺ID,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关].txt', 'a', encoding='utf-8')
    with open(r'X:\数据库\速卖通\速卖通_拍照信息\速卖通工商信息.csv', 'r', encoding='utf-8') as data_r:
        for data in data_r:
            data_re = re.search(r'""data""(.*?)""msg"":null}', data)
            if data_re:
                data_re = data_re.group(0)
                data_str = '{' + data_re.replace('""', '"')
                data_json = json.loads(data_str)
                data_data = data_json["data"]
                seller_id = str(data_data.get("aliMemberId"))
                company = if_data(data_data, "companyName")
                shui_id = if_data(data_data, "uniSocialCredit")
                yingye_id = if_data(data_data, "regNo")
                address = if_data(data_data, "regAddress")
                people = if_data(data_data, "entCorpName")
                scope = if_data(data_data, "entBusinessScope")
                shopCreatedAt = if_data(data_data, "establishTime")
                jiguan = if_data(data_data, "regAuthority")
                data_list = [seller_id, company, shui_id, yingye_id, address, people, scope, shopCreatedAt, jiguan]
                if seller_id == '254942100':
                    print()
                data_w.write(','.join(data_list) + '\n')
                print(data_list)


def if_data(data_data, str_d):
        data_dd = data_data.get(str_d)
        if data_dd == None:
            return ''
        else:
            return data_dd


def seller_id():
    seller_id_dict = {}
    session_227 = DataBaseSession(kj_1_4_pool)
    sql = "select seller_id, shop_id from `smt_shopinfo_202209`"

    # 需要更换查询的库名：session_104  session_227_tm
    daima_res = session_227.query_tuple_data(sql)
    for s_id in daima_res:
        seller_id_dict[s_id[0]] = s_id[1]
    data_w = open(r'X:\数据库\速卖通\company_data_new.txt', 'a', encoding='utf-8')
    with open(r'X:\数据库\速卖通\company_data.txt', 'r', encoding='utf-8') as s_r:
        for n_s in s_r:
            d_s_r = n_s.strip('\n').split(',')
            seller_id = d_s_r[0]
            shop_id = seller_id_dict.get(seller_id)
            if shop_id:
                d_s_r[0] = shop_id
                data_w.write(','.join(d_s_r) + '\n')
                data_w.flush()
        data_w.close()


if __name__ == '__main__':
    with_r()
    # seller_id()




