from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import life_227_pool

data_dict = {}
life_server = DataBaseSession(life_227_pool)


def opne_data():
    data_dict = {}
    # with open(r'D:\data\shop_all_comment_num.txt', 'r', encoding='utf-8') as f:
    #     for i in f:
    #         data_list = i.strip('\n').split(',')
    #         try:
    #             data_dict[data_list[0]] = data_list[1]
    #         except Exception as e:
    #             print(data_list)

    quest = 'select shop_id from meituan_wenzhou_new'
    shop_id_list = life_server.query_tuple_data(quest)
    for shop_id_t in shop_id_list:
        shop_id = shop_id_t[0]
        all_comment_num = data_dict.get(str(shop_id))
        if all_comment_num:
            updata_sql = 'UPDATE meituan_wenzhou_new set all_comment_num = {} where shop_id = {}'.format(all_comment_num, shop_id)
            life_server.updata_data(updata_sql)
            print(str(shop_id) + '===' + all_comment_num)


if __name__ == '__main__':
    opne_data()


