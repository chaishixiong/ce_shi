import requests
import re


def run_vph():
    url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'referer': 'https://list.vip.com/',
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "script",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-site"
    }
    params = {
        'callback': 'getProductIdsListRank',
        'app_name': 'shop_pc',
        'app_version': '4.0',
        'warehouse': 'VIP_SH',
        'fdc_area_id': '103103101',
        'client': 'pc',
        'mobile_platform': '1',
        'province_id': '103103',
        'api_key': '70f71280d5d547b2a7bb370a529aeea1',
        'user_id': '',
        'mars_cid': '1603366077890_5508c4a950bc8ca71263d2c0cba63d66',
        'wap_consumer': 'a',
        'uid': '',
        'abtestId': '1872',
        'mtmsRuleId': '52156162',  # 类目id
        'scene': 'rule_stream',
        'sizeNames': '',
        'props': '',
        'vipService': '',
        'bigSaleTagIds': '',
        'filterStock': '0',
        'brandStoreSns': '',
        'sort': '0',
        'pageOffset': '240',  # 每循环一次加120
        'salePlatform': '1',
    }
    r = requests.get(url=url, headers=headers, params=params)
    data = r.content.decode()
    ids = re.findall('"pid":"(\d+)"', data)
    print(data)


def get_vph_goods():
    url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2?'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'referer': 'https://list.vip.com/',
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "script",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-site"
    }
    params = {
        'callback': 'getMerchandiseDroplets1',
        'app_name': 'shop_pc',
        'app_version': '4.0',
        'warehouse': 'VIP_SH',
        'fdc_area_id': '103103103',
        'client': 'pc',
        'mobile_platform': '1',
        'province_id': '103103',
        'api_key': '70f71280d5d547b2a7bb370a529aeea1',
        'user_id': '',
        'mars_cid': '1624258928410_7c8963e26387cc670b98be6ea6b88488',
        'wap_consumer': 'a',
        'productIds': '6919103859808873497,6918721159478060893,6918965173768013202,6918375228737197966,6918792672991510872,6917925668863218332,6918760630874290895,6917917244553020060,6919280758614747421,6919247329944339019,6917917244536214172,6918500792052609602,6919308718491743260,6918892804019462489,6919220281756165084,6917917221918081692,6918656274010386589,6918954733306094237,6918721484869564253,6918924499550197275,6917966180629832732,6919327176192775007,6918712818229987215,6918919693578031692,6919369576316502594,6919360736099759890,6918067417696040604,6919076771613258077,6919022705330467035,6919011370422670363,6918954733171434141,6919289344322848925,6917999598731167196,6919220236696431062,6917917243688796764,6918408354033137436,6919115849867007635,6919189443416373010,6918527034704664541,6918931606027183643,6918902406087920459,6918942977327674206,6919310239335544580,6919249223559301519,6918414315351324444,6919327161470604127,6918347452064806300,6919238024898024596,6919208653248379780,6918466071313938269',
        'scene': 'rule_stream',
        'standby_id': 'nature',
        'extParams': '{"stdSizeVids": "", "preheatTipsVer": "3", "couponVer": "v2", "exclusivePrice": "1", "iconSpec": "2x", "ic2label": 1}',
    }
    r = requests.get(url=url, headers=headers, params=params)
    data = r.content.decode()
    print(data)


def get_vph_goods_a():
    url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2?'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'referer': 'https://list.vip.com/',
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "script",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-site"
    }
    params = {
        'callback': 'getMerchandiseDroplets1',
        'app_name': 'shop_pc',
        'app_version': '4.0',
        'warehouse': 'VIP_SH',
        'fdc_area_id': '103103103',
        'client': 'pc',
        'mobile_platform': '1',
        'province_id': '103103',
        'api_key': '70f71280d5d547b2a7bb370a529aeea1',
        'user_id': '',
        'mars_cid': '1624258928410_7c8963e26387cc670b98be6ea6b88488',
        'wap_consumer': 'a',
        'productIds': '6919103859808873497,6918721159478060893,6918965173768013202,6918375228737197966,6918792672991510872,6917925668863218332,6918760630874290895,6917917244553020060,6919280758614747421,6919247329944339019,6917917244536214172,6918500792052609602,6919308718491743260,6918892804019462489,6919220281756165084,6917917221918081692,6918656274010386589,6918954733306094237,6918721484869564253,6918924499550197275,6917966180629832732,6919327176192775007,6918712818229987215,6918919693578031692,6919369576316502594,6919360736099759890,6918067417696040604,6919076771613258077,6919022705330467035,6919011370422670363,6918954733171434141,6919289344322848925,6917999598731167196,6919220236696431062,6917917243688796764,6918408354033137436,6919115849867007635,6919189443416373010,6918527034704664541,6918931606027183643,6918902406087920459,6918942977327674206,6919310239335544580,6919249223559301519,6918414315351324444,6919327161470604127,6918347452064806300,6919238024898024596,6919208653248379780,6918466071313938269',
        'scene': 'rule_stream',
        'standby_id': 'nature',
        'extParams': '{"stdSizeVids": "", "preheatTipsVer": "3", "couponVer": "v2", "exclusivePrice": "1", "iconSpec": "2x", "ic2label": 1}',
    }
    r = requests.get(url=url, headers=headers, params=params)
    data = r.content.decode()
    print(data)


