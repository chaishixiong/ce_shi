def updata_smt_shop_name():
    shop_data = {}
    with open(r"smt_shopinfo_202106.txt", "r", encoding="utf-8") as f_f:
        b_num = 0
        for i_i in f_f:
            b_num += 1
            if b_num % 1000000 == 0:
                print(b_num)
            data_1 = i_i.strip().split(",")
            b_name_id = data_1[0]
            shop_data[b_name_id] = data_1[1]
    num = 0
    file_write = open(r"smt_shopinfo_202107_new.txt", "a", encoding="utf-8")
    with open(r"smt_shopinfo_202107.txt", "r", encoding="utf-8") as f:
        for i in f:
            try:
                num += 1
                data = i.strip().split(",")
                new_shop_name = data[0]
                shop_name = shop_data.get(new_shop_name)
                if shop_name != None:
                    data[2] = shop_name
                    file_write.write(",".join(data) + "\n")
                else:
                    file_write.write(",".join(data) + "\n")
                if num % 1000000 == 0:
                    print(num)
                    file_write.flush()
            except Exception as e:
                print(e)


if __name__ == '__main__':
    updata_smt_shop_name()
