def quchong_smt_wx_shop():
    seed_data_dict = dict()
    with open(r'X:\数据库\速卖通\速卖通无效店铺.txt', 'r', encoding='utf-8') as r:
        for seed_data in r:
            seed_list = seed_data.strip('\n').split(',')
            seed_data_dict[seed_list[0]] = seed_list[0]

    new_shop_w = open(r'X:\数据库\速卖通\smt_comment.txt', 'w', encoding='utf-8')

    with open(r'D:\速卖通\{速卖通_商品种子}[卖家id,商品id].txt', 'r', encoding='utf-8') as new_r:
        for seed_data_1 in new_r:
            seed_list_1 = seed_data_1.strip('\n').split(',')
            di = seed_list_1[0]
            asas = seed_data_dict.get(di)
            if asas == None:
                new_shop_w.write(seed_data_1)
                new_shop_w.flush()
        new_shop_w.close()


def quchong_smt_pzinfo():
    seed_data_dict = set()
    with open(r'X:\数据库\速卖通\速卖通_拍照信息_合并.txt', 'r', encoding='utf-8') as r:
        for seed_data in r:
            seed_list = seed_data.strip('\n').split(',')
            shopid = seed_list[0]
            seed_data_dict.add(shopid)

    new_shop_w = open(r'X:\数据库\速卖通\seed\smt_pzinfo.txt', 'w', encoding='utf-8')

    with open(r'X:\数据库\速卖通\seed\smt_shopid_new[1].txt', 'r', encoding='utf-8') as new_r:
        for seed_data_1 in new_r:
            shop_id = seed_data_1.strip('\n')
            if shop_id not in seed_data_dict:
                new_shop_w.write(seed_data_1)
                new_shop_w.flush()
        new_shop_w.close()


def cookie_to_dic(cookie):
    cookies_list = []
    for item in cookie.split('; '):
        cooie_dict = dict()
        item_list = item.split('=')
        cooie_dict['name'] = item_list[0]
        cooie_dict['value'] = item_list[1]
        cookies_list.append(cooie_dict)
    print(cookies_list)
    # return {item.split('=')[0]: item.split('=')[1] for item in cookie.split('; ')}


if __name__ == '__main__':
    quchong_smt_pzinfo()


