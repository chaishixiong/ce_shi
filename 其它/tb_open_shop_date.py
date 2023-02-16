#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sql.mysqlhelper import MySqLHelper
import requests
import re


class TbUpdataShopDate(object):
        def __init__(self):
            pass

        def sql_find(self, sql, param=None):
            db = MySqLHelper()
            if param:
                ret = db.selectone(sql=sql, param=None)
            else:
                ret = db.selectone(sql=sql)
            return ret

        def sql_updat_timen(self, id, time_time):
            update_sql = 'UPDATE taobao_shopinfo_202103 SET open_shop_date = {} WHERE shop_id = {}'.format(time_time, id)

        def request(self, id):
            url = 'https://shop.taobao.com/getShopInfo.htm?shopId=133&_ksTS={}&callback=jsonp328'.format(id)
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "max-age=0",
                "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
                "sec-ch-ua-mobile": "?0",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1"
            }
            cookies_str = 'cna=Oc1gGAJtnD0CAXPE7lr4pkxx; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=%5Cu4E09%5Cu9014%5Cu6CB3%5Cu8FD8%5Cu662F%5Cu5929%5Cu5802; _cc_=URm48syIZQ%3D%3D; enc=B6kKbNgmvF9T97QEqkn6JgA7p%2FErgv8lTK%2BFa34hd2MacOxWF7QeoxPcC3r%2FQ60ZA5IMD%2FeUtAYk9FoiBreDpQ%3D%3D; miid=494221691506845391; sgcookie=E100UQ2ra6H5TythdxTP9AwlnSj05iK%2Bo4S1hi%2FwXzVX7VoOWrirqLYIZZtwD%2BWMsk%2BW4iaFriGZ9Et5QiOffERw3A%3D%3D; cookie2=1e37952e12b0df248c46f9248398ae28; t=3d09009effe7e583d9f624ef8e8deb5a; _tb_token_=f8b3eed583816; _m_h5_tk=577e968b2d6eeff4f12ce0ee8b6000d8_1619349354450; _m_h5_tk_enc=e188320d50a51982ebcacb0dce8ed734; tfstk=cs2cB3tphSljwpluOtMbDxJ_gq5dZdxq8RPaURlgb7c8RyePiHdyTstAqDU0BC1..; l=eBgB_l6gjKHVGxnsKOfwourza77OSIRAguPzaNbMiOCP_eCp5TZcW615lB89C3GVh6eyR3leHMv_BeYBqIAAIUfw65ssXcHmn; isg=BMDAvaLAtAbCXkgC2Qp9D_4NkU6SSaQTNfN0oTpRjFtutWDf4ll0o5aHzR11BVzr'
            cookie_dict = {i.split('=')[0]: i.split('=')[1] for i in cookies_str.split(';')}
            r = requests.get(url, headers=headers, cookies=cookie_dict)
            return r

        def item_data(self, response):
            data = response.content.decode()
            time_str = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", data).groups()[0]
            return time_str

        def tb_id_cycle(self, sql):
            data_list = self.sql_find(sql, param=None)
            for id in data_list:
                print(id)
                response = self.request(id)
                time_time = self.item_data(response)
                self.sql_updat_timen(id, time_time)


def run_tb():
    run_ = TbUpdataShopDate()
    # # 查询单条
    sql1 = 'SELECT shop_id FROM `taobao_shopinfo_202103` where open_shop_date ="" union SELECT shop_id FROM `taobao_shopinfo_202102` where open_shop_date ="" union SELECT shop_id FROM `taobao_shopinfo_202101` where open_shop_date ="" '
    sql = 'select * from `taobao_shopinfo_202103` where shop_id =100000177'
    run_.tb_id_cycle(sql)
    id = '1288'
    times = '2003-05-29'
    run_.sql_updat_timen(id, times)


if __name__ == '__main__':
    run_tb()

