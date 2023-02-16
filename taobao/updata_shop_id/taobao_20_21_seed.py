b_name = {}
with open(r"C:\Users\Administrator\Desktop\taobao_seed\taobao_tm_sed.txt", "r", encoding="utf-8") as f_f:
    b_num = 0
    for i_i in f_f:
        data = i_i.strip().split(",")
        seller_id = data[1]
        b_name[seller_id] = data[0]

file_write = open(r"C:\Users\Administrator\Desktop\taobao_seed\taobao_tm_look_new.txt", "w", encoding="utf-8")
with open(r"C:\Users\Administrator\Desktop\taobao_seed\tmall_20_21_seet.txt", "r", encoding="utf-8") as f:
    num = 0
    for i in f:
        try:
            num += 1
            data = i.strip().split(",")
            seller_id = data[1]
            shop_name = b_name.get(seller_id)
            if shop_name == None:
                file_write.write(seller_id + "\n")
                # pass
            # else:
            #     # 淘宝天猫信用信息更新
            #     data[10] = shop_name[1]  # shop_hpl
            #     data[2] = shop_name[2]  # describe_rate
            #     data[5] = shop_name[3]   # service_rate
            #     data[8] = shop_name[4]   # logistics_rate
            #     file_write.write(",".join(data)+"\n")
            if num % 1000000 == 0:
                print(num)
                file_write.flush()
        except Exception as e:
            print(e)

