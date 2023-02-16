# sales_month_a = {}
# with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\10月goodsinfo-第一轮.txt", "r", encoding="utf-8") as f_0:
#     for i_0 in f_0:
#         data_0 = i_0.strip().split(",")
#         goods_id_0 = data_0[0]
#         sales_month_0 = int(data_0[1]) if len(data_0[1]) > 0 else 0
#         sales_month_a[goods_id_0] = [int(sales_month_0)]
#
# with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_1_new.txt", "r", encoding="utf-8") as f_1:
#     for i_1 in f_1:
#         data_1 = i_1.strip().split(",")
#         goods_id_1 = data_1[1]
#         sales_month_1 = int(data_1[3]) if len(data_1[3]) > 0 else 0
#         sales_month_ls = sales_month_a.get(goods_id_1) if sales_month_a.get(goods_id_1) != None else []
#         sales_month_ls.append(sales_month_1)
#         sales_month_a[goods_id_1] = sales_month_ls
#
# with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_2_new.txt", "r", encoding="utf-8") as f_2:
#     for i_2 in f_2:
#         data_2 = i_2.strip().split(",")
#         goods_id_2 = data_2[1]
#         sales_month_2 = int(data_2[3]) if len(data_2[3]) > 0 else 0
#         sales_month_ls = sales_month_a.get(goods_id_2) if sales_month_a.get(goods_id_2) != None else []
#         sales_month_ls.append(sales_month_2)
#         sales_month_a[goods_id_2] = sales_month_ls
#
# with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_3_new.txt", "r", encoding="utf-8") as f_3:
#     for i_3 in f_3:
#         data_3 = i_3.strip().split(",")
#         goods_id_3 = data_3[1]
#         sales_month_3 = int(data_3[3]) if len(data_3[3]) > 0 else 0
#         sales_month_ls = sales_month_a.get(goods_id_3) if sales_month_a.get(goods_id_3) != None else []
#         sales_month_ls.append(sales_month_3)
#         sales_month_a[goods_id_3] = sales_month_ls
#
# with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_4_new.txt", "r", encoding="utf-8") as f_4:
#     for i_4 in f_4:
#         data_4 = i_4.strip().split(",")
#         goods_id_4 = data_4[1]
#         sales_month_4 = int(data_4[3]) if len(data_4[3]) > 0 else 0
#         sales_month_ls = sales_month_a.get(goods_id_4) if sales_month_a.get(goods_id_4) != None else []
#         sales_month_ls.append(sales_month_4)
#         sales_month_a[goods_id_4] = sales_month_ls

# sales_month_a = {
#     "aaa": [1,2,3,4]
# }
# file_write = open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\all_sales_list.txt", "w", encoding="utf-8")
# num = 0
# for item_k, item_v in zip(sales_month_a.keys(), sales_month_a.values()):
#     try:
#         num += 1
#         datal_l = [item_k, str(item_v)]
#         file_write.write(",".join(datal_l) + "\n")
#         if num % 1000000 == 0:
#             print(num)
#         # file_write.flush()
#     except Exception as e:
#         print(e)

with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\all_sales_list.txt", "r", encoding="utf-8") as f_4:
    for i_4 in f_4:
        data_4 = i_4.strip().split(",")
        print(data_4)







