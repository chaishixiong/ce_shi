import requests
import json
import time
from feng_lan_spider.feng_lan_settings import headers, web_site
from sql.mysqlhelper import MySqLHelper


class FengLanWebSiteList(object):
    def __init__(self):
        self.num = 1

    def request_post(self, url, parmas):
        r = requests.request('POST', url=url, headers=headers , data=json.dumps(parmas))
        data = r.content.decode()
        data_dict = json.loads(data)
        return data_dict

    def process_item(self, data):
        item = dict()
        item['crm'] = '网站列表'  # CRM
        item['merchant_name'] = data['merchantName']  # 网站名称
        item['title'] = data['title']  # 客户名称
        item['domain_name'] = data['defaultDomain']  # 域名
        if data['siteType'] == 2:
            item['site_type'] = '企业单页'  # 网站类型 （判断）
        elif data['siteType'] == 3:
            item['site_type'] = '企业网站'
        else:
            item['site_type'] = ''
        item['create_time'] = self.times_time(data['createTime'])  # 创建时间
        item['site_name'] = self.times_time(data['expiryTime'])  # 到期时间
        if data['state'] == 0:
            item['state'] = '正常'  # 状态
        elif data['state'] == 1:
            item['state'] = '禁用'  # 状态
        else:
            item['state'] = ''  # 状态
        sql = "insert into feng_lan_website_copy1 (crm, merchant_name, title, domain_name, site_type, create_time, site_name, state) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        tuple_data = tuple(item.values())
        self.open_sql(sql, tuple_data)
        print(item)

    def times_time(self, times):
        expired_at = times // 1000
        timeArray = time.localtime(expired_at)
        time_times = time.strftime("%Y-%m-%d", timeArray)
        return time_times

    def open_sql(self, sql, param=None):
        db = MySqLHelper()
        ret = db.insertone(sql=sql, param=param)

    def run_feng_lan(self):
        for self.num in range(1, 7):
            url = 'https://api.fomille.com/merchant/api/site/site/paging'
            web_site["current"] = self.num
            responts = self.request_post(url, web_site)
            data_list = responts['data']['records']
            for data in data_list:
                self.process_item(data)


def run_feng_lan():
    run = FengLanWebSiteList()
    run.run_feng_lan()


if __name__ == '__main__':
    run_feng_lan()
