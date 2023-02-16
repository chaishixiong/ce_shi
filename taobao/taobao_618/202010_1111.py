shop_dict = {}
# month = int(input("202012(除了1月1月要改):"))
# last_month = 1 if month == 12 else month-1
with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\2020_10.txt", "r", encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        shop_id = data[0]
        seller_id = data[1]
        shop_dict[seller_id] = shop_id


file_write = open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_4_new.txt", "w", encoding="utf-8")
with open(r"C:\Users\Administrator\Desktop\tb\taobao_shop\shop_202010\tmall_goodsmobile_1111_202011_4.txt", "r", encoding="utf-8") as f:
    b_type = "B"
    num = 0
    for i in f:
        try:
            num += 1
            data = i.strip().split(",")
            seller_id = data[12]
            shop_i = shop_dict.get(seller_id) if shop_dict.get(seller_id) != None else ''
            data[13] = shop_i
            file_write.write(",".join(data)+"\n")
            if num % 1000000 == 0:
                print(num)
                # file_write.flush()
        except Exception as e:
            print(e)



