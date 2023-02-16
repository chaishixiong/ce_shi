#!/usr/bin/env python
# -*- coding:utf-8 -*-

import js2py
import os
import re
import time
import threading
import execjs
import requests
import json
import redis
import socket,re
mutex = threading.Lock()


def get_ip():
    addrs = socket.getaddrinfo(socket.gethostname(), "")
    match = re.search("'192.168.(\d+.\d+)'", str(addrs))
    ip_num = "0.000"
    if match:
        ip_num = match.group(1)
    return ip_num

def if_ip():
    if get_ip() in ["9.10","9.11","9.42","9.127","9.128","10.101","10.102","10.103","10.104","10.105","10.106","10.100","9.97","9.95","9.122","9.68","9.100"]:
        USER_NAME = "057762355592"
        PASSWORD = "928858"
    elif get_ip() == "9.123":
        USER_NAME = "wzlcb57746616"
        PASSWORD = "123456"
    elif get_ip() == "9.124":
        USER_NAME = "wzlcf57746616"
        PASSWORD = "123456"
    elif get_ip() == "9.125":
        USER_NAME = "wzlcg57746616"
        PASSWORD = "123456"
    elif get_ip() == "9.126":
        USER_NAME = "wzlcc57746616"
        PASSWORD = "123456"
    elif get_ip() in ["9.148","9.149","9.170","9.171","9.172","9.173"]:
        USER_NAME = "057764473605"
        PASSWORD = "744523"
    else:
        USER_NAME = "057762355594"#9.100 9.99 9.98 0.56 0.59 9.129
        PASSWORD = "045805"
    if get_ip() == "0.226" or get_ip() == "7.144":
        USER_NAME = "null"
        PASSWORD = "null"
    return USER_NAME, PASSWORD

