al_yb_zip_dict = dict()

with open('X:\数据库\阿里巴巴国际站\seed\阿里巴巴国际邮编.txt', 'r', encoding='utf-8') as f:
    for yb_zio in f:
        yb_zio_list = yb_zio.strip('\n').split(',')
        # al_key = yb_zio_list[0]
        # al_zip = yb_zio_list[1]
        al_yb_zip_dict[yb_zio_list[0]] = yb_zio_list[1]

alibabagj_shopinfo_new = open('X:\数据库\阿里巴巴国际站\{alibabagj_shopinfo}[key,url,company_name,address_detail,country,province,city,address,zip,contact_people,sales_money,sales_num,company_type,keep_time].txt', 'w', encoding='utf-8')
with open('X:\数据库\阿里巴巴国际站\{alibabagj_shopinfo_old}[key,url,company_name,address_detail,country,province,city,address,zip,contact_people,sales_money,sales_num,company_type,keep_time].txt', 'r', encoding='utf-8') as alibabagj_shopinfo:
    for data in alibabagj_shopinfo:
        data_list = data.strip('\n').split(',')
        al_id = data_list[0]
        al_zip = al_yb_zip_dict.get(al_id, '')
        data_list[8] = al_zip
        alibabagj_shopinfo_new.write(','.join(data_list) + '\n')
        alibabagj_shopinfo_new.flush()
    alibabagj_shopinfo_new.close()





