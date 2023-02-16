c_id = dict()
with open(r"X:\数据库\taobao\{taobao_look-data_zhejiang}[goods,seller_id,price,sales,name,cid,score,url].txt","r",encoding="utf-8") as cid_f:
    for cid in cid_f:
        print()

file_write = open(r"X:\数据库\taobao\taobao_goodsmobile_202111.txt", "a", encoding="utf-8")
with open(r"X:\数据库\taobao\{taobao_look-data_zhejiang}[goods,seller_id,price,sales,name,cid,score,url].txt","r",encoding="utf-8") as data_f:
    num = 0
    for i in data_f:
        try:
            num += 1
            data = i.strip().split(",")
            c_cid = data[0]
            c_data = c_id.get(c_cid)
            if c_data != None:
                file_write.write(",".join(data) + "\n")
                if num % 1000000 == 0:
                    print(num)
                    file_write.flush()
        except Exception as e:
            pass




