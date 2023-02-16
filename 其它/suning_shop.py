import requests
import json
from sql.mysqlhelper import MySqLHelper


def request(shop_id):
    url = "https://salav.suning.com/jsonp/{}/shopinfo/shopinfo.html?callback=shopinfo".format(shop_id)
    headers = {
        "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
        "sec-ch-ua-mobile": "?0",
        "x-requested-with": "XMLHttpRequest"
    }
    r = requests.get(url, headers=headers)
    data = r.content.decode()
    item = data.replace('shopinfo(', '').replace(')', '')
    item_item = json.loads(item)
    item_dict(item_item)


def item_dict(item_dict):
    item = dict()
    item['shop_id'] = item_dict.get('shopId')
    item['shop_name'] = item_dict.get('shopName')
    item['company'] = item_dict.get('companyName')
    item['address'] = item_dict.get('companyAddress')
    item['logistics_score'] = item_dict.get('Astar')
    item['product_score'] = item_dict.get('Qstar')
    item['service_score'] = item_dict.get('Dstar')
    item['logistics_percent'] = str(int(float(item_dict.get('Astar')) * 10)) + '%' if item_dict.get('Astar') else 0
    item['telPhone'] = item_dict.get('telPhone')
    item['countryName'] = item_dict.get('countryName')
    item['companyProvince'] = item_dict.get('companyProvince')
    item['companyCity'] = item_dict.get('companyCity')
    item['shopDomain'] = item_dict.get('shopDomain')
    item['main_sale'] = ''
    item['main_sale_count'] = '0'
    item['main_sale_all'] = ''
    item['main_sale_top5'] = ''
    item_value = item.values()
    str_s = str(item_value).replace("'", '').replace(' ', '').replace('dict_values([', '').replace('])', '')
    with open('suning.txt', 'a', encoding='utf-8')as f:
        f.write(str_s + '\n')
    print(item_value)


def open_sql(sql, param=None):
    db = MySqLHelper()
    if param:
        ret = db.selectone(sql=sql, param=None)
    else:
        ret = db.selectone(sql=sql)
    for id in ret:
        shop_id = id[0]
        request(shop_id)


if __name__ == '__main__':
    # request('70100331')
    sql = 'select shop_id from suning_shopinfo_202102'
    open_sql(sql)
