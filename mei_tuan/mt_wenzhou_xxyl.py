import requests
import json
import js2py
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import life_227_pool

county_id = {
    59: "西湖区",
    57: "拱墅区",
    5225: "萧山区",
    60: "滨江区",
    2779: "余杭区",
    55: "上城区",
    2780: "临安市",
    2781: "富阳区",
    2783: "桐庐县",
    56: "钱塘区",
    58: "临平区",
    2782: "建德市",
    2784: "淳安县"
}


class MTWenZhouData(object):
    def __init__(self):
        self.session_227_life = DataBaseSession(life_227_pool)
        self.total_count = 0
        self.county_id = 0
        self.run_spdir = False

    def request_get(self, offset_num, county_id):
        url = 'https://meishi.meituan.com/i/api/channel/deal/list'
        headers = {
            "Accept": "application/json",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Cookie": "__mta=218035113.1657691148681.1658131692986.1658801209976.112; _lxsdk_cuid=1813801294bc8-0906b807eb0f9c-15373079-240000-1813801294bc8; rvct=186%2C10; iuuid=2F4484CA879600DDB829E897F4EFC505379128AE0F50E6F2F60F010E77621B8B; _lxsdk=2F4484CA879600DDB829E897F4EFC505379128AE0F50E6F2F60F010E77621B8B; _hc.v=b6acb976-47f3-af25-c56c-0967fcf32ddf.1657695829; webp=1; _ga=GA1.1.952985750.1657696795; _ga_LYVVHCWVNG=GS1.1.1657768090.1.1.1657768101.0; __utmz=74597006.1657874791.4.2.utmcsr=meishi.meituan.com|utmccn=(referral)|utmcmd=referral|utmcct=/; mtcdn=K; IJSESSIONID=node0zgzasoc8w6jv1o3bq06d41ffe104320337; ci3=50; __utmc=74597006; __utma=74597006.952985750.1657696795.1658126720.1658800947.7; WEBDFPID=w3613x08y2x452801y02zuz3z466xzx8817616u40899795822x8569v-1658887452468-1658801051912CMKQMOIfd79fef3d01d5e9aadc18ccd4d0c95073716; client-id=f94bfa7b-1536-4182-a3ae-eeb80566c69e; ndr=i.meituan.com; a2h=1; cssVersion=22f790f1; wm_order_channel=mtib; utm_source=60030; request_source=openh5; au_trace_key_net=default; _lx_utm=utm_source%3D60030; uuid=2F4484CA879600DDB829E897F4EFC505379128AE0F50E6F2F60F010E77621B8B; openh5_uuid=2F4484CA879600DDB829E897F4EFC505379128AE0F50E6F2F60F010E77621B8B; isIframe=false; logan_session_token=bmdth792cq1sujmjdoaz; latlng=30.365373,120.233771,1658802039143; ci=50; cityname=%E6%9D%AD%E5%B7%9E; __utmb=74597006.17.9.1658802084049; i_extend=C_b1Gimthomepagecategory11H__a; _lxsdk_s=182383d3722-be3-dc9-4e1%7C%7C85; meishi_ci=50; cityid=50",
            "Origin": "https://meishi.meituan.com",
            "Referer": "http://meishi.meituan.com/i/?ci=45&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
            "sec-ch-ua": 'Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "Android",
            "x-requested-with": "XMLHttpRequest"
        }
        data = {
              "platform": 3,
              "partner": 126,
              "riskLevel": 1,
              "optimusCode": 10,
              "limit": 50,  # 没次请求量
              "cateId": 1,  # 美食类目ID
              "areaId": county_id,  # 区
              "offset": offset_num,  # 商品数量
              # "offset": 950,  # 商品数量
            }
        request = requests.post(url=url, headers=headers, data=json.dumps(data))
        return request

    def json_data(self, item):
        shop_id = item['poiid']  # 店铺id
        shop_name = item['name']  # 店铺名称
        avg_score = item['avgScore']  # 店铺评分
        all_comment_num = 0  # 店铺评论数
        address = item['areaName']  # 店铺地址
        avg_price = item['avgPrice']  # 人均
        category = '美食'
        province = '浙江省'
        city = '杭州市'
        county = self.county
        street = self.regionName
        data_list = [shop_id, shop_name, avg_score, all_comment_num, address, avg_price, category, province, city, county, street]
        self.open_write(data_list)
        # self.insertion_data(data_list)
        # print(data_list)

    def insertion_data(self, data_list):
        insertion_sql = "insert into meituan_wenzhou_new_copy1 (shop_id, shop_name, avg_score, all_comment_num, address, avg_price, category, province, city, county, street) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        # 插入库名： session_227_life
        self.session_227_life.insertion_data(insertion_sql, data_list)

    def select_sql(self):
        select_sql = "select shop_id, shop_name, avg_score, all_comment_num, address, avg_price, category, province, city, county, street from meituan_wenzhou_new where shop_id <> '' GROUP BY shop_id"
        data_list = self.session_227_life.query_tuple_data(select_sql)
        for data in data_list:
            data_l = list(data)
            self.insertion_data(data_l)

    def run_spider(self, county_id):
        offset_num = 0
        self.county_id = county_id
        while True:
            if offset_num > self.total_count:
                break
            response_data = self.request_get(offset_num, county_id)
            offset_num += 50
            try:
                json_data = json.loads(response_data.text)
                if json_data.get('code') == 406:
                    break
                poi_list = json_data['data']['poiList']
                total_count = poi_list.get('totalCount')
                poiInfos_list = poi_list.get('poiInfos')
                if total_count == 0 and len(poiInfos_list) == 0:
                    break
                for item in poiInfos_list:
                    self.json_data(item)
            except Exception as e:
                if '抱歉，页面暂时无法访问' in response_data:
                    print('抱歉，页面暂时无法访问')
                else:
                    print(e)

    def open_write(self, data_list):
        with open('data_data.txt', 'a', encoding='utf-8') as wf:
            wf.write(','.join(data_list + '\n'))
            wf.flush()

    def demo(self):
        with open('areaId.txt', 'r', encoding='utf-8') as f:
            data_dict = f.read()
        js_env = json.loads(data_dict)
        area_obj_list = js_env['navBarData']['areaObj']
        return area_obj_list

    def for_data_id(self):
        area_obj_list = self.demo()
        for area_obj in area_obj_list:
            area_id_list = area_obj_list[area_obj]
            for area_id in area_id_list:
                id = area_id['id']
                name = area_id['name']
                regionName = area_id['regionName']
                self.total_count = area_id['count']
                if name == '全部':
                    self.county = regionName
                else:
                    self.regionName = regionName
                    street_street = self.county + self.regionName + str(self.total_count)
                    if street_street == "拱墅区北部新城558":
                        self.run_spdir = True
                    if self.run_spdir == True:
                        self.run_spider(id)


def run_mt_wenzhou_spider():
    run_mt_wz = MTWenZhouData()
    run_mt_wz.select_sql()


if __name__ == '__main__':
    run_mt_wenzhou_spider()



