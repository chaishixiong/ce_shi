def taobao_cid_data():
    with open(r"D:\tb_data\taobao_goodsmobile_202111.txt", "r", encoding="utf-8") as f_f:
        b_num = 0
        for i_i in f_f:
            b_num += 1
            if b_num % 1000000 == 0:
                print(b_num)
            data = i_i.strip().split(",")
            try:
                cid_int = int(data[8])
            except Exception as e:
                print(data)


if __name__ == '__main__':
    taobao_cid_data()




