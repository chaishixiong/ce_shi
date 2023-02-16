import json


def run_data():
    data_name = open(r'data_data.txt', 'a', encoding='utf-8')
    with open(r'本地淘宝企业信息11.txt', 'r', encoding='utf-8') as read:
        for d in read:
        # dict_data = data.strip('[').strip(']')
            data_list = d.replace("'", '"')
            dict_data = json.loads(data_list)
            for data_item in dict_data:
                shop_name = data_item['网店名称']
                company = data_item['归属企业']
                company_addres = data_item['企业注册地']
                if 'shop'in company_addres:
                    province = ''
                    city = ''
                    county = ''
                elif len(company_addres) < 4:
                    province = ''
                    city = ''
                    county = ''
                else:
                    province = company_addres[0:3]
                    city = company_addres[3:6]
                    county = company_addres[6:9]
                data_l = [shop_name, company, company_addres, province, city, county]
                data_name.write(','.join(data_l) + '\n')


if __name__ == '__main__':
    run_data()