'''<class 'dict'>: {'_m_h5_tk': '3183ad262c286ca290f39883b94b2c95_1623924818882', '_m_h5_tk_enc': 'b6099178d60d7688fde0e3b8694b2e88'}'''
class TbTM618(object):
    def __init__(self):
        with open(r"taobao_sign.js", encoding='utf-8') as f:
            self.cx = f.read()
        self.cookie = 'cna=HDhDE5soETwCAXPa4gThuY+A; cookie2=5ffc6896fae561ae0ea98c26191dbab5; v=0; _tb_token_=377eb6b634117; _samesite_flag_=true; existShop=MTU5NTMzNDAzNg%3D%3D; _cc_=VFC%2FuZ9ajQ%3D%3D; ockeqeudmj=gOP57ic%3D; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BuCTNvlJkGJJJFSIzUzDgsGKQKMYyNwg%3D; _w_app_lg=0; sgcookie=E100sCLKfcQQsT%2FybGOKPvDWji7YqILLJW%2FxENAXvKv%2BctA0z%2BgYSCpK1M8hhVD6%2B47P%2BTaUea9ZxwY%2FLXcIbCSFtA%3D%3D; csg=f8a71ffd; dnk=%5Cu4E09%5Cu9014%5Cu6CB3%5Cu8FD8%5Cu662F%5Cu5929%5Cu5802; skt=baec8ab48c0cc721; tracknick=%5Cu4E09%5Cu9014%5Cu6CB3%5Cu8FD8%5Cu662F%5Cu5929%5Cu5802; uc1=cookie14=Uoe0bkpV%2FUv7cQ%3D%3D&existShop=false&cookie21=UtASsssmeW6lpyd%2BB%2B3t&pas=0&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D; isg=BKys-re24LQQTMtVa7r83EYOfYreZVAPWH_3FAbtm9f6EU0bLnTdnPDgNdmpmYhn'
        self.data = '{"detail_v":"3.5.0","exParams":"{\"appReqFrom\":\"detail\",\"container_type\":\"xdetail\",\"dinamic_v3\":\"true\",\"supportV7\":\"true\",\"ultron2\":\"true\"}","itemNumId":"%s","pageCode":"miniAppDetail","_from_":"miniapp"}'
        self._m_h5_tk_first = 'undefined'
        self.url = 'https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/?jsv=2.6.1&appKey=12574478&t={}&sign={}&api=mtop.taobao.detail.getdetail&v=6.0&ttid=202012%40taobao_h5_9.17.0&isSec=0&ecode=0&AntiFlood=true&AntiCreep=true&H5Request=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data=%7B%22detail_v%22%3A%223.5.0%22%2C%22exParams%22%3A%22%7B%5C%22appReqFrom%5C%22%3A%5C%22detail%5C%22%2C%5C%22container_type%5C%22%3A%5C%22xdetail%5C%22%2C%5C%22dinamic_v3%5C%22%3A%5C%22true%5C%22%2C%5C%22supportV7%5C%22%3A%5C%22true%5C%22%2C%5C%22ultron2%5C%22%3A%5C%22true%5C%22%7D%22%2C%22itemNumId%22%3A%22{}%22%2C%22pageCode%22%3A%22miniAppDetail%22%2C%22_from_%22%3A%22miniapp%22%7D'
        self.time_dd = ''
        self.username, self.password = if_ip()
        self.redisPool = redis.Redis(host='192.168.0.225', port=5208, db=0, decode_responses=True)
        self.error_key = "tm_618_goods:error_url"

    def get_sign(self, data):
        ctx = execjs.compile(self.cx)
        self.time_dd = str(int(time.time() * 1000))
        sign_str = self._m_h5_tk_first + "&" + self.time_dd + "&" + "12574478" + "&" + data
        sign = ctx.call("get_sign_demo", sign_str)
        return sign

    def request(self, sign, goods_id):
        url = self.url.format(self.time_dd, sign, goods_id)
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "script",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-site",
            "authority": "h5api.m.taobao.com",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
            "referer": "https://h5.m.taobao.com/",
            "cookie": self.cookie
        }
        r = requests.get(url=url, headers=headers)
        return r

    def connect(self):
        name = "宽带连接"
        username = self.username
        password = self.password
        cmd_str = "rasdial %s %s %s" % (name, username, password)
        res = os.system(cmd_str)
        if res == 0:
            print("连接成功")
            return "成功"
        else:
            print("连接失败")
            return "失败"

    def disconnect(self):
        name = "宽带连接"
        cmdstr = "rasdial %s /disconnect" % name
        os.system(cmdstr)
        print('断开成功')

    def huan_ip(self):
        # 断开网络
        self.disconnect()
        # 开始拨号
        a = self.connect()
        return a

    def process_item(self, respones):
        item = dict()
        match = re.search("mtopjsonp1\((.*)\)", respones.text)
        json_str = match.group(1)
        json_data = json.loads(json_str)
        mark_1 = re.search("(满200减30)", json_str)
        mark_2 = re.search("(满199减20)", json_str)
        mark_3 = re.search("(跨店)", json_str)
        if mark_1 is not None:
            mark = mark_1.group(1)
        elif mark_2 is not None:
            mark = mark_2.group(1)
        else:
            mark = ''
        if mark_3 is not None:
            mark2 = '跨店'
        else:
            mark2 = ''
        item['goods_id'] = json_data['data']['item']['itemId']
        item['mark'] = mark
        item['mark2'] = mark2
        with open('W:\scrapy_xc\{taobao_618_logo}.txt', 'a', encoding='utf-8')as f:
            for i in item.values():
                f.write(i + ',')
            f.write('\n')
        return item

    def redis_list(self):
        goods_id = self.redisPool.spop('tm_618_goods:request_goods')
        return goods_id

    def cookies_generate(self, goodid):
        url = "https://h5api.m.taobao.com/h5/mtop.taobao.baichuan.smb.get/1.0/?jsv=2.6.1&appKey={}&t={}&sign={}&api=mtop.taobao.baichuan.smb.get&v=1.0&type=originaljson&dataType=jsonp&timeout=10000"
        time_now = str(int(time.time() * 1000))
        appkey = "12574478"
        data = '{}'
        sign = self.get_sign(data)
        url = url.format(appkey, time_now, sign)
        data1 = {"pageCode":"mainDetail","ua":"Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Mobile Safari/537.36 Edg/86.0.622.48","params":"{\"url\":\"https://h5.m.taobao.com/awp/core/detail.htm?id=%s\",\"referrer\":\"\",\"oneId\":null,\"isTBInstalled\":\"null\",\"fid\":\"dSnxbHpDSQi\"}" % goodid}
        headers = {'Host': 'h5api.m.taobao.com', 'Connection': 'keep-alive',
                   'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Mobile Safari/537.36 Edg/86.0.622.48',
                   'Accept': '*/*', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'no-cors',
                   'Sec-Fetch-Dest': 'script', 'Referer': 'https://h5.m.taobao.com/',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        try:
            req = requests.post(url=url, headers=headers, data=data1)
            headers_rep = req.headers
            set_cookiesstr = headers_rep.get("set-cookie")
            set_cookies = self.reqhead_split(set_cookiesstr)
            cookies_dict = dict()
            cookies_dict["_m_h5_tk"] = set_cookies.get("_m_h5_tk", "")
            cookies_dict["_m_h5_tk_enc"] = set_cookies.get("_m_h5_tk_enc", "")
            if cookies_dict.get("_m_h5_tk") and cookies_dict.get("_m_h5_tk_enc"):
                return cookies_dict
        except Exception as e:
            print(e)
            pass

    def reqhead_split(self, headers_str):
        b = re.sub("(expires=[^,]*),", "\\1，", headers_str, flags=re.I)
        h_list = b.split(",")
        dict_p = {}
        for str_p in h_list:
            parameter = str_p.split(";")[0]
            parameter_l = parameter.split("=", 1)
            value_p = ""
            if len(parameter_l) > 1:
                value_p = parameter_l[1].strip()
            name_p = parameter_l[0].strip()
            dict_p[name_p] = value_p
        return dict_p

    def run_tb(self):
        while True:
            goods_id = '643349031200'
            data = self.data % goods_id
            sign = self.get_sign(data)
            try:
                respones = self.request(sign, goods_id)
                data_dict = self.process_item(respones)
                print(data_dict)
            except Exception as e:
                # state = self.huan_ip()
                self.redisPool.lpush(self.error_key, goods_id)
                cookies_dict = self.cookies_generate(goods_id)
                self.cookie = self.cookie.format(cookies_dict['_m_h5_tk'], cookies_dict['_m_h5_tk_enc'])
                print(self.cookie)
                print(e)

def open_goods():
    import redis
    with open(r"W:\scrapy_xc\taobao_618_look-data_ll\good_seet.txt", "r",encoding="utf-8") as f:
        goods_str = f.read()
        f.close()
    redisPool = redis.ConnectionPool(host='192.168.0.225', port=5208, db=0, decode_responses=True)
    redis = redis.Redis(connection_pool=redisPool)
    good_list = goods_str.split('\n')
    for goods in good_list:
        redis.sadd('tm_618_goods:request_goods', goods)


def withopen():
    r = TbTM618()
    r.run_tb()


if __name__ == "__main__":
    _m_h5_tk_first = 'undefined'
    time_dd = str(int(time.time() * 1000))
    data = '{"detail_v":"3.5.0","exParams":"{\"appReqFrom\":\"detail\",\"container_type\":\"xdetail\",\"dinamic_v3\":\"true\",\"supportV7\":\"true\",\"ultron2\":\"true\"}","itemNumId":"643349031200","pageCode":"miniAppDetail","_from_":"miniapp"}'
    withopen()
    # open_goods()
