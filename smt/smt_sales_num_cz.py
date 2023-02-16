from 统计局需求_2.sql_pool.dbpool import kj_1_4_pool
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from collections import defaultdict


def smt_sales_num_cz():
    '''
    速卖通销销售额计算方法
    '''
    sales_num_data_202207 = defaultdict(lambda: [[], []])
    sales_money_dict = dict()
    comment_dict = dict()
    # session_kuajin = DataBaseSession(kuajing_227_pool)
    # query_sql = "select seller_id, good_id, sales_num, minPrice from smt_goodsinfo_202208  WHERE `sales_num` <> '' and `minPrice` <> ''"
    # smt_sales_num_7 = session_kuajin.query_tuple_data(query_sql)
    sales_num_cz = open(r'X:\数据库\速卖通\{3_1_1_字典_速卖通_月统计}[店铺id,sum(销量 米 商品价格_较高值),sum(销量)].txt', 'w', encoding='utf-8')
    with open(r'X:\数据库\速卖通\smt_goodsinfo_202212[店铺id,卖家id,商品数目,商品id,销量,商品价格,商品价格_较高值,产品url,评分,商品名称,评论数量,媒体id,图片链接,标签].txt', 'r', encoding='utf-8') as smt_goodsinfo:
        n = 0
        for data_r in smt_goodsinfo:
            data_7 = data_r.strip('\n').split(",")
            # if n > 10000:
            #     break
            if len(data_7) >= 14:
                seller_id = data_7[0]
                price = data_7[6]
                comment_num = data_7[4]
                comment_num1 = int(comment_num) if comment_num else 0
                price1 = float(price) if price else 0
                sales_money = round(comment_num1 * price1, 2)
                sales_num_data_202207[seller_id][0].append(comment_num1)
                sales_num_data_202207[seller_id][1].append(sales_money)
                n += 1
        num = 0
        for s_id, sales_m in sales_num_data_202207.items():
            comment = sum(sales_m[0])
            sales_moneys = round(sum(sales_m[1]), 2)
            # sales_money_dict[s_id] = [comment, sales_moneys]
            data_list = [s_id, str(sales_moneys), str(comment)]
            sales_num_cz.write(','.join(data_list) + '\n')
            sales_num_cz.flush()
            num += 1
            if num % 10000 == 0:
                print(num)
        sales_num_cz.close()
    #     print(sales_moneys)
    # shopdata_sql = "select * from smt_shopinfo_202208"
    # smt_shopdata = session_kuajin.query_tuple_data(shopdata_sql)
    # sales_num_cz = open(r'X:\数据库\速卖通\{smt_shopinfo_2022111}[店铺ID,卖家ID,店铺名称,营业地址,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关,省,市,区,销量,销售额,粉丝数,店铺地址,开店时间,浙江地区当月销量].txt', 'w', encoding='utf-8')
    # with open(r'X:\数据库\速卖通\{smt_shopinfo_2022111_old}[店铺ID,卖家ID,店铺名称,营业地址,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关,省,市,区,销量,销售额,粉丝数,店铺地址,开店时间,浙江地区当月销量].txt', 'r', encoding='utf-8') as smt_shopinfo:
    #     num = 0
    #     for da in smt_shopinfo:
    #         num += 1
    #         data = da.strip('\n').split(",")
    #         seller_id = data[1]
    #         sales_num = sales_money_dict.get(seller_id, [0, 0])
    #         data[-1] = str(sales_num[1])
    #         data[-5] = str(sales_num[1])
    #         data[-6] = str(sales_num[0])
    #         sales_num_cz.write(','.join(data) + '\n')
    #         sales_num_cz.flush()
    #         if num % 10000 == 0:
    #             print(num)
    #     sales_num_cz.close()


