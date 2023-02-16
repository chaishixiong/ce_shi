import requests
import json
import js2py
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import life_227_pool


class MTWenZhouData(object):
    def __init__(self):
        self.session_227_life = DataBaseSession(life_227_pool)

    def request_get(self):
        url = 'https://wz.meituan.com/meishi/api/poi/getPoiList?cityName=%E6%B8%A9%E5%B7%9E&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=37&userId=603449349&uuid=a863d4a8c5dc4f849c52.1655360106.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fwz.meituan.com%2Fmeishi%2Fpn37%2F&riskLevel=1&optimusCode=10&_token=eJyFj0tvozAUhf%2BLt6BgwjtSF03JUMBpIUkJdDQLYkhwCI%2FE5hGq%2Be%2FjatrFrEa60jn%2B7tHR9Qe4uRlYyBBaEIqgz29gAeQZnOlABIzyja5puqWoqmWqsgjwv8ySVREcbpENFj9law5FZQ5%2FfZINB3%2BJDE2Ovr3K%2FVzl85lyeQgUjLV0IUnDNKtywrq0nuGmkrinBZHaWjEkfsp%2FU7oEeGW145Vcyy9Nv5R9v9f8e7yOklPNXe4Nl2nHusf7Klm%2BPhmdb5dJRExHLQkuYg932HaDgjX3IRgS4SzYdodVVIa01MJ2c%2B0rF1JjFRkuVWqbINMVHg2ID8NxNI%2FxKAXNKfDfnjNNMwbn4LzatPwRCiOrJ5gMb1WnbtD2mhoVuZzT1fylz8amSFDudcX0jhF1ohbhdYToMpnwOR3UolGS9OLtiZDhZnTKon%2FXT8uODnc5fvFDRXjuo%2FjpKm%2FRPlSatZKxw9afOuO%2BY3LNYtISGOXttdQa7%2BYTUh%2BDNVruI9SeHh7A7z812KMH'
        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "_lxsdk_cuid=1813801294bc8-0906b807eb0f9c-15373079-240000-1813801294bc8; iuuid=D6B9594FAFD20A1CF6E486AE0D90B18DC9452B5933C4FC05C3DE444FC87FED1B; cityname=%E4%B8%8A%E6%B5%B7; _lxsdk=D6B9594FAFD20A1CF6E486AE0D90B18DC9452B5933C4FC05C3DE444FC87FED1B; ci=112; rvct=112%2C10; uuid=a863d4a8c5dc4f849c52.1655360106.1.0.0; mtcdn=K; userTicket=zFVobdmuOTNjNiCxaNZjxqknEGZNwGlAmtTImKKS; firstTime=1655360559655; __mta=250902841.1654506843112.1654592194793.1655367807970.6; client-id=1176d2ec-f896-4341-80e7-c5def33c737b; u=603449349; n=HfU164403759; lt=SDQUNF1ys1kc0ZjibrthCPWHgP0AAAAASRIAAOuEPl-iDUDPgPs1hgTuoHV2gChrkt0B46BU5BrGhg96OO5qdqgQQGeWKszu8voEcA; mt_c_token=SDQUNF1ys1kc0ZjibrthCPWHgP0AAAAASRIAAOuEPl-iDUDPgPs1hgTuoHV2gChrkt0B46BU5BrGhg96OO5qdqgQQGeWKszu8voEcA; token=SDQUNF1ys1kc0ZjibrthCPWHgP0AAAAASRIAAOuEPl-iDUDPgPs1hgTuoHV2gChrkt0B46BU5BrGhg96OO5qdqgQQGeWKszu8voEcA; _lxsdk_s=1817ea871a3-77b-0e8-a91%7C%7C13; token2=SDQUNF1ys1kc0ZjibrthCPWHgP0AAAAASRIAAOuEPl-iDUDPgPs1hgTuoHV2gChrkt0B46BU5BrGhg96OO5qdqgQQGeWKszu8voEcA",
            "Host": "wz.meituan.com",
            "Referer": "https://wz.meituan.com/meishi/",
            "Sec-Fetch-Dest": "empty"
        }
        request = requests.get(url=url, headers=headers)
        data_text = request.content.decode()
        return data_text

    def json_data(self, json_data):
        poiInfos_list = json_data['data']['poiInfos']
        for item in poiInfos_list:
            shop_id = item['poiId']  # 店铺id
            shop_name = item['title']  # 店铺名称
            avg_score = item['avgScore']  # 店铺评分
            all_comment_num = item['allCommentNum']  # 店铺评论数
            address = item['address']  # 店铺地址
            avg_price = item['avgPrice']  # 人均
            category = ''
            data_list = [shop_id, shop_name, avg_score, all_comment_num, address, avg_price, category]
            self.insertion_data(data_list)
            print(data_list)

    def insertion_data(self, data_list):
        insertion_sql = "insert into meituan_wenzhou (shop_id, shop_name, avg_score, all_comment_num, address, avg_price, category) VALUES (%s,%s,%s,%s,%s,%s,%s)"

        # 插入库名： session_227_life
        self.session_227_life.insertion_data(insertion_sql, data_list)

    def run_spider(self):
        response_data = self.request_get()
        try:
            json_data = json.loads(response_data)
            self.json_data(json_data)
        except Exception as e:
            if '抱歉，页面暂时无法访问' in response_data:
                print('抱歉，页面暂时无法访问')
            else:
                print(e)

    def demo(self, url):
        with open('wn_mt_js.js', 'r', encoding='utf-8') as f:
            aa = f.read()
        js_env = js2py.eval_js(aa)
        ss = js_env.Rohr_Opt.reload("https://wz.meituan.com/meishi/api/poi/getPoiList?cityName=温州&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=1&userId=603449349&uuid=560b2538a3d045f9aa27.1654502007.1.0.0&platform=1&partner=126&originUrl=https://wz.meituan.com/meishi/&riskLevel=1&optimusCode=10")
        token = js_env.call("GetToken", url)
        return token


def run_mt_wenzhou_spider():
    url = "https://wz.meituan.com/meishi/api/poi/getPoiList?cityName=温州&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=1&userId=603449349&uuid=560b2538a3d045f9aa27.1654502007.1.0.0&platform=1&partner=126&originUrl=https://wz.meituan.com/meishi/&riskLevel=1&optimusCode=10"
    run_mt_wz = MTWenZhouData()
    run_mt_wz.run_spider()


if __name__ == '__main__':
    run_mt_wenzhou_spider()



