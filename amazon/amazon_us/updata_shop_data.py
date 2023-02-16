#  处理店铺销量与评分
import re


def re_shop_data():
    new_shop_data = open(r'X:\数据库\美国亚马逊\{amazonus_shopinfo_202301_old}[KEY,店铺名称,店铺介绍,公司,公司地址信息,国家,邮编,公司原始信息,30天好评率,30天中评率,30天差评率,30天评论数,90天好评率,90天中评率,90天差评率,90天评论数,12月好评率,12月中评率,12月差评率,12月评论数,累积好评率,累积中评率,累积差评率,累积评论数,省,市,区,main_sales,店铺单价].txt', 'w', encoding='utf-8')
    with open(r'X:\数据库\美国亚马逊\{amazonus_shopinfo_202301_old_old}[KEY,店铺名称,店铺介绍,公司,公司地址信息,国家,邮编,公司原始信息,30天好评率,30天中评率,30天差评率,30天评论数,90天好评率,90天中评率,90天差评率,90天评论数,12月好评率,12月中评率,12月差评率,12月评论数,累积好评率,累积中评率,累积差评率,累积评论数,省,市,区,main_sales,店铺单价].txt', 'r', encoding='utf-8') as old_shop_data:
        for shop_data in old_shop_data:
            shop_data_list = shop_data.strip().split(',')
            shop_data_list.append('')
            shop_data_list.append('')
            shop_data_list.append('')
            shop_data_list.append('')
            shop_data_list.append('')
            shop_data_list.append('')
            shop_data_list.append('')
            shop_data_list.append('')
            if len(shop_data_list) == 29:
                shop_data_list[8] = re_data(shop_data_list[8])
                shop_data_list[11] = re_data(shop_data_list[9])
                shop_data_list[12] = re_data(shop_data_list[10])
                shop_data_list[15] = re_data(shop_data_list[11])
                shop_data_list[16] = re_data(shop_data_list[12])
                shop_data_list[19] = re_data(shop_data_list[13])
                shop_data_list[20] = re_data(shop_data_list[14])
                shop_data_list[23] = re_data(shop_data_list[15])

                shop_data_list[9] = ''
                shop_data_list[10] = ''
                shop_data_list[13] = ''
                shop_data_list[14] = ''
                shop_data_list[17] = ''
                shop_data_list[18] = ''
                shop_data_list[21] = ''
                shop_data_list[22] = ''
                new_shop_data.write(','.join(shop_data_list) + '\n')
                new_shop_data.flush()
            else:
                new_shop_data.write(','.join(shop_data_list) + '\n')
                new_shop_data.flush()


def re_data(data):
    num_data = data.replace("['", '').replace("']", '').replace("，", "")
    return num_data


if __name__ == '__main__':
    re_shop_data()

