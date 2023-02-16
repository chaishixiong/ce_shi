def taobao_tm_shop():
    b_name = {}
    with open(r"C:\Users\Administrator\Desktop\tmall\tmall_shopinfo_202201.txt", "r", encoding="utf-8") as f_f:
        b_num = 0
        for i_i in f_f:
            b_num += 1
            if b_num % 1000000 == 0:
                print(b_num)
            data = i_i.strip().split(",")
            b_name[data[0]] = data

    file_write = open(r"C:\Users\Administrator\Desktop\tmall\tmall_shopinfo_202202_new.txt", "w", encoding="utf-8")
    with open(r"C:\Users\Administrator\Desktop\tmall\tmall_shopinfo_202202.txt", "r", encoding="utf-8") as f:
        b_type = "B"
        num = 0
        for i in f:
            try:
                num += 1
                data = i.strip().split(",")
                goods_id = data[0]
                shop_name = b_name.get(goods_id)
                # shop_fans_num = data[13]
                # goods_num = data[15]
                # new_goods_num = data[16]
                if shop_name == None:
                    file_write.write(",".join(data) + "\n")
                    # pass
                # elif len(shop_fans_num) > 0 and len(goods_num) > 0 and len(new_goods_num) > 0:
                #     file_write.write(",".join(data) + "\n")
                else:
                    # 天猫店铺信息更新
                    data[7] = shop_name[7]
                    data[8] = shop_name[8]
                    data[9] = shop_name[9]
                    data[10] = shop_name[10]  # shop_name
                    data[11] = shop_name[11]
                    data[12] = shop_name[12]
                    data[13] = shop_name[13]
                    data[14] = shop_name[14]
                    data[15] = shop_name[15]
                    data[16] = shop_name[16]  # shop_name
                    data[17] = shop_name[17]
                    data[18] = shop_name[18]
                    data[19] = shop_name[19]
                    data[20] = shop_name[20]
                    data[21] = shop_name[21]
                    data[22] = shop_name[22]  # shop_name
                    data[23] = shop_name[23]
                    data[24] = shop_name[24]
                    data[25] = shop_name[25]  # shop_name
                    data[26] = shop_name[26]
                    data[27] = shop_name[27]
                    data[28] = shop_name[28]
                    data[29] = shop_name[29]
                    data[30] = shop_name[30]
                    data[31] = shop_name[31]

                    # 淘宝店铺信息更新
                    # data[5] = shop_name[11]
                    # data[6] = shop_name[10]
                    file_write.write(",".join(data)+"\n")
                if num % 10000 == 0:
                    print(num)
                    file_write.flush()
            except Exception as e:
                print(e)
    # b_name = {}
    # with open(r"C:\Users\Administrator\Desktop\tb\tmall_shopinfo_new\tmall_shopinfo_202108.txt", "r", encoding="utf-8") as f_f:
    #     b_num = 0
    #     for i_i in f_f:
    #         b_num += 1
    #         if b_num % 1000000 == 0:
    #             print(b_num)
    #         data = i_i.strip().split(",")
    #         b_name[data[0]] = [data[1], data[2], data[3]]
    #
    # for i in range(202101, 202106):
    #     file_write = open(r"C:\Users\Administrator\Desktop\tb\tmall_shopinfo_{}_new.txt".format(i), "w", encoding="utf-8")
    #     with open(r"C:\Users\Administrator\Desktop\tb\tmall_shopinfo_{}.txt".format(i), "r", encoding="utf-8") as f:
    #         b_type = "B"
    #         num = 0
    #         for i in f:
    #             try:
    #                 num += 1
    #                 data = i.strip().split(",")
    #                 goods_id = data[0]
    #                 data_data = b_name.get(goods_id)
    #                 if data_data == None:
    #                     file_write.write(",".join(data) + "\n")
    #                     file_write.flush()
    #                 else:
    #                     province = data_data[0]
    #                     city = data_data[1]
    #                     county = data_data[2]
    #                     data[14] = province
    #                     data[15] = city
    #                     data[16] = county
    #                     file_write.write(",".join(data)+"\n")
    #                     if num % 1000000 == 0:
    #                         print(num)
    #                         file_write.flush()
    #             except Exception as e:
    #                 print(e)


file_write_1 = open(r"F:\{taobao_look-data_tmall}[goods]_1.txt", "w", encoding="utf-8")
file_write_2 = open(r"F:\{taobao_look-data_tmall}[goods]_2.txt", "w", encoding="utf-8")


with open(r"F:\{taobao_look-data_tmall}[goods].txt", "r", encoding="utf-8") as f_f:
    b_num = 0
    for i_i in f_f:
        b_num += 1
        if b_num > 35000000:
            file_write_2.write(i_i)
        else:
            file_write_1.write(i_i)
