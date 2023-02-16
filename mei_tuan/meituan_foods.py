import json
import random
import re
import time
from pymongo import MongoClient
import requests
from lxml import html


class MeituanSpider():
    def __init__(self):
        # 入口url
        self.start_url = 'https://chs.meituan.com/meishi/'
        # 首先需要登录自己的账号上 获取登录后的Cookie信息和User-Agent来构造响应头
        self.headers = {
            # 修改成自己的cookie
            "Cookie": "_lxsdk_cuid=1813801294bc8-0906b807eb0f9c-15373079-240000-1813801294bc8; ci3=50; uuid=849972e6d11a47798b6a.1657695643.1.0.0; client-id=5d3ee733-c3d3-4f53-a2fa-50307a366dee; mtcdn=K; userTicket=AlkRXEgDTFIgrEiYcEOTNTUmrFvMYyeeOztIpZWI; rvct=186%2C10; p_token=FtO35xaCmlO6F-BF_FJsCZfxV7gAAAAAvRIAAFbiuBHLpuK7WauM1QB8WxMj35KIMJ0XB4qUyYHiQb6F6hq-n9bObRmr_f5owvcfKA; IJSESSIONID=node01gkls04p27qbsanf9707ksyy381629743; iuuid=2F4484CA879600DDB829E897F4EFC505379128AE0F50E6F2F60F010E77621B8B; _lxsdk=2F4484CA879600DDB829E897F4EFC505379128AE0F50E6F2F60F010E77621B8B; _hc.v=b6acb976-47f3-af25-c56c-0967fcf32ddf.1657695829; webp=1; __utmz=74597006.1657696795.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=74597006; meishi_ci=112; cityid=112; latlng=30.301067,120.215945,1657761837194; __utma=74597006.952985750.1657696795.1657696795.1657761837.2; ci=50; cityname=%E6%9D%AD%E5%B7%9E; i_extend=H__a100002__b2; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; WEBDFPID=7772y4y3vwxv5287z289v507u36u63zu818uz2529699795817502684-1657850745220-1657764343331EMEQUGUfd79fef3d01d5e9aadc18ccd4d0c95071035; lat=30.252616; lng=120.137612; __mta=19110407.1654502012684.1657763821745.1657764406266.9; _gid=GA1.2.254601901.1657768090; _ga=GA1.1.952985750.1657696795; _ga_LYVVHCWVNG=GS1.1.1657768090.1.1.1657768101.0; u=603449349; n=HfU164403759; lt=cUFIS9yPpNVNzjr-vZOIWYKr-EYAAAAAzhIAAGOpkhm3MEQ378ffyUizXT8llNFtCRk0JNCK8VTFAQ74WPn2qrQHiEq999MFD449sQ; mt_c_token=cUFIS9yPpNVNzjr-vZOIWYKr-EYAAAAAzhIAAGOpkhm3MEQ378ffyUizXT8llNFtCRk0JNCK8VTFAQ74WPn2qrQHiEq999MFD449sQ; token=cUFIS9yPpNVNzjr-vZOIWYKr-EYAAAAAzhIAAGOpkhm3MEQ378ffyUizXT8llNFtCRk0JNCK8VTFAQ74WPn2qrQHiEq999MFD449sQ; token2=cUFIS9yPpNVNzjr-vZOIWYKr-EYAAAAAzhIAAGOpkhm3MEQ378ffyUizXT8llNFtCRk0JNCK8VTFAQ74WPn2qrQHiEq999MFD449sQ; firstTime=1657768393360; unc=HfU164403759; _lxsdk_s=181faa9704e-94a-b5d-bb3%7C%7C13",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        }


    # 获取需要爬取的url列表
    def get_url_list(self, url, total_nums):
        url_temp = url + 'pn{}/'
        # 每一页显示显示15个美食  通过获取到每个分类下的总美食数来求出总页数
        pages = total_nums // 15 + 1 if total_nums % 15 != 0 else total_nums // 15
        url_list = [url_temp.format(i) for i in range(1, pages + 1)]
        return url_list

    # 对url进行请求并返回处理后的响应信息
    def parse_url(self, url):
        # self.headers['Cookie'] = random.choice(self.cookies)
        time.sleep(1)
        rest = requests.get(url, headers=self.headers)
        html_str = re.findall(r'window._appState = (.*?);</script>', rest.content.decode())[0]
        return html_str

    # 创建item并进行存储
    def get_content_list(self, html_str, item):
        json_html = json.loads(html_str)
        foods = json_html['poiLists']['poiInfos']
        for i in foods:
            item['food_id'] = i['poiId']
            item['food_url'] = "https://www.meituan.com/meishi/{}/".format(item['food_id'])
            item['title'] = i['title']
            item['avg_score'] = i['avgScore']
            item['avg_price'] = i['avgPrice']
            item['comments'] = i['allCommentNum']
            item['area'] = i['address'][0:3]
            item['address'] = i['address']
            print(item)

    # 主方法
    def run(self):
        # 首先请求入口url来获取每一个美食分类的url地址
        # 请看图例一
        html_str = requests.get(self.start_url, headers=self.headers)
        # 代码已经改变
        # html_str = html.etree.HTML(html_str.content.decode())
        # cate_list = html_str.xpath('//div[text()="分类"]/../ul/li')[1:]
        str_html = re.findall(r'window._appState = (.*?);</script>', html_str.content.decode())[0]
        json_html = json.loads(str_html)
        cate_list = json_html['filters']['cates'][1:]
        item_list = []

        # 对每一个分类进行分组分别获取美食的分类名和美食的分类的url
        for i in cate_list:
            item = {}
            # 分类的url进行反爬处理
            # 从网页中获取的url地址为 http://wx.meituan.com/meishi/c11/
            # 实际url地址为 https://wx.meituan.com/meishi/c11/
            # 因此需要将http替换成https
            # cate_url= i.xpath('./a/@href')[0]
            cate_url = i['url']
            item['cate_url'] = cate_url.replace('http', 'https')
            # item['cate_name'] = i.xpath('./a/text()')[0]
            item['cate_name'] = i['name']
            item_list.append(item)
        # 对每一个美食分类的分类名和分类url地址进行遍历并分别进行处理
        for i in item_list:
            # 睡眠1秒防止被识别为网络爬虫
            time.sleep(1)
            rest = requests.get(i['cate_url'], headers=self.headers)
            str_html = rest.content.decode()
            str_html = re.findall(r'window._appState = (.*?);</script>', str_html)[0]
            json_html = json.loads(str_html)
            total_nums = json_html['poiLists']['totalCounts']
            url_list = self.get_url_list(i['cate_url'], total_nums)
            for url in url_list:
                list_html = self.parse_url(url)
                self.get_content_list(list_html, i)


if __name__ == '__main__':
    meituan = MeituanSpider()
    meituan.run()

