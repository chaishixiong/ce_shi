import pymysql
import json


def open_sql(sql, database_name):
    # 连接database
    conn = pymysql.connect(host="192.168.0.227", user="update", password="change227NRIAT!#$",
                           database="{}".format(database_name), port=9227, use_unicode=True, charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    # 定义要执行的SQL语句
    # 执行SQL语句
    cursor.execute(sql)
    # 关闭光标对象
    data = cursor.fetchall()
    cursor.close()
    # 关闭数据库连接
    conn.close()
    return data


def fund(listTemp, n):
    # 列表等分切割
    resules = []
    for i in range(0, len(listTemp), n):
        temp = listTemp[i:i + n]
        resules.append(temp)
    print(len(listTemp))
    return resules


def goods_seller_id():
    database_tm_name = 'oridata_tmall'
    database_tb_name = 'oridata_taobao'
    sql = "SELECT seller_id from taobao_goodsmobile_202108 WHERE shop_id = '' group by seller_id"
    seller_list = open_sql(sql, database_tm_name)
    num = 10000
    seller_id_list = fund(seller_list, num)
    for seller_id in seller_id_list:
        id_list = []
        for id in seller_id:
            id_list.append(id[0])
        sql_seller = '''SELECT shop_id,seller_id from(
                                    SELECT shop_id,seller_id from taobao_shopinfo_202012 WHERE seller_id in {}
                                    union
                                    SELECT shop_id,seller_id from taobao_shopinfo_202011 WHERE seller_id in {}
                                    union
                                    SELECT shop_id,seller_id from taobao_shopinfo_202010 WHERE seller_id in {}
                                    union
                                    SELECT shop_id,seller_id from taobao_shopinfo_202009 WHERE seller_id in {}
                                    union
                                    SELECT shop_id,seller_id from taobao_shopinfo_202008 WHERE seller_id in {}
                                    union
                                    SELECT shop_id,seller_id from taobao_shopinfo_202007 WHERE seller_id in {}
                                    union
                                    SELECT shop_id,seller_id from taobao_shopinfo_202106 WHERE seller_id in {}
                                    union
                                    SELECT shop_id,seller_id from taobao_shopinfo_202105 WHERE seller_id in {}
                                    union
                                    SELECT shop_id,seller_id from taobao_shopinfo_202104 WHERE seller_id in {}
                                    union
                                    SELECT shop_id,seller_id from taobao_shopinfo_202103 WHERE seller_id in {}
                                    union
                                    SELECT shop_id,seller_id from taobao_shopinfo_202102 WHERE seller_id in {}
                                    union
                                    SELECT shop_id,seller_id from taobao_shopinfo_202101 WHERE seller_id in {}
                                    )
                                    as a GROUP BY seller_id'''.format(tuple(id_list), tuple(id_list),
                                                                      tuple(id_list), tuple(id_list),
                                                                      tuple(id_list), tuple(id_list),
                                                                      tuple(id_list), tuple(id_list),
                                                                      tuple(id_list), tuple(id_list),
                                                                      tuple(id_list), tuple(id_list),
                                                                      tuple(id_list))
        # sql_seller = '''SELECT shop_id,seller_id from(
        #                                     SELECT shop_id,seller_id from tmall_shopinfo_202012 WHERE seller_id in {}
        #                                     union
        #                                     SELECT shop_id,seller_id from tmall_shopinfo_202011 WHERE seller_id in {}
        #                                     union
        #                                     SELECT shop_id,seller_id from tmall_shopinfo_202010 WHERE seller_id in {}
        #                                     union
        #                                     SELECT shop_id,seller_id from tmall_shopinfo_202009 WHERE seller_id in {}
        #                                     union
        #                                     SELECT shop_id,seller_id from tmall_shopinfo_202008 WHERE seller_id in {}
        #                                     union
        #                                     SELECT shop_id,seller_id from tmall_shopinfo_202007 WHERE seller_id in {}
        #                                     union
        #                                     SELECT shop_id,seller_id from tmall_shopinfo_202106 WHERE seller_id in {}
        #                                     union
        #                                     SELECT shop_id,seller_id from tmall_shopinfo_202105 WHERE seller_id in {}
        #                                     union
        #                                     SELECT shop_id,seller_id from tmall_shopinfo_202104 WHERE seller_id in {}
        #                                     union
        #                                     SELECT shop_id,seller_id from tmall_shopinfo_202103 WHERE seller_id in {}
        #                                     union
        #                                     SELECT shop_id,seller_id from tmall_shopinfo_202102 WHERE seller_id in {}
        #                                     union
        #                                     SELECT shop_id,seller_id from tmall_shopinfo_202101 WHERE seller_id in {}
        #                                     )
        #                                     as a GROUP BY seller_id'''.format(tuple(id_list), tuple(id_list),
        #                                                                       tuple(id_list), tuple(id_list),
        #                                                                       tuple(id_list), tuple(id_list),
        #                                                                       tuple(id_list), tuple(id_list),
        #                                                                       tuple(id_list), tuple(id_list),
        #                                                                       tuple(id_list), tuple(id_list),
        #                                                                       tuple(id_list))
        shop_id_data = open_sql(sql_seller, database_tb_name)
        print(id_list)
        with open('tb_shop_id.txt', 'a', encoding='utf-8')as f:
            for shop_id in shop_id_data:
                f.write(",".join(shop_id) + "\n")


if __name__ == '__main__':
    goods_seller_id()