def get_vph_gooddata():
    url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc2/product/detail/v5?app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103103103&client=pc&mobile_platform=1&province_id=103103&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1624258928410_7c8963e26387cc670b98be6ea6b88488&wap_consumer=a&productId=6918560830787461197&functions=brand_store_info%2CnewBrandLogo%2ChideOnlySize%2CextraDetailImages%2Csku_price%2Cui_settings&kfVersion=1&highlightBgImgVer=1&is_get_TUV=1&commitmentVer=2&haitao_description_fields=text&supportSquare=1&longTitleVer=2&propsVer=1'
    # headersheaders = {
    # 	'Cookie': 'vip_province_name=%E6%B2%B3%E5%8D%97%E7%9C%81; vip_city_name=%E4%BF%A1%E9%98%B3%E5%B8%82; vip_city_code=104101115; vip_wh=VIP_HZ; vip_ipver=31; user_class=a; mars_sid=ff7be68ad4dc97e589a1673f7154c9f9; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A0%7Cul%3A3105; mars_pid=0; visit_id=98C7BA95D1CA0C0E518537BD0B4ABEA0; vip_tracker_source_from=; pg_session_no=5; mars_cid=1600153235012_7a06e53de69c79c1bad28061c13e9375',
    # 	'Referer': 'https://category.vip.com/suggest.php?keyword=%E6%8A%A4%E8%82%A4&ff=235|12|1|1',
    # 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    # }
    headers = {
        'Cookie': 'vip_province_name=%E6%B2%B3%E5%8D%97%E7%9C%81; vip_city_name=%E4%BF%A1%E9%98%B3%E5%B8%82; vip_city_code=104101115; vip_wh=VIP_HZ; vip_ipver=31; user_class=a; mars_sid=ff7be68ad4dc97e589a1673f7154c9f9; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A0%7Cul%3A3105; mars_pid=0; visit_id=98C7BA95D1CA0C0E518537BD0B4ABEA0; vip_tracker_source_from=; pg_session_no=5; mars_cid=1600153235012_7a06e53de69c79c1bad28061c13e9375',
        'Referer': 'https://category.vip.com/suggest.php?keyword=%E6%8A%A4%E8%82%A4&ff=235|12|1|1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    params = {
        'app_name': 'shop_pc',
        'app_version': '4.0',
        'warehouse': 'VIP_SH',
        'fdc_area_id': '103103103',
        'client': 'pc',
        'mobile_platform': '1',
        'province_id': '103103',
        'api_key': '70f71280d5d547b2a7bb370a529aeea1',
        'user_id': '',
        'mars_cid': '1624258928410_7c8963e26387cc670b98be6ea6b88488',
        'wap_consumer': 'a',
        'productId': '6918984012292347293',
        'functions': 'brand_store_info,newBrandLogo,hideOnlySize,extraDetailImages,sku_price,ui_settings',
        'kfVersion': '1',
        'highlightBgImgVer': '1',
        'is_get_TUV': '1',
        'commitmentVer': '1',
        'haitao_description_fields': 'text',
        'supportSquare': '1',
        'longTitleVer': '2',
        'propsVer': '1'
    }
    # r = requests.get(url=url, headers=headers)
    # data = r.content.decode()
    # print(data)
    pid = '6918984012292347293'
    # product_url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2?callback=getMerchandiseDroplets3&app_name=shop_pc&app_version=4.0&warehouse=VIP_HZ&fdc_area_id=104101115&client=pc&mobile_platform=1&province_id=104101&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1600153235012_7a06e53de69c79c1bad28061c13e9375&wap_consumer=a&productIds={}%2C&scene=search&standby_id=nature&extParams=%7B%22stdSizeVids%22%3A%22%22%2C%22preheatTipsVer%22%3A%223%22%2C%22couponVer%22%3A%22v2%22%2C%22exclusivePrice%22%3A%221%22%2C%22iconSpec%22%3A%222x%22%7D&context=&_=1600164018137'.format(pid)
    product_url = 'https://mapi.vip.com/vips-mobile/rest/content/reputation/queryBySpuId_for_pc?callback=getCommentDataCb&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103103101&client=pc&mobile_platform=1&province_id=103103&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1626921908186_11bc490f22e4c90b54aa0a97f8d8aed2&wap_consumer=a&spuId=2048933186433679364&brandId=1710613372&page=1&pageSize=10&timestamp=1626932771000&keyWordNlp=%E6%9C%80%E6%96%B0-%E6%8C%89%E6%97%B6%E9%97%B4%E6%8E%92%E5%BA%8F&_=1626932740443'
    product_html = requests.get(product_url, headers=headers)
    data = product_html.text
    # dict_data = re.search(r'"getMerchandiseDroplets3\\("(.*?)"\\)"', data).group()
    print(data)

'''
商品ID  productIdStr
月销量
评论数
类目ID
品牌ID  brandIdStr
平台
商品名称
促销价
原价
配送费用
主图
'''


class VphGoodsId(object):
    def __init__(self):
        pass

    def request_id(self):
        pass

    def pid_list(self):
        pass

    def run_id(self):
        pass


def vph_pid():
    pass


if __name__ == '__main__':
    # run_vph()
    # get_vph_goods()
    get_vph_gooddata()
