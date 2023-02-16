def quchong_amazon_sortshop():
    goodsid_set = set()
    with open(r'X:\数据库\美国亚马逊\us_seed\amazon_goods_id\amazon_goods_id_2212_2301.txt', 'r', encoding='utf-8') as r:
        for seed_data in r:
            goodsid = seed_data.strip('\n')
            goodsid_set.add(goodsid)

    new_goodsid_w = open(r'W:\scrapy_seed\amazon_sortshop.txt', 'w', encoding='utf-8')

    with open(r'X:\数据库\美国亚马逊\us_seed\amazon_goods_id\amazon_goods_id_23010913.txt', 'r', encoding='utf-8') as new_r:
        for seed_data_1 in new_r:
            goods_id = seed_data_1.strip('\n')
            if goods_id not in goodsid_set:
                goodsid_set.add(goods_id)
                new_goodsid_w.write(seed_data_1)
                new_goodsid_w.flush()
        new_goodsid_w.close()


if __name__ == '__main__':
    # with_r()
    # quchong_amazon_sortshop()
    z = dict()
    z['a'] = ''
    z['b'] = ''
    z['c'] = ''
    z['d'] = ''
    l = ['a', 'b', 'c']
    b = ['q', 'w', 'e']
    # for z_d, f in zip(z, range(0, len(b))):
    #     z_d = b[f]
    for i in range(0, len(b)):
        z[l[i]] = b[i]
    print(z)


