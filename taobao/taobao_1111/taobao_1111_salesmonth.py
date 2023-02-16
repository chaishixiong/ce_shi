all_data = {}  # 总数据字典
all_sales_month = {}  # 总销量数据字典
sales_month_list = []
sales_month_a = {}
sales_list = {
}
# with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\10月goodsinfo-第一轮.txt", "r", encoding="utf-8") as f_0:
#     for i_0 in f_0:
#         data_0 = i_0.strip().split(",")
#         goods_id_0 = data_0[0]
#         sales_month_0 = data_0[1] if len(data_0[1]) > 0 else 0
#         sales_month_a[goods_id_0] = int(sales_month_0)
#         # all_data[goods_id_0] = data_0

with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\10月goodsinfo-第一轮.txt", "r", encoding="utf-8") as f_0:
    for i_0 in f_0:
        data_0 = i_0.strip().split(",")
        goods_id_0 = data_0[0]
        sales_month_0 = int(data_0[1]) if len(data_0[1]) > 0 else 0
        sales_list[goods_id_0] = [int(sales_month_0)]

with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_1_new.txt", "r", encoding="utf-8") as f_1:
    for i_1 in f_1:
        data_1 = i_1.strip().split(",")
        goods_id_1 = data_1[1]
        sales_month_1 = int(data_1[3]) if len(data_1[3]) > 0 else 0
        sales_month_ls = sales_list.get(goods_id_1) if sales_list.get(goods_id_1) != None else []
        sales_month_ls.append(sales_month_1)
        sales_list[goods_id_1] = sales_month_ls

with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_2_new.txt", "r", encoding="utf-8") as f_2:
    for i_2 in f_2:
        data_2 = i_2.strip().split(",")
        goods_id_2 = data_2[1]
        sales_month_2 = int(data_2[3]) if len(data_2[3]) > 0 else 0
        sales_month_ls = sales_list.get(goods_id_2) if sales_list.get(goods_id_2) != None else []
        sales_month_ls.append(sales_month_2)
        sales_list[goods_id_2] = sales_month_ls

with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_3_new.txt", "r", encoding="utf-8") as f_3:
    for i_3 in f_3:
        data_3 = i_3.strip().split(",")
        goods_id_3 = data_3[1]
        sales_month_3 = int(data_3[3]) if len(data_3[3]) > 0 else 0
        sales_month_ls = sales_list.get(goods_id_3) if sales_list.get(goods_id_3) != None else []
        sales_month_ls.append(sales_month_3)
        sales_list[goods_id_3] = sales_month_ls

with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_4_new.txt", "r", encoding="utf-8") as f_4:
    for i_4 in f_4:
        data_4 = i_4.strip().split(",")
        goods_id_4 = data_4[1]
        sales_month_4 = int(data_4[3]) if len(data_4[3]) > 0 else 0
        sales_month_ls = sales_list.get(goods_id_4) if sales_list.get(goods_id_4) != None else []
        sales_month_ls.append(sales_month_4)
        sales_list[goods_id_4] = sales_month_ls










# sales_month_b = {}
with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_2_new.txt", "r", encoding="utf-8") as f_2:
    for i_2 in f_2:
        data_2 = i_2.strip().split(",")
        goods_id_2 = data_2[1]
        sales_month_2 = int(data_2[3]) if len(data_2[3]) > 0 else 0
        xiao_liang_list = sales_list.get(goods_id_2) if sales_list.get(goods_id_2) != None else [0]
        xiao_liang = xiao_liang_list[0] if len(xiao_liang_list) > 1 else 0
        num_sales = sales_month_2 - int(xiao_liang)
        if num_sales > 0:
            all_sales_month[goods_id_2] = [num_sales]
        else:
            all_sales_month[goods_id_2] = [0]
        all_data[goods_id_2] = data_2


with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_1_new.txt", "r", encoding="utf-8") as f_1:
    for i_1 in f_1:
        data_1 = i_1.strip().split(",")
        goods_id_1 = data_1[1]
        sales_month_1 = int(data_1[3]) if len(data_1[3]) > 0 else 0
        # s_1 = sales_month_a.get(goods_id_1) if sales_month_a.get(goods_id_1) != None else 0
        xiao_liang_list = sales_list.get(goods_id_1) if sales_list.get(goods_id_1) != None else [0]
        xiao_liang = xiao_liang_list[0] if len(xiao_liang_list) > 1 else 0
        num_sales = sales_month_1 - int(xiao_liang)
        data_1_list = all_sales_month.get(goods_id_1)
        if data_1_list != None:
            if num_sales > 0:
                data_1_list.append(num_sales)
                all_sales_month[goods_id_1] = data_1_list
            else:
                data_1_list.append(0)
                all_sales_month[goods_id_1] = data_1_list
        else:
            all_sales_month[goods_id_1] = [num_sales]
        all_data[goods_id_1] = data_1