def smt_sales_num_cz_new():
    '''
    速卖通销销售额计算方法
    '''
    sales_num_data_202207 = defaultdict(lambda: [[], []])
    # sales_money_dict = dict()
    comment_dict = dict()
    session_kuajin = DataBaseSession(kj_1_4_pool)
    query_sql = "select good_id, sales_num from smt_goodsinfo_202212  WHERE `sales_num` <> ''"
    smt_sales_num_7 = session_kuajin.query_tuple_data(query_sql)
    for sales_num_7 in smt_sales_num_7:
        comment_dict[sales_num_7[0]] = sales_num_7[1]
    sales_num_cz = open(r'X:\数据库\速卖通\{3_1_1_字典_速卖通_月统计}[店铺id,sum(销量 米 商品价格_较高值),sum(销量)].txt', 'w', encoding='utf-8')
    with open(r'X:\数据库\速卖通\{smt_goodsinfo_202301}[店铺id,卖家id,商品数目,商品id,销量,商品价格,商品价格_较高值,产品url,评分,商品名称,评论数量,媒体id,图片链接,标签].txt', 'r', encoding='utf-8') as smt_goodsinfo:
        n = 0
        for data_r in smt_goodsinfo:
            data_7 = data_r.strip('\n').split(",")
            # if n > 10000:
            #     break
            try:
                if len(data_7) >= 14:
                    shop_id = data_7[0]
                    goods_id = data_7[3]
                    old_sales = comment_dict.get(goods_id, 0)
                    price = data_7[6]
                    comment_num = data_7[4]
                    comment_num1 = int(comment_num) - int(old_sales) if comment_num else 0
                    if comment_num1 < 0:
                        comment_num1 = int(comment_num)
                    price1 = float(price) if price else 0
                    sales_money = round(comment_num1 * price1, 2)
                    sales_num_data_202207[shop_id][0].append(comment_num1)
                    sales_num_data_202207[shop_id][1].append(sales_money)
                    n += 1
            except Exception as e:
                print(data_7)
        num = 0
        for s_id, sales_m in sales_num_data_202207.items():
            comment = sum(sales_m[0])
            sales_moneys = round(sum(sales_m[1]), 2)
            # sales_money_dict[s_id] = [comment, sales_moneys]
            data_list = [s_id, str(sales_moneys), str(comment)]
            sales_num_cz.write(','.join(data_list) + '\n')
            sales_num_cz.flush()
            num += 1
            if num % 10000 == 0:
                print(num)
        sales_num_cz.close()
    #     print(sales_moneys)
    # shopdata_sql = "select * from smt_shopinfo_202208"
    # smt_shopdata = session_kuajin.query_tuple_data(shopdata_sql)
    # sales_num_cz = open(r'X:\数据库\速卖通\{smt_shopinfo_2022111}[店铺ID,卖家ID,店铺名称,营业地址,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关,省,市,区,销量,销售额,粉丝数,店铺地址,开店时间,浙江地区当月销量].txt', 'w', encoding='utf-8')
    # with open(r'X:\数据库\速卖通\{smt_shopinfo_2022111_old}[店铺ID,卖家ID,店铺名称,营业地址,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关,省,市,区,销量,销售额,粉丝数,店铺地址,开店时间,浙江地区当月销量].txt', 'r', encoding='utf-8') as smt_shopinfo:
    #     num = 0
    #     for da in smt_shopinfo:
    #         num += 1
    #         data = da.strip('\n').split(",")
    #         seller_id = data[1]
    #         sales_num = sales_money_dict.get(seller_id, [0, 0])
    #         data[-1] = str(sales_num[1])
    #         data[-5] = str(sales_num[1])
    #         data[-6] = str(sales_num[0])
    #         sales_num_cz.write(','.join(data) + '\n')
    #         sales_num_cz.flush()
    #         if num % 10000 == 0:
    #             print(num)
    #     sales_num_cz.close()


if __name__ == '__main__':
    # smt_sales_num_cz()
    import urllib
    smt_sales_num_cz_new()
    # aa = 'Adapters+%26+Connectors'
    # a = aa.encode()
    # b = a.decode()
    # print(a)
    # print(b)



