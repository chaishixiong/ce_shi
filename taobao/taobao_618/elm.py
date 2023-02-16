import requests
from fake_useragent import UserAgent
import json
import random
import time
import pymongo

'''
1.记得登录后再写入cookies 
2.因为电脑没有GPS 所以饿了么是通过经度 纬度 来确定你周围的外卖店铺
3.保存到数据库 可以自己做个小程序 查询好吃的 并且通过数据库自带的搜索功能 来搜索好吃的 比如评分最高的 派送费最便宜的或者免费
4.也可以直接写个CSV函数 弄成表格

因为是AJAX请求的 所以简单很多 
因为怕有反爬虫 避免给服务器带来压力 加了休眠

'''

clien=pymongo.MongoClient(host='改成自己的数据库')
db=clien.Hungry
coll=db.text

ua=UserAgent()
headers = {
        'User-Agent':ua.random,
        'cookie':'请先登录后填入登录后的Cookies 因为如果不传这个 只能显示前40条数据 '
    }


def Request_Json(URL):
    try:
        sponse = requests.get(URL, headers=headers).text
        jsons = json.loads(sponse)
        return jsons
    except Exception:
        print('request error')


def fetch_information(json):
    #data['地区']=json.get('address')
    for i in json:
        data = {}
        #print(type(i))
        data['店铺名']=i['name']
        data['地址']=i.get('address')
        data['食品类型']=i.get('support_tags')[0].get('text')
        data['营业时间']=i.get('opening_hours')[0]
        data['配送费']=i.get('piecewise_agent_fee').get('description')
        data['联系电话']=i.get('phone')
        data['起送价']=i.get('float_minimum_order_amount')
        data['店铺的纬度']=i.get('latitude')
        data['店铺的经度']=i.get('longitude')
        data['评分']=i.get('rating')
        data['最近订单数']=i.get('recent_order_num')
        coll.insert_one(data)
        print(data)


for i in range(0,22):
    page=i*24
    URL='https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wkqrwjsr089v&latitude=25.256027&limit=24&longitude=110.308595&offset={}&terminal=web'.format(page)
    #print(URL)
    fetch_information(Request_Json(URL))
    time.sleep(random.randint(0,6))