with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_3_new.txt", "r", encoding="utf-8") as f_3:
    for i_3 in f_3:
        data_3 = i_3.strip().split(",")
        goods_id_3 = data_3[1]
        sales_month_3 = int(data_3[3]) if len(data_3[3]) > 0 else 0
        # s_3 = sales_month_a.get(goods_id_3) if sales_month_a.get(goods_id_3) != None else 0
        xiao_liang_list = sales_list.get(goods_id_3) if sales_list.get(goods_id_3) != None else [0]
        xiao_liang = xiao_liang_list[0] if len(xiao_liang_list) > 1 else 0
        num_sales = sales_month_3 - int(xiao_liang)
        data_3_list = all_sales_month.get(goods_id_3)
        if data_3_list != None:
            if num_sales > 0:
                data_3_list.append(num_sales)
                all_sales_month[goods_id_3] = data_3_list
            else:
                data_3_list.append(0)
                all_sales_month[goods_id_3] = data_3_list
        else:
            all_sales_month[goods_id_3] = [num_sales]
        all_data[goods_id_3] = data_3


with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_4_new.txt", "r", encoding="utf-8") as f_4:
    for i_4 in f_4:
        data_4 = i_4.strip().split(",")
        goods_id_4 = data_4[1]
        sales_month_4 = int(data_4[3]) if len(data_4[3]) > 0 else 0
        # s_4 = sales_month_a.get(goods_id_4) if sales_month_a.get(goods_id_4) != None else 0
        xiao_liang_list = sales_list.get(goods_id_4) if sales_list.get(goods_id_4) != None else [0]
        xiao_liang = xiao_liang_list[0] if len(xiao_liang_list) > 1 else 0
        num_sales = sales_month_4 - int(xiao_liang)
        data_4_list = all_sales_month.get(goods_id_4)
        if data_4_list != None:
            if num_sales > 0:
                data_4_list.append(num_sales)
                all_sales_month[goods_id_4] = data_4_list
            else:
                data_4_list.append(0)
                all_sales_month[goods_id_4] = data_4_list
        else:
            all_sales_month[goods_id_4] = [num_sales]
        all_data[goods_id_4] = data_4


file_write = open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_1111_all.txt", "w", encoding="utf-8")
with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\tmall_goodsmobile_1111_202011_4_all.txt", "r", encoding="utf-8") as f_all:
    num = 0
    for i in f_all:
        try:
            num += 1
            item = i.strip().split(",")
            all_goods = item[1]
            sales_cha_list = all_sales_month.get(all_goods) if all_sales_month.get(all_goods) != None else 0
            sales_cha = max(sales_cha_list) if sales_cha_list != 0 else 0
            item[25] = str(sales_cha)
            file_write.write(",".join(item) + "\n")
            if num % 1000000 == 0:
                print(num)
            # file_write.flush()
        except Exception as e:
            print(e)


# b_name = {}
# with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\2020_10.txt", "r", encoding="utf-8") as f_f:
#     b_num = 0
#     for i_i in f_f:
#         b_num += 1
#         if b_num % 1000000 == 0:
#             print(b_num)
#         data = i_i.strip().split(",")
#         shop_id = data[0]
#         seller_id = data[1]
#         b_name[seller_id] = shop_id
#
# file_write = open(r"C:\Users\Administrator\Desktop\tb\tmall_goodsmobile_1111_202011_4_all.txt", "w", encoding="utf-8")
# with open(r"C:\Users\Administrator\Desktop\tb\tmall_goodsmobile_1111_202011_4_all_new.txt", "r", encoding="utf-8") as f:
#     b_type = "B"
#     num = 0
#     for i in f:
#         try:
#             num += 1
#             item = i.strip().split(",")
#             good_id = item[1]
#             shop_id_i = b_name.get(good_id) if b_name.get(good_id) != None else ''
#             item[13] = shop_id_i
#             file_write.write(",".join(item) + "\n")
#             if num % 1000000 == 0:
#                 print(num)
#             # file_write.flush()
#         except Exception as e:
#             print(e)





