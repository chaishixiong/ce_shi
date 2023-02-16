
shop_dict = {}
# month = int(input("202012(除了1月1月要改):"))
# last_month = 1 if month == 12 else month-1
with open(r"C:\Users\Administrator\Desktop\tb\taobao_1111\{3_4_天猫卖家ID}[KEY,卖家ID].txt", "r", encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        shop_id = data[0]
        seller_id = data[1]
        shop_dict[seller_id] = shop_id
#
bid_dict = {}
with open(r"C:\Users\Administrator\Desktop\tb\taobao_1111\{8_0_0_天猫商品信息}[商品ID,库存,bid].txt", "r", encoding="utf-8") as f:
    num = 0
    for i in f:
        num += 1
        if num % 1000000 == 0:
            print(num)
        data = i.strip().split(",")
        goods_id = data[0]
        inventory_id = data[1]
        bid = data[2]
        bid_dict[goods_id] = bid

b_name = {}
with open(r"C:\Users\Administrator\Desktop\tb\taobao_1111\bid_bname.csv", "r", encoding="utf-8") as f_f:
    b_num = 0
    for i_i in f_f:
        b_num += 1
        if b_num % 1000000 == 0:
            print(b_num)
        data = i_i.strip().split(",")
        b_name_id = data[0]
        name_b = data[1]
        b_name[b_name_id] = name_b

file_write = open(r"C:\Users\Administrator\Desktop\tb\taobao_1111\tmall_goodsmobile_20211111_3_old.txt", "w", encoding="utf-8")
with open(r"C:\Users\Administrator\Desktop\tb\taobao_1111\tmall_goodsmobile_20211111_3.txt", "r", encoding="utf-8") as f:
    b_type = "B"
    num = 0
    for i in f:
        try:
            num += 1
            data = i.strip().split(",")
            goods_id = data[1]
            sales_mouth = data[2]
            inventory = data[4]
            cid = data[7]
            if bid_dict.get(goods_id) != None:
                bid = bid_dict.get(goods_id)
                b_name_name = b_name.get(bid) if b_name.get(bid) != None else ''
            else:
                bid = ''
                b_name_name = ''
            good_name = data[10]
            seller_id = data[11]
            shop_id = shop_dict.get(seller_id) if shop_dict.get(seller_id) != None else ''
            price = data[14]
            pic = data[24]
            mark = "双11"
            write_data = [""] * 27
            write_data[1] = goods_id  # goods_id 商品ID
            write_data[2] = sales_mouth  # veges_month 销量
            write_data[3] = sales_mouth  # sales_month 销量
            write_data[4] = ''  # comment_count
            write_data[5] = inventory  # inventory  库存
            write_data[6] = ''  # collect_num
            write_data[7] = ''  # address 发货地址
            write_data[8] = cid  # cid 天猫类目ID
            write_data[9] = bid if bid != None else ''  # bid 天猫品牌ID
            write_data[10] = b_type  # bc_type 平台
            write_data[11] = good_name  # goods_name 天猫商品名称
            write_data[12] = seller_id  # seller_id 卖家ID
            write_data[13] = shop_id  # shop_id 店铺ID
            write_data[14] = price  # discount_price 折扣价
            write_data[15] = price  # real_price 真实扣价
            write_data[16] = ''  # price_area 区间价格
            write_data[17] = ''  # price
            write_data[18] = pic  # image_url
            write_data[19] = mark  # mark 双十一标识
            write_data[20] = ''  # mark2 跨店
            write_data[21] = ''  # obtained 是否下架
            write_data[22] = ''  # c_name1 类别
            write_data[23] = ''  # c_name2 类别2TypeError: sequence item 24: expected str instance, NoneType found
            write_data[24] = b_name_name  # b_name 品牌name
            write_data[25] = ''  # sales_cha 销量差值
            write_data[26] = ''  # sales_money 销售额
            file_write.write(",".join(write_data)+"\n")
            if num % 1000000 == 0:
                print(num)
                # file_write.flush()
        except Exception as e:
            print(e)





