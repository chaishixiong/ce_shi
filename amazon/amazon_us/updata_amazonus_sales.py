from 统计局需求_2.sql_pool.dbpool import kj_1_4_pool
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from collections import defaultdict


kj_227_mysql = DataBaseSession(kuajing_227_pool)
kj_1_4_mysql = DataBaseSession(kj_1_4_pool)


def shop_danjia(month):
    last_month = month - 1
    sql_227 = "SELECT shop_id,average_price FROM `amazonus_shopinfo_{}_sales_new` WHERE `average_price` <> '' AND `average_price` > '0'".format('202101')
    danjia_list = kj_227_mysql.query_tuple_data(sql_227)
    write_file = open("X:\数据库\美国亚马逊\店铺单价\{{3_2店铺单价_{}}}[id,price_avg].txt".format(month), "w", encoding="utf-8")
    amazon_id = set()
    for average_price in danjia_list:
        shop_id = average_price[0]
        average_p = average_price[1]
        price_avg = float(average_p) + 8
        amazon_id.add(shop_id)
        write_file.write("{},{}\n".format(shop_id, str(price_avg)))
    with open(r"X:\数据库\美国亚马逊\店铺单价\{{3_2店铺单价_{}}}[id,price_avg].txt".format(last_month), "r", encoding="utf-8") as f:
        for i in f:
            data = i.strip().split(",")
            if data[0] not in amazon_id:
                data[1] = str(float(data[1]) + 8)
                write_file.write(i)
                amazon_id.add(data[0])


def shop_process(month):
    # month = '202101'
    # shop_file = open(
    #     r"X:\数据库\美国亚马逊\{{amazonus_shopinfo_{}}}[KEY,店铺名称,店铺介绍,公司,公司地址信息,国家,邮编,公司原始信息,30天好评率,30天中评率,30天差评率,30天评论数,90天好评率,90天中评率,90天差评率,90天评论数,12月好评率,12月中评率,12月差评率,12月评论数,累积好评率,累积中评率,累积差评率,累积评论数,省,市,区,main_sales,店铺单价].txt".format(
    #         month), "w", encoding="utf-8")
    price_dict = {}
    with open(r"X:\数据库\美国亚马逊\店铺单价\{{3_2店铺单价_{}}}[id,price_avg].txt".format(month), "r", encoding="utf-8") as f:
        for i in f:
            data = i.strip().split(",")
            price_dict[data[0]] = (data[1])

    sql_1 = '''select a.main_sales,a.totol_money/b.totle_num from
            (select main_sales,sum(comment_total*average_price) as totol_money from amazonus_shopinfo_{}
            GROUP BY main_sales) as a
            join
            (select main_sales,sum(comment_total) as totle_num  from amazonus_shopinfo_{}
            where average_price != ""
            GROUP BY main_sales) as b 
            on a.main_sales = b.main_sales'''.format(month, month)
    data_1 = kj_227_mysql.query_tuple_data(sql_1)
    price_dict_cname = {}
    for i in data_1:
        key = i[0]
        if not key:
            key = "other"
            price_dict_cname[key] = i[1] + 8
        # 拿月度和年度评论比例
    # sql_year = '''select sum(comment_year)/sum(comment_mouth) from amazonus_shopinfo_{}'''.format(month)
    sql_year = '''select sum(comment_year)/sum(comment_month) from amazonus_shopinfo_{}'''.format(month)
    data_year = kj_227_mysql.query_tuple_data(sql_year)
    year_bili = data_year[0][0]
        # 拿销评比
    bili_dict = {}
    with open(r"X:\数据库\美国亚马逊\us_seed\销量评论比.txt", "r", encoding="utf-8") as f:
        for i in f:
            data_i = i.strip().split(",")
            bili_dict[data_i[0]] = (data_i[1], data_i[2])

    sql_227 = 'select * from amazonus_shopinfo_{}_sales'.format(month)
    shop_data_list = kj_1_4_mysql.query_tuple_data(sql_227)
    list_shop_data = []
    num = 0
    for shop_list in shop_data_list:
        num += 1
        amazon_data = list(shop_list)
        key = amazon_data[0]
        price = price_dict.get(key, "")
        amazon_data[-5] = price
        # shop_file.write(",".join(amazon_data) + "\n")
        if len(amazon_data) >= 29:
            comment_month = amazon_data[11]  # 月评论数
            comment_year = amazon_data[19]  # 年评论数
            comment_totle = amazon_data[23]  # 累积评论数
            main_sales = amazon_data[27]  # main_sales
            average_price = amazon_data[28]  # 店铺单价
            sales_money = ""
            sales_year = ""
            sales_money_year = ""
            if comment_totle:
                if not main_sales:
                    main_sales = "other"
                if not average_price:
                    average_price = price_dict_cname.get(main_sales)
                    if not average_price:
                        average_price = price_dict_cname.get("other")
                if "锛?" in comment_month or "锛?" in comment_totle or "锛?" in comment_year:
                    comment_month = comment_month.replace("锛?", "0")
                    comment_totle = comment_totle.replace("锛?", "0")
                    comment_year = comment_year.replace("锛?", "0")
                sales = int((int(comment_totle) * float(bili_dict.get(main_sales)[0]) + int(
                    comment_month) * float(bili_dict.get(main_sales)[1])) / 2)
                sales_money = sales * float(average_price)
                sales_year = int((int(comment_totle) * float(bili_dict.get(main_sales)[0]) + int(
                    comment_year) / year_bili * float(bili_dict.get(main_sales)[1])) / 2 * year_bili)
                sales_money_year = sales_year * float(average_price)
                if sales > sales_year:
                    print(shop_list)
            amazon_data[-3] = sales_money
            amazon_data[-2] = sales_year
            amazon_data[-1] = sales_money_year
            list_shop_data.append(amazon_data)
            if num % 10000 == 0:
                insertion_data(month, list_shop_data)
                list_shop_data = []
                print(num)
    if len(list_shop_data) > 0:
        print(num)
        insertion_data(month, list_shop_data)


def insertion_data(i, data_list):
    # 无farm_flag字段：2021-1-3   20201-10
    insertion_sql = "insert into amazonus_shopinfo_{}_sales_new (shop_id, shop_name, shop_info, company, company_address, country, postcode, html, goodrate_month, middlerate_month, badrate_month, comment_month, goodrate_quarterly, middlerate_quarterly, badrate_quarterly, comment_quarterly, goodrate_year, middlerate_year, badrate_year, comment_year, goodrate_total, middlerate_total, badrate_total, comment_total, province, city, county, main_sales, average_price, sales, sales_money, sales_y, sales_money_y) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(
        i)

    # 有farm_flag字段：2020-11-12
    # insertion_sql = "insert into taobao_goodsmobile_20210{}_E_zj (update_date, goods_id, sales_month, sales_month1, comment_count, inventory, collect_num, address, cid, bid, bc_type, goods_name, seller_id, shop_id, advertising, discount_price, earnest, earnest_desc, price_name, price, ship_cost, assurance, promotion, promotion_desc, rewards, image_url, goods_info,farm_flag, E_daima) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(i)

    # 插入库名： session_227_tb
    kj_1_4_mysql.insertion_data_list(insertion_sql, data_list)


if __name__ == '__main__':
    for n in range(202202, 202210):
        print('amazonus_shopinfo_{}_sales_new'.format(n))
    # n = 202102
        shop_danjia(n)
        shop_process(n)




