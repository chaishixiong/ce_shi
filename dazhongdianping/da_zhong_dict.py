# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
import re
import requests
import pandas as pd
from lxml import etree
from dazhongdianping.da_zhong_setteng import cate_list


# def index():
#     url = "https://www.dianping.com/quzhou/ch10"
#     headers = {
#         'Accept':'text/html,application/xhtml+xml,application/xmlq=0.9,image/webp,image/apng,*/*q=0.8,application/signed-exchangev=b3',
#         'Accept-Encoding':'gzip, deflate',
#         'Cookie':'navCtgScroll=100; _lxsdk=1766018886cc8-04d7ab8077d427-5437971-4a574-1766020c6400; _lxsdk_cuid=1766018886cc8-04d7ab8077d427-5437971-4a574-1766020c6400; switchcityflashtoast=1; _hc.v=ce0d9b7c-277f-582f-7204-2d40c1c9a9cc.1614744421; s_ViewType=10; _tr.u=KmpIrpU4VFRQEB9E; _dp.ac.v=28882ee0-66fa-400f-a218-97da5a749b5b; ctu=2a2d9a661eb30bb6d36de26436e1fdf1857c55c22c0f2809953c81468300ca3a; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1619679169; source=m_browser_test_33; PHOENIX_ID=0a48873f-1791c776a08-610f; info="{\"query_id\":\"9dce19f9-c2a9-4884-99c4-0fe41c38b073\",\"ab_id\":\"exp000095_a\"}"; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_3713187639; uamo=18779340395; cityid=106; cy=106; cye=quzhou; fspop=test; pvhistory="6L+U5ZuePjo8L3F1emhvdS9jaCU3Qj46PDE2MjAzNzcxNDUyMTVdX1s="; m_flash2=1; default_ab=citylist%3AA%3A1%7Cshop%3AA%3A11%7Cindex%3AA%3A3%7CshopList%3AA%3A5%7Cmap%3AA%3A1%7Cmyinfo%3AA%3A1; thirdtoken=e9214815-06a0-41d9-a0ef-2ed692fff555; _thirdu.c=35551c46e88dbc3a47a53c2e949b3cbd; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1619677706,1619681417,1619753965,1620379992; aburl=1; Hm_lpvt_dbeeb675516927da776beeb1d9802bd4=1620380041; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1620640617; _lxsdk_s=17955b15b65-97b-196-418%7C%7C103',
#         'Host':'www.dianping.com',
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
#         }
#     response = requests.get(url=url, headers=headers)
#     html = etree.HTML(response.text)
#     ul_li = html.xpath('//*[@id="shop-all-list"]/ul/li')  # 多少个li标签
#     number = len(ul_li)
#     df = pd.DataFrame()
#     for i in range(1, number + 1):
#         # 详情url
#         details_url = html.xpath("//li[{}]//div[@class='tit']/a[1]/@href".format(1))[0]
#         # 标题
#         title = html.xpath("//li[{}]//div[@class='tit']/a[1]/h4/text()".format(1))
#         print(title)
#         # 评分
#         score = html.xpath('//li[1]//div[@class="nebula_star"]/div[2]/text()'.format(i))
#         print(score)
#         # 评论数
#         comment_str = html.xpath('//li[{}]//a[@class="review-num"]/b//text()'.format(i))
#         # comment = [shop_num.get(k) if k in shop_num.keys() else k for k in comment]
#         # comment = ["".join(comment)]
#         comment = str_data('shop_num', comment_str)
#         print(comment)
#         # 人均价
#         people_money_str = html.xpath(
#             "//ul/li[{}]/div[@class='txt']/div[@class='comment']/a[@class='mean-price']/b//text()".format(i))
#         # people_money = [shop_num.get(j) if j in shop_num.keys() else j for j in people_money]
#         # people_money = ["".join(people_money)]
#         people_money = str_data('shop_num', people_money_str)
#         print(people_money)
#         # 主营
#         # main_business_name = html.xpath('//li[{}]//div[@class="tag-addr"]/a[1]/span/svgmtsi/text()'.format(i))
#         main_business_name = html.xpath('//li[{}]//div[@class="tag-addr"]/a[1]/span//text()'.format(i))
#         main_business = str_data('tag_name', main_business_name)
#         print(main_business)
#         # 地址
#         address_name = html.xpath('//li[{}]//div[@class="tag-addr"]/a[2]/span//text()'.format(i))
#         # address = html.xpath('//li[{}]//div[@class="tag-addr"]/a[2]/span/svgmtsi/text()'.format(i))
#         address = str_data('tag_name', address_name)
#         print(address)
#         # 精确地址
#         precise_address_str = html.xpath('//li[{}]//div[@class="tag-addr"]/span//text()'.format(i))
#         # precise_address = html.xpath('//li[{}]//div[@class="tag-addr"]/span/svgmtsi/text()'.format(i))
#         precise_address = str_data('address', precise_address_str)
#         precise_name = address + ', ' + precise_address
#         print(precise_name)
#     return df
#
#
#
#
# def svg_parser(url):
#     """
#     解析界面: 每行汉字的值
#     y值 : 表示属于第几梯队
#     font-size: 每个像素占的 像素
#     """
#     headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#         'Accept-Encoding': 'gzip, deflate',
#         'Host': 's3plus.meituan.net',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
#     }
#     r = requests.get(url, headers=headers).content
#     from fontTools.ttLib import TTFont
#     with open('responts.woff', 'wb')as f:
#         f.write(r)
#     addressfont = TTFont('responts.woff')
#     addressfont.saveXML('responts.xml')
#     address_TTGlyphs = addressfont['cmap'].tables[0].ttFont.getGlyphOrder()[2:]
#
#     address_dict = {}
#     for i, x in enumerate(address_TTGlyphs):
#         address_dict[x] = str(i)
#         print(address_dict[x])
#     print(address_dict)
#     return address_dict
#
#
# def category_name(details_responts):
#     headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xmlq=0.9,image/webp,image/apng,*/*q=0.8,application/signed-exchangev=b3',
#         'Accept-Encoding': 'gzip, deflate',
#         'Cookie': 'navCtgScroll=100; _lxsdk=1766018886cc8-04d7ab8077d427-5437971-4a574-1766020c6400; _lxsdk_cuid=1766018886cc8-04d7ab8077d427-5437971-4a574-1766020c6400; switchcityflashtoast=1; _hc.v=ce0d9b7c-277f-582f-7204-2d40c1c9a9cc.1614744421; s_ViewType=10; _tr.u=KmpIrpU4VFRQEB9E; _dp.ac.v=28882ee0-66fa-400f-a218-97da5a749b5b; ctu=2a2d9a661eb30bb6d36de26436e1fdf1857c55c22c0f2809953c81468300ca3a; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1619679169; source=m_browser_test_33; PHOENIX_ID=0a48873f-1791c776a08-610f; info="{\"query_id\":\"9dce19f9-c2a9-4884-99c4-0fe41c38b073\",\"ab_id\":\"exp000095_a\"}"; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_3713187639; uamo=18779340395; cityid=106; cy=106; cye=quzhou; fspop=test; pvhistory="6L+U5ZuePjo8L3F1emhvdS9jaCU3Qj46PDE2MjAzNzcxNDUyMTVdX1s="; m_flash2=1; default_ab=citylist%3AA%3A1%7Cshop%3AA%3A11%7Cindex%3AA%3A3%7CshopList%3AA%3A5%7Cmap%3AA%3A1%7Cmyinfo%3AA%3A1; thirdtoken=e9214815-06a0-41d9-a0ef-2ed692fff555; _thirdu.c=35551c46e88dbc3a47a53c2e949b3cbd; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1619677706,1619681417,1619753965,1620379992; aburl=1; Hm_lpvt_dbeeb675516927da776beeb1d9802bd4=1620380041; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1620640617; _lxsdk_s=17955b15b65-97b-196-418%7C%7C103',
#         'Host': 'www.dianping.com',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
#     }
#     response = requests.get(url=details_responts, headers=headers)
#     html = etree.HTML(response.text)
#     category_list = html.xpath('//div[@class="breadcrumb"]/a/text()')
#     print(category_list)


if __name__ == '__main__':
    # 数字匹配  .woff 格式
    # df = index()
    # url = 'https://s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/b0f80c5f.woff'
    # svg_parser(url)
    # re_str()
    # import csv
    # with open('responts.xml', 'r',encoding='utf-8')as f:
    #     r_open = csv.reader(f)
    #     print(r_open)
    # url = 'http://www.dianping.com/shop/H5IsL3QzGr9BedqU'
    # category_name(url)
    import json
    url = 'https://api.fomille.com/agent/api/merchant/merchant/customer-paging'
    headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "app": "fomille",
            "cache-control": "no-cache",
            "content-type": "application/json;charset=UTF-8",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sign": "c48d15e93d8478ed88ff9949246c3178",
            "timestamp": "1554441329790",
            "token": "44af32f8d14a4dc4b9240f8937baaca0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
        }

    parmas = {
        "current": 1,
        "size": 10,
        "params": {
            "states": [1, 2, 3]
        }
    }
    r = requests.request('POST', url=url, headers=headers, data=json.dumps(parmas))
    data = r.content.decode()
    print(data)
