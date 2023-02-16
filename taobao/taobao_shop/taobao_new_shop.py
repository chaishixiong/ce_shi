import requests
import json
from taobao.setting import cat_name_list, platform_list
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import tb_pool
import time
import re


class TaoBaoShop(object):
    def __init__(self):
        self.session_227_tb = DataBaseSession(tb_pool)
        self.platform_list = platform_list  # 平台
        self.cat_name_list = cat_name_list  # 类目名称
        self.one_url = 'https://shopsearch.taobao.com/search?{}&q={}&s={}'
        self.data_list = []
        self.num = 740

    def request(self, url):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "cookies": "t=d1194c05a545b3a5cdbe62837e1c2acd; enc=Bc%2Bg1a%2FiecQEVe0fEGLz8iZ8Lb%2BwuC%2BCHXTBPyddNMdxaRyPaV%2Fi14Abu0fndofQkcvep3yDoRdU8udWJnNcMQ%3D%3D; thw=cn; xlly_s=1; cookie2=147297f0d2d2bb0ad50000015e52102a; _samesite_flag_=true; _tb_token_=ee133e87353ed; sgcookie=E100Q%2BQb6wtEwWOgfUw6ZmuqNeGOclhuwCNFrsOnjgO1TbtlYTwexdlVqdQ84QIsAHNroN7RVkUSVKM1HgG5bzVpOrBm8JvaJetDdm%2BtGk08JyH7Z86uLeh7dU%2B27h43QZ5P; linezing_session=aebZgXGY8jw3RvZvJTRwvd8w_1658202844951fQX5_1; _m_h5_tk=5484befe39b31e8f99e0ba7e0f35eeaf_1658210406391; _m_h5_tk_enc=0a5ba8e3952c77afcbefcf861a9fc598; mt=ci=0_0; tracknick=; cna=UFDAGlBKIk0CAX14bA/x0nK6; tfstk=c-ZfBe1aPIAXqJCSaq6P7f9NbMmNwZJICZG0h_YL2eB7FX1mzHlQxaUM633KF; l=eBLmnkzlL0J1zu_LBOfwourza77OSIRAguPzaNbMiOCP_pfH5iRVW6vyRgLMC3GVh6WXR3Wrj_IwBeYBqIV_ttkQzC_TF8Mmn; isg=BFJSC2eSZDuT_pjEUCkZultBoxg0Y1b9Y9o5qByrfoXwL_IpBPOmDVhNn4sTX86V",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        }
        re = requests.get(url=url, headers=headers)
        # time.sleep(2)
        return re

    def data_analysis(self, response):
        try:
            str_data = response.content.decode().replace('\n', '').replace('\r', '').replace(' ', '')
            str_dict_data = re.search(r'g_page_config=(.*);g_srp_loadCss', str_data).group(1)
            data_dict = json.loads(str_dict_data)
            return data_dict
        except Exception as e:
            return {}

    def parameter(self, parameter):
        self.data_list = []
        i = 0
        try:
            mods = parameter.get('mods')
            shop_list = mods.get('shoplist')
            if shop_list == 'hide':
                return 0
            data = shop_list.get('data')
            shop_items = data.get('shopItems')
            for item in shop_items:
                i += 1
                shop_id = item.get('nid')
                seller_id = item.get('uid')
                title = item.get('title')
                nick = item.get('nick')
                provcity = item.get('provcity')
                shop_url = item.get('shopUrl')
                similar_url = item.get('similarUrl')
                data_tuple = (shop_id, seller_id, title, nick, provcity, shop_url, similar_url)
                self.data_list.append(data_tuple)
            self.tb_shop_insertion_data()
            return len(self.data_list)
        except Exception as e:
            return 0

    def tb_shop_insertion_data(self):
        insertion_sql = "replace into taobao_all_shop (shop_id, seller_id,title,nick,provcity, shop_url, similar_url) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        # 插入库名： session_227_tb
        self.session_227_tb.insertion_data_list(insertion_sql, self.data_list)

    def run_spider(self):
        platform = 'data-key=isb%2Cshop_type%2Cratesum&data-value=0%2C%2C'
        for cat_name in cat_name_list:
            for num in range(self.num, 2200, 20):
                print('淘宝' + cat_name + '页数：' + str(num))
                response = self.request(self.one_url.format(platform, cat_name, num))
                # re_data = self.re_data(response)
                parameter = self.data_analysis(response)
                number = self.parameter(parameter)
                if number == 0:
                    self.num = 0
                    break


def run_taobao_spider():
    run = TaoBaoShop()
    url = 'https://shop1296507.taobao.com'
    run.request(url)


if __name__ == '__main__':
    run_taobao_spider()











