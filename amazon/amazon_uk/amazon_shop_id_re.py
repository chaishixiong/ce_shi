import re
from 统计局需求_2.sql_pool.dbpool import kj_1_4_pool
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession


def shop_id():
    re_shopid = open(r'W:\scrapy_seed\amazon_uk_shopinfo_new.txt', 'w', encoding='utf-8')
    shopid_old_id = set()
    with open(r'W:\scrapy_seed\amazon_uk_shopinfo.txt', 'r', encoding='utf-8') as shopid_old:
        for i in shopid_old:
            if '&' in i:
                shop_id_old = re.search(r'(.*?)&|(.*?)\\&', i).group(1).strip('\\')
                shopid_old_id.add(shop_id_old)
    with open(r'X:\数据库\欧洲亚马逊\欧亚店铺id.txt', 'r', encoding='utf-8') as shopid:
        for id in shopid:
            if '&' in id:
                shop_id = re.search(r'(.*?)&|(.*?)\\&', id).group(1).strip('\\')
                if shop_id not in shopid_old_id:
                    re_shopid.write(shop_id + '\n')
            else:
                re_shopid.write(id)
            re_shopid.flush()
        re_shopid.close()


def goods_id():
    goodsid = set()
    registration_mysql = DataBaseSession(kj_1_4_pool)
    sql = 'select goods_id from amazonuk_goodsinfo_202212'
    data = registration_mysql.query_tuple_data(sql)
    for i in data:
        g_id = i[0]
        goodsid.add(g_id)

    re_shopid = open(r'W:\scrapy_seed\amazon_uk_sort_shop.txt', 'w', encoding='utf-8')
    with open(r'X:\数据库\欧洲亚马逊\goods_id\amazon_uk_goodsid_1_合并.txt', 'r', encoding='utf-8') as shopid_old:
        for shopidold in shopid_old:
            aa = shopidold.strip('\n')
            goodsid.add(aa)
    with open(r'X:\数据库\欧洲亚马逊\goods_id\amazon_uk_goodsid_2_合并.txt', 'r', encoding='utf-8') as shopid:
        for id in shopid:
            goods_i = id.strip()
            if goods_i not in goodsid:
                re_shopid.write(id)
            re_shopid.flush()
        re_shopid.close()


if __name__ == '__main__':
    shop_id()










