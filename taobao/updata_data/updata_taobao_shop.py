b_name = {}
with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\jd_goodssales_202004.txt", "r", encoding="utf-8") as f_f:
    b_num = 0
    for i_i in f_f:
        b_num += 1
        if b_num % 1000000 == 0:
            print(b_num)
        data = i_i.strip().split(",")
        b_name[data[0]] = data


a_name = {}
with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\jd_shopinfo_202104_cp.txt", "r", encoding="utf-8") as f_f:
    a_num = 0
    for i_i in f_f:
        a_num += 1
        if a_num % 1000000 == 0:
            print(a_num)
        adata = i_i.strip().split(",")
        a_name[adata[0]] = adata

file_write = open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\jd_shopinfo_202104_new.txt", "w", encoding="utf-8")
with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\jd_shopinfo_202104.txt", "r", encoding="utf-8") as f:
    num = 0
    for i in f:
        try:
            num += 1
            data = i.strip().split(",")
            goods_id = data[0]
            sales_count = b_name.get(goods_id)
            sales_money = b_name.get(goods_id)
            if sales_count == None:
                file_write.write(",".join(data) + "\n")
                print(1)
                # pass
            else:
                # 淘宝天猫信用信息更新
                data[16] = shop_name[3]  # shop_hpl
                data[27] = shop_name[2]  # describe_rate
                file_write.write(",".join(data)+"\n")
            if num % 1000000 == 0:
                print(num)
                file_write.flush()
        except Exception as e:
            print(e)

