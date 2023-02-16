f_n = open('dm_county_shoplist_kj_new.txt', 'a', encoding='utf-8')
n = 39576
for d in range(202102, 202112):
    with open(r'C:\Users\Administrator\Desktop\c_金华\美国亚马逊\ods_amazonus_shopinfo_{}.txt'.format(d), 'r', encoding='utf-8') as f:
        for i in f:
            n += 1
            data = i.strip('\n').split(',')
            # data[1] = str(d)
            data.insert(0, str(n))
            f_n.write(', '.join(data) + '\n')




