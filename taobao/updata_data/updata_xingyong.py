b_name = {}
with open(r"C:\Users\Administrator\Desktop\tb\xingyong\taobao_shopinfo_202106_cp.txt", "r", encoding="utf-8") as f_f:
    b_num = 0
    for i_i in f_f:
        b_num += 1
        if b_num % 1000000 == 0:
            print(b_num)
        data = i_i.strip().split(",")
        b_name[data[0]] = data

file_write = open(r"C:\Users\Administrator\Desktop\tb\xingyong\taobao_shop_xinyong_202106.txt", "w", encoding="utf-8")
with open(r"C:\Users\Administrator\Desktop\tb\xingyong\taobao_shop_xinyong_202107.txt", "r", encoding="utf-8") as f:
    num = 0
    for i in f:
        try:
            num += 1
            data = i.strip().split(",")
            goods_id = data[0]
            shop_name = b_name.get(goods_id)
            if shop_name == None:
                file_write.write(",".join(data) + "\n")
                # pass
            else:
                # 淘宝天猫信用信息更新
                data[10] = shop_name[1]  # shop_hpl
                data[2] = shop_name[2]  # describe_rate
                data[5] = shop_name[3]   # service_rate
                data[8] = shop_name[4]   # logistics_rate
                file_write.write(",".join(data)+"\n")
            if num % 1000000 == 0:
                print(num)
                file_write.flush()
        except Exception as e:
            print(e)

