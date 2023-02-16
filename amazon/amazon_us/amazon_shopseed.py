from 统计局需求_2.sql_pool.dbpool import kj_1_4_pool
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession

def quchong_amazon_sortshop():
    session_kuajin = DataBaseSession(kj_1_4_pool)
    query_sql = "select shop_id from amazonus_shopinfo_202211_sales_new"
    amazon_shop_id = session_kuajin.query_tuple_data(query_sql)
    seed_data_dict = set()
    for amazon_shop in amazon_shop_id:
        amazon_shopid = amazon_shop[0]
        seed_data_dict.add(amazon_shopid)
    new_shop_w = open(r'X:\数据库\美国亚马逊\amazon_shopgoods_seed_2.txt', 'w', encoding='utf-8')

    with open(r'X:\数据库\美国亚马逊\us_seed\amazon_new_shopid\amazon_shopid_20221226.txt', 'r', encoding='utf-8') as new_r:
        for seed_data_1 in new_r:
            seed_list_1 = seed_data_1.strip('\n')
            if seed_list_1 not in seed_data_dict:
                new_shop_w.write(seed_data_1)
                new_shop_w.flush()
        new_shop_w.close()



def shop_data_amazon_sortshop():
    new_shop_w = open(r'X:\数据库\美国亚马逊\{amazonus_shopinfo_202212}[KEY,店铺名称,店铺介绍,公司,公司地址信息,国家,邮编,公司原始信息,30天好评率,30天中评率,30天差评率,30天评论数,90天好评率,90天中评率,90天差评率,90天评论数,12月好评率,12月中评率,12月差评率,12月评论数,累积好评率,累积中评率,累积差评率,累积评论数,省,市,区,main_sales,店铺单价].txt', 'a', encoding='utf-8')
    shop_dict = dict()
    with open(r'X:\数据库\美国亚马逊\{amazonus_shopinfo_202212}[KEY,店铺名称,店铺介绍,公司,公司地址信息,国家,邮编,公司原始信息,30天好评率,30天中评率,30天差评率,30天评论数,90天好评率,90天中评率,90天差评率,90天评论数,12月好评率,12月中评率,12月差评率,12月评论数,累积好评率,累积中评率,累积差评率,累积评论数,省,市,区,main_sales,店铺单价]_old.txt', 'r', encoding='utf-8') as new_r:
        for seed_data_1 in new_r:
            seed_list_1 = seed_data_1.strip('\n').split(',')
            shop_dict[seed_list_1[0]] = seed_data_1
            new_shop_w.write(seed_data_1)
            new_shop_w.flush()
    with open(r'X:\数据库\美国亚马逊\202211\amazonus_shopinfo_202211_new.txt', 'r', encoding='utf-8') as new_r_old:
        for seed_data_1_old in new_r_old:
            seed_list_1_old = seed_data_1_old.strip('\n').split(',')
            shop_id = seed_list_1_old[0]
            shop_data = shop_dict.get(shop_id)
            if shop_data == None:
                new_shop_w.write(seed_data_1_old)
                new_shop_w.flush()
        new_shop_w.close()


def quchong_amazon_sortshop_2():
    '''
    排查未采集的店铺ID重新作为种子采集
    :return:
    '''
    new_shop_w = open(r'W:\scrapy_seed\amazon_shopinfo.txt', 'w', encoding='utf-8')
    seed_data_dict = set()
    with open(r'W:\scrapy_xc\amazon_shopinfo-data_合并.txt', 'r', encoding='utf-8') as new_r:
        for seed_data_1 in new_r:
            id = seed_data_1.strip().split(',')
            shop_id = id[0]
            seed_data_dict.add(shop_id)
    session_kuajin = DataBaseSession(kj_1_4_pool)
    query_sql = "SELECT shop_id FROM `amazonus_shopinfo_202212_sales`"
    amazon_shop_id = session_kuajin.query_tuple_data(query_sql)

    for amazon_shop in amazon_shop_id:
        amazon_shopid = amazon_shop[0]
        if amazon_shopid not in seed_data_dict:
            new_shop_w.write(amazon_shopid + '\n')
            new_shop_w.flush()
    new_shop_w.close()


if __name__ == '__main__':
    # with_r()
    quchong_amazon_sortshop_2()


