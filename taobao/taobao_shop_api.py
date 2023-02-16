# -*- coding: utf-8 -*-

import time
from typing import Dict
import requests

import json
from urllib.parse import quote


def timer(function):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        res = function(*args, **kwargs)
        cost_time = time.time() - time_start
        print("【%s】运行时间：【%s】秒" % (function.__name__, cost_time))
        return res

    return wrapper


def dict_encode(param_dict):
    return json.dumps(param_dict, separators=(',', ':'))


class TBBaseClass():
    xsign_url = "xxxxxx"  # 测试链接，如需测试，请联系QQ获取。+Q: 251273504
    serverg = "tb910"
    servera = "tbxsign"

    def random_lat_lng(self):
        return {"lng": "0", "lat": "0"}

    def random_device_info(self):
        device_info = {
            "user-agent": 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Xiaomi 8 Build/OPM1.171019.011)',
            # "deviceId": 'xxxx',
            "appKey": "21646297",
            # "utdid": 'xxxxxxx',
            "ttid": "1628000524142@taobao_android_9.1.0",
        }
        return device_info

    def get_xsign(self, params):
        params["group"] = self.serverg
        params["action"] = self.servera
        try:
            response = requests.post(
                self.xsign_url,
                json=params,
                verify=False,
                timeout=3
            )
            res = response.json()
            result = res["data"]
            if "x-sign" not in result.keys():
                print({'error': f'调用x-sign接口失败., result: {result}'})
                return None
            return result
        except Exception as e:
            import traceback
            traceback.print_exc()
            print({'error': f'调用x-sign接口异常. {e}'})
            return None

    @staticmethod
    def get_header(params, x_sign_data):
        headers = {
            "x-features": params.get("x-features"),
            "x-pv": "6.3",
            "x-sgext": "923",
            "x-location": ",".join([params.get("lng"), params.get("lat")]),
            "user-agent": params.get("user-agent"),  # quote(params.get("user-agent"), safe="+"),
            "x-ttid": params.get("ttid"),
            "x-appkey": params.get("appKey"),
            "x-devid": params.get("deviceId"),
            "x-utdid": params.get("utdid"),
            "x-t": params.get("timestamp")[:10],
            "x-uid": params.get("uid"),
            "x-sid": params.get("sid"),
            "x-umt": quote(x_sign_data.get("x-umt"), safe=''),
            "x-mini-wua": quote(x_sign_data.get("x-mini-wua"), safe=''),
            "x-sign": quote(x_sign_data.get("x-sign"), safe=''),
            'x-bx-version': '6.4.11',
            'Host': 'guide-acs.m.taobao.com',
        }
        return headers

    def get_x_sign_data(self, params):
        sign_params = {
            "deviceId": params.get("deviceId"),
            "appKey": params.get("appKey"),
            "extdata": params.get("extdata"),
            "utdid": params.get("utdid"),
            "x-features": params.get("x-features"),
            "ttid": params.get("ttid"),
            "v": params.get("v"),
            "sid": params.get("sid"),
            "t": params.get("timestamp")[:10],
            "api": params.get("api"),
            "data": params.get("data"),
            "uid": params.get("uid"),
            "lng": params.get("lng"),
            "lat": params.get("lat"),
            "pageName": params.get("pageName"),
            "pageId": params.get("pageId"),
        }
        x_sign_data = self.get_xsign(sign_params)
        return x_sign_data

    @staticmethod
    def prepare_params(features, v, api, page_name, page_id, data, device_info, lat_lng_info, user_cookie) -> Dict:
        timestamp = str(int(time.time() * 1000000))
        sid = user_cookie.get("cookie2", "")
        uid = user_cookie.get("unb", "")
        params = {
            "x-features": features,
            "v": v,
            "api": api,
            "pageName": page_name,
            "pageId": page_id,
            "deviceId": device_info.get("deviceId"),
            "appKey": device_info.get("appKey"),
            "extdata": device_info.get("extdata"),
            "utdid": device_info.get("utdid"),
            "ttid": device_info.get("ttid"),
            "lng": lat_lng_info.get("lng"),
            "lat": lat_lng_info.get("lat"),
            "sid": sid,
            "uid": uid,
            "data": data,
            "timestamp": timestamp,
        }
        return params

    def get_shop_all_items_data(self, seller_id, shop_id, page):
        data = dict_encode({
            'LBS': '{"SG_TMCS_1H_DS":"xxxxxxxxxxx"}',
            '_inNestedEmbed': 'true',
            '_page_home_isweex_': 'true',
            '_page_inside_embed_': 'true',
            '_useless1': '1',
            '_wx_f_': '1',
            '_wx_shop_render_activity': 'true',
            'active_bd': '1',
            'features': '{}',
            'info': 'wifi',
            'isFlagship': '1',
            'isMiniApp': 'false',
            'isWeexShop': 'true',
            'item_id': '627624856025',
            'm': 'shopitemsearch',
            'miniAppCategoryUrl': '',
            'miniAppDetailUrl': '',
            'n': '10',
            'network': 'wifi',
            'new_shopstar': 'true',
            'page': f'{page}',
            'pre_item_id': '627624856025',
            'searchFramework': 'true',
            'search_wap_mall': 'false',
            'sellerId': f'{seller_id}',
            'setting_on': 'imgBanners,userdoc,tbcode,pricerange,localshop,smartTips,firstCat,dropbox,realsale,insertTexts,tabs',
            'shopFetchTimeout': '200',
            'shopFrameRenderTimestamp': '1621927466956',
            'shopId': f'{shop_id}',
        })
        return data

    def get_shop_all_items(self, seller_id, shop_id, page):
        features = "27"
        api = "mtop.taobao.wsearch.appsearch"
        v = "1.0"
        page_name = "com.taobao.android.shop.activity.ShopRenderActivity"
        page_id = "http%3A%2F%2Fh5.m.taobao.com%2Fweex%2Fviewpage.htm"
        api_url = f"http://guide-acs.m.taobao.com/gw/{api}/{v}/"
        lat_lng_info = self.random_lat_lng()
        device_info = self.random_device_info()
        user_cookie = {}
        data = self.get_shop_all_items_data(seller_id, shop_id, page)
        params = self.prepare_params(features, v, api, page_name, page_id, data, device_info, lat_lng_info, user_cookie)
        x_sign_data = self.get_x_sign_data(params)
        params["user-agent"] = device_info["user-agent"]
        headers = self.get_header(params, x_sign_data)
        return api_url, data, headers, user_cookie

    def test_shop_all_items(self, seller_id, shop_id, page):
        api_url, data, headers, cookie = self.get_shop_all_items(seller_id, shop_id, page)
        params = {"data": data}
        try:
            response = requests.get(api_url, params=params, headers=headers, cookies=cookie, timeout=3, verify=False)
        except:
            return None
        return response


@timer
def test_shop_items(seller_id, shop_id):
    obj = TBBaseClass()
    totalPage = None
    for page in range(1, 100):
        if totalPage is not None and page > totalPage:
            break
        while True:
            res = obj.test_shop_all_items(seller_id, shop_id, page)
            if res.status_code == 200:
                totalPage = int(res.json()["data"]["totalPage"])
                t_page = int(res.json()["data"]["page"])
                totalResults = int(res.json()["data"]["totalResults"])
                item_ids = [i["item_id"] for i in res.json()["data"]["itemsArray"]]
                print(f"店铺商品总数:{totalResults}, 总页数:{totalPage}, 当前页数:{t_page}, item_ids:{item_ids}", )
                break
            else:
                continue


seller_id = "3948263976"
shop_id = "251740197"
test_shop_items(seller_id, shop_id)