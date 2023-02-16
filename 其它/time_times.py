#coding:UTF-8
import time
import requests

# dt = "2004-02-02"
#
# #转换成时间数组
# timeArray = time.strptime(dt, "%Y-%m-%d")
# #转换成时间戳
# timestamp = time.mktime(timeArray)
#
# print(timestamp)
# time_now = str(int(time.time() * 1000))
# print(time_now)

url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?jsv=2.6.1&appKey={}&t={}&sign={}&api=mtop.relationrecommend.WirelessRecommend.recommend&v=2.0&isSec=0&ecode=0&AntiFlood=true&AntiCreep=true&H5Request=true&type=jsonp&dataType=jsonp&callback=mtopjsonp3&data=%7B%22id%22%3A%22{}%22%2C%22appId%22%3A%22766%22%2C%22params%22%3A%22%7B%5C%22itemid%5C%22%3A%5C%22{}%5C%22%2C%5C%22sellerid%5C%22%3A%5C%22{}%5C%22%7D%22%7D'
time_now = '1628653712684'
sign = '174efe615440f5c367470047e4e203da'
appkey = '12574478'
goods_id = '611630153925'
seller_id = '2590418492'
url_q = url.format(appkey, time_now, sign, goods_id,goods_id,seller_id)
headers = {
    'Host': 'h5api.m.taobao.com', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Mobile Safari/537.36 Edg/86.0.622.48', 'Accept': '*/*', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'no-cors', 'Sec-Fetch-Dest': 'script', 'Referer': 'https://h5.m.taobao.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}
params = {"itemid":"611630153925", "spm":"0.0.0.0.hUro0P","sellerid":"2590418492","appId":"10777"}

r = requests.get(url_q, headers=headers, params=params)
data = r.content.decode()
print(data)