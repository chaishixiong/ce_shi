import requests
import json
from taobao.setting import cat_name_list, platform_list
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import tm_pool


class TmallShop(object):
    def __init__(self):
        self.session_227_tm = DataBaseSession(tm_pool)
        self.platform_list = platform_list  # 平台
        self.cat_name_list = cat_name_list  # 类目名称
        self.one_url = 'https://shopsearch.taobao.com/search?{}&ajax=true&q={}&s=2000'
        self.data_list = []

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
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "cookie": "sgcookie=E100TpQoiI8dRTWgtJecUyIbTwaSWwGBNTCuQkOpALl8m0NJABcem7r8kvIcp96t0j8ylCyYE7fn%2F8X5uprW4iZethTS%2B7RBl3VTvpsfCfL8tx0%3D; unb=2103455748; uc3=nk2=F5RMHK6PLjrWyQ%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&id2=UUkO1%2BLahLblCw%3D%3D&vt3=F8dCvUr0HqDyaDZsis8%3D; csg=2d878608; cookie17=UUkO1%2BLahLblCw%3D%3D; skt=5a0e0b1ec510fb35; existShop=MTYzOTU0OTk3NQ%3D%3D; uc4=id4=0%40U2uCuLZXEe%2Fl8gAXJJBR3vIm81Cs&nk4=0%40FY4HWUiuhU2ELf%2BnMxQ841qWEp8C; _cc_=UIHiLt3xSw%3D%3D; _l_g_=Ug%3D%3D; sg=688; _nk_=tb95487286; cookie1=BqbgAZBKLZ%2BfLKcRqFKvBrM4QyuYcsCJPyv7Oojo5FM%3D; enc=qAJmlEFQp%2B45qy3RlDdba5mK0fO%2FM5hkWVVfG0ckO0opRFy5vt5wFPcaOgWFrXVtb8WIm49TdO3dtbdewthvog%3D%3D; mt=ci=77_1; uc1=existShop=false&cookie21=V32FPkk%2Fgi8IDE%2FSq3xx&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie14=Uoe3fokabRE7UA%3D%3D&pas=0&cookie15=UtASsssmOIJ0bQ%3D%3D; _uab_collina=163955010451928233798807; cna=mHpAGrqkig4CATy6ccYfOVOR; xlly_s=1; tfstk=cQXFBucp3Jee6aJ7Mp9zO-VYZzxdaLjhqA-Xt6kmB8iEabXMusmsyhfrIh-WkRAh.; l=eBaO-vfmg34JyzQkBO5Zourza779oCRfGsPzaNbMiIncC6Hh1l99Hx-QcdHNiptRR8XcTh8B4IiyLIyTmFCUJskVF3H6JuFfqBMkCef..; isg=BNzcbwp50VYlk6UFnTO6NiF_rfqOVYB_vh4p8rbZbEaJAXiL3mfMDzrzYWn5ibjX; JSESSIONID=F9BFA4898285D49410D1BDE37E03B727"
        }
        re = requests.get(url=url, headers=headers)
        return re

    def data_analysis(self, response):
        data = response.content.decode()
        try:
            data_dict = json.loads(data)
            return data_dict
        except Exception as e:
            print(data)
            return None

    def parameter(self, parameter):
        self.data_list = []
        try:
            mods = parameter.get('mods')
            shop_list = mods.get('shoplist')
            if shop_list == 'hide':
                return 0
            data = shop_list.get('data')
            shop_items = data.get('shopItems')
            for item in shop_items:
                shop_id = item.get('nid')
                seller_id = item.get('uid')
                shop_url = item.get('shopUrl')
                similar_url = item.get('similarUrl')
                data_tuple = (shop_id, seller_id, shop_url, similar_url)
                self.data_list.append(data_tuple)
            # self.tm_shop_insertion_data()
            return len(self.data_list)
        except Exception as e:
            return 0

    def tm_shop_insertion_data(self):
        insertion_sql = "insert into taobao_all_shop (shop_id, seller_id, shop_url, similar_url) VALUES (%s,%s,%s,%s)"
        # 插入库名： session_227_tb
        self.session_227_tm.insertion_data(insertion_sql, self.data_list)

    def run_spider(self):
        platform = 'data-key=isb%2Cshop_type%2Cratesum%2Cgoodrate&data-value=1%2C%2C%2C'
        for cat_name in cat_name_list:
            response = self.request(self.one_url.format(platform, cat_name))
            parameter = self.data_analysis(response)
            number = self.parameter(parameter)
            if number < 0:
                break


def run_tmall_spider():
    run = TmallShop()
    run.run_spider()


if __name__ == '__main__':
    run_tmall_spider()










