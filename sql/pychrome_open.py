def sql_id():
    list1 = []
    with open('data_合并.txt', encoding='utf-8') as f:
        res = f.readlines()
    with open('data_data.txt', 'a', encoding='utf-8') as fs:
        b = 1
        for i in res:
            write_data = [""] * 22
            i = i.strip('\n').split(',')
            write_data[0] = str(b)
            write_data[1] = i[0]  # goods_id 商品ID
            write_data[2] = i[1]  # veges_month 销量
            write_data[3] = i[2]  # sales_month 销量
            write_data[4] = i[3]  # comment_count
            write_data[5] = i[4]  # inventory
            write_data[7] = i[6]  # address 发货地址
            write_data[8] = i[7]  # cid 天猫类目ID
            write_data[9] = i[8]  # bid 天猫品牌ID
            write_data[10] = i[9]  # bc_type 平台
            write_data[11] = i[10]  # goods_name 天猫商品名称
            write_data[12] = i[11]  # seller_id 卖家ID
            write_data[13] = i[12]  # shop_id 店铺ID
            write_data[14] = i[13]  # discount_price 折扣价
            write_data[16] = i[14]  # price_area 区间价格
            write_data[17] = i[15]  # price
            write_data[18] = i[16]  # image_url
            write_data[19] = i[17]  # mark 双十一标识
            write_data[21] = i[5]
            fs.write(",".join(write_data) + "\n")
            b += 1
        fs.close()
    print(list1)


def sql_cid_cid():
    list1 = []
    with open('cpi_cid.txt', encoding='utf-8') as f:
        res = f.readlines()
        for i in res:
            i = i.strip()
            a = i
            if i != '' and i not in list1:
                # print(i, 'shop'+i+'.taobao.com')
                list1.append(a)
    print(list1)
    print(len(list1))


def sql_shop_id():
    with open('cpi_cid.csv', encoding='utf-8') as f:
        res = f.readlines()


if __name__ == '__main__':
    sql_id()

