
# shop_dict = {}
# # month = int(input("202012(除了1月1月要改):"))
# # last_month = 1 if month == 12 else month-1
# with open(r"C:\Users\Administrator\Desktop\{3_4_天猫卖家ID}[KEY,卖家ID].txt", "r", encoding="utf-8") as f:
#     for i in f:
#         data = i.strip().split(",")
#         shop_id = data[0]
#         seller_id = data[1]
#         shop_dict[seller_id] = shop_id
#
# bid_dict = {}
# with open(r"C:\Users\Administrator\Desktop\{8_0_0_天猫商品信息}[商品ID,库存,bid].txt", "r", encoding="utf-8") as f:
#     num = 0
#     for i in f:
#         num += 1
#         if num % 1000000 == 0:
#             print(num)
#         data = i.strip().split(",")
#         goods_id = data[0]
#         inventory_id = data[1]
#         bid = data[2]
#         bid_dict[goods_id] = (inventory_id, bid)
'''
update_date,goods_id,sales_month,comment_count,inventory,collect_num,address,cid,bid,bc_type,goods_name,seller_id,shop_id,discount_price,price_area,price,image_url
'''
# b_name = {}
# with open(r"C:\Users\Administrator\Desktop\tmall_goodsmobile_618_202102.txt", "r", encoding="utf-8") as f_f:
#     b_num = 0
#     for i_i in f_f:
#         b_num += 1
#         if b_num % 1000000 == 0:
#             print(b_num)
#         data = i_i.strip().split(",")
#         b_name_id = data[1]
#         b_name[b_name_id] = i_i
#
# file_write = open(r"C:\Users\Administrator\Desktop\goods_tmall_202105.txt", "w", encoding="utf-8")
# with open(r"C:\Users\Administrator\Desktop\tmall_goodsmobile_202105.txt", "r", encoding="utf-8") as f:
#     b_type = "B"
#     num = 0
#     for i in f:
#         try:
#             num += 1
#             data = i.strip().split(",")
#             goods_id = data[0]
#             sales_mouth = data[3]
#             inventory = bid_dict.get(goods_id, ["", ""])[0]
#             cid = data[5]
#             bid = bid_dict.get(goods_id, ["", ""])[1]
#             good_name = data[4]
#             seller_id = data[1]
#             shop_id = shop_dict.get(seller_id, "")
#             price = data[2]
#             pic = data[7]
#             mark = data[8]
#             b_name = b_name.get(bid)
#             write_data = [""] * 27
#             write_data[1] = goods_id  # goods_id 商品ID
#             write_data[2] = sales_mouth  # veges_month 销量
#             write_data[3] = sales_mouth  # sales_month 销量
#             write_data[4] = ''  # comment_count
#             write_data[5] = inventory  # inventory
#             write_data[6] = ''  # collect_num
#             write_data[7] = ''  # address 发货地址
#             write_data[8] = cid  # cid 天猫类目ID
#             write_data[9] = bid  # bid 天猫品牌ID
#             write_data[10] = b_type  # bc_type 平台
#             write_data[11] = good_name  # goods_name 天猫商品名称
#             write_data[12] = seller_id  # seller_id 卖家ID
#             write_data[13] = shop_id  # shop_id 店铺ID
#             write_data[14] = price  # discount_price 折扣价
#             write_data[15] = price  # real_price 真实扣价
#             write_data[16] = ''  # price_area 区间价格
#             write_data[17] = ''  # price
#             write_data[18] = pic  # image_url
#             write_data[19] = mark  # mark 双十一标识
#             write_data[20] = ''  # mark2 跨店
#             write_data[21] = ''  # obtained 是否下架
#             write_data[22] = ''  # c_name1 类别
#             write_data[23] = ''  # c_name2 类别2TypeError: sequence item 24: expected str instance, NoneType found
#             write_data[24] = b_name  # b_name 品牌name
#             write_data[25] = ''  # sales_cha 销量差值
#             write_data[26] = ''  # sales_money 销售额
#             file_write.write(",".join(write_data)+"\n")
#             if num % 1000000 == 0:
#                 print(num)
#                 file_write.flush()
#         except Exception as e:
#             print(e)


def tm_updata_data():
    new_202107_227 = open(r"new_tmall_shopinfo_202107.txt", "a", encoding="utf-8")
    new_202107_228 = open(r"new_tmall_shopinfo_202107_228.txt", "a", encoding="utf-8")

    tmall_227_old = {}
    with open(r"tmall_shopinfo_202107_old.txt", "r", encoding="utf-8") as tm_227_old:
        for tm_227_o in tm_227_old:
            tm_s = tm_227_o.strip('\n')
            tm_seed_id = tm_s.split(',')
            tmall_227_old[tm_seed_id[0]] = tm_seed_id[15]

    # with open(r"tmall_shopinfo_202107_228.txt", "r", encoding="utf-8") as tm_228_old:
    #     for tm_228 in tm_228_old:
    #         tm_s = tm_228.strip('\n')
    #         shop_data = tm_s.split(',')
    #         shop_id = shop_data[0]
    #         goods_num = tmall_227_old.get(shop_id)
    #         if goods_num != None:
    #             shop_data[15] = goods_num
    #             new_202107_228.write(",".join(shop_data) + "\n")

    with open(r"tmall_shopinfo_202107.txt", "r", encoding="utf-8") as tm_227:
        for i in tm_227:
            s_id = i.strip('\n')
            shop_data_227 = s_id.split(',')
            shop_id_2 = shop_data_227[0]
            goods_num_227 = tmall_227_old.get(shop_id_2)
            if goods_num_227 != None:
                if len(shop_data_227) == 32:
                    shop_data_227[15] = goods_num_227
                    new_202107_227.write(",".join(shop_data_227) + "\n")


if __name__ == '__main__':
    tm_updata_data()




