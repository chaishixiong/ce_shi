import re
import requests, redis, time
from lxml import etree
from 统计局需求_2.sql_pool.dbpool import kj_1_4_pool
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession


class AlbabagjRegistration(object):
    def __init__(self):
        self.shop_key = ''
        self.registration_mysql = DataBaseSession(kj_1_4_pool)
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True, password="nriat.123456")
        self.write_data = open(r'X:\数据库\阿里巴巴国际站\alibabagj_shopkey_cuowu.txt', 'w', encoding='utf-8')
        self.alibabagj_key = 'alibabagj_key_id'

    def albbgj_request(self, url):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "cookie": 'ali_apache_id=33.50.230.34.1665456325942.543072.9; intl_common_forever=3VS+9zvMKHYHlY2iOnQKQaE9KFw3umvOpB13ynuxl0/OVFBsrAeO7w==; _ga=GA1.2.80178810.1665463013; ali_apache_track=mt=2^|mid=cn1557833621ffzi; t=8993b40bff80b250a2d31163918835ea; cbc=G4A1F7E1A2C71552844E2F7ADE07B339ED54AF341E5DCBD43DF; umdata_=GED5272F140D2DE79BEDA5B34AB17CCA865DB541EB213D1E7B0; sgcookie=E100PulwPzwPxa3yOhj6f9DYPlXqQzxY5QRhOxdIGQGDcrrhtCcnzRc1Y4IgAyMW9^%^2BJnwX9LDkiH87xrvep6NIjp5A^%^3D^%^3D; xman_us_f=x_l=1; acs_usuc_t=acs_rt=e4a1d593bdeb41af8ad459dc67f42a80; cookie2=141b56958e89e4f0d22927d7b5614855; _tb_token_=771886134e757; cna=ko/zG5QU3QgCAdpKN4zufp8S; sc_g_cfg_f=sc_b_locale=en_US; _samesite_flag_=true; xman_t=/CXJLa4uOjaxrXkvK05UaPW007Ib5jbTHNZDdjuU2MUFfbAMk1XdnCR2gDgMu3YDy4Al0GmqtyeGvxQCzAGqHrh8NTl4Esgj; xlly_s=1; _m_h5_tk=bf129f847e66207ea0680f799e87c901_1670470149061; _m_h5_tk_enc=8fe3d2f32e44d240fef8f1ef5ee678b1; c_csrf=6f70d494-bab7-4a7e-9267-1e9043de458c; ug_se_c=free_1670462816750; _umdata=G7DAE85F217FF1278226DF0B0914F71033705D6; JSESSIONID=D99578B92D631F6AE32B6EF4EC60F5B0; ali_apache_tracktmp=^\^" ^\ ^ "; xman_f=YruPURLiH6u5q5odZAP+SsDTzqEHrOerNpuDUR6gSTdWZdIIV37+bBc9aICJ2hkWAv5L62RcFRCgWWU/Iva+ZboOdfbaF95Gn0tAY5SigmcnfplEuf0Ynw==; isg=BFBQDuzYB0KmSNtGxmlVpvthIZ6iGTRjfEe3aUolKqt-hfwv9ihB8jD3WU1lVew7; tfstk=c5_OBr40sJ2gQpyD8FEHg1Ihe-VlC9q9pfOKkaecF6wSSvA6gw1mCab-vBZ6LLJT9; l=fBPBG3WnL57gjeZyBO5Clurza779yCAXGsPzaNbMiIEGa1ydteMcHOCFhqi9SdtjgT54AFtzEHwxcd3w-rUU-xaWs5kgcPG1JQvvoewvTtH5.'
        }
        r = requests.get(url, headers=headers)
        return r

    def re_xpath(self, respones_data):
        if '<title>HTTP 404</title>' in respones_data.text:
            return None
        try:
            respones_html = etree.HTML(respones_data.text)
            registration = respones_html.xpath(r'//table[@class="table"]//dd/text()')
            if len(registration) == 12:
                respones_num = registration[0]
                company_name = re.search(r'name "(.*?)" on', respones_data.text).group(1)
                date_of_lssue = registration[3]
                date_of_expiry = registration[4]
                registered_capital = registration[5]
                country = registration[6]
                registered_address = registration[7]
                year_established = registration[8]
                legal_representative = registration[9]
                legal_from = registration[10]
                issuing_authority = registration[11]
                data_list = [self.shop_key, respones_num, company_name, date_of_lssue, date_of_expiry, registered_capital, country, registered_address, year_established, legal_representative, legal_from, issuing_authority]
                self.item_sql_data(data_list)
                print(data_list)
        except Exception as e:
            self.write_data.write(self.shop_key + '\n')
            print(e)

    def item_sql_data(self, data_list):
        insertion_sql = "insert into alibabagj_respones_info (shop_key, respones_num, company_name, date_of_lssue, date_of_expiry, registered_capital, country, registered_address, year_established, legal_representative, legal_from, issuing_authority) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # 插入库名： session_227_tb
        self.registration_mysql.insertion_data(insertion_sql, data_list)

    def shop_redis(self):
        set_dict = set()
        insertion_sql = "select `shop_key` from alibabagj_respones_info"
        # 插入库名： session_227_tb
        albbgj_key_list = self.registration_mysql.query_tuple_data(insertion_sql)
        for albbgj_key in albbgj_key_list:
            key_name = albbgj_key[0]
            set_dict.add(key_name)
        with open(r'X:\数据库\阿里巴巴国际站\alibabagj_shop_seed\shop_key.txt', 'r', encoding='utf-8') as s_key:
            for i in s_key:
                s_id = i.strip()
                if s_id not in set_dict:
                    self.r.sadd(self.alibabagj_key, s_id)

    def run_al_spider(self):
        while True:
            try:
                if self.r.exists(self.alibabagj_key):
                    self.shop_key = self.r.spop(self.alibabagj_key)
                    url = 'https://himalayanherbaria.trustpass.alibaba.com/company_profile/trustpass_profile.html'.format(self.shop_key)
                    response_data = self.albbgj_request(url)
                    self.re_xpath(response_data)
                    self.write_data.close()
                else:
                    print('------未找到任务队列--------')
                    self.write_data.close()
                    time.sleep(60)
                    break
            except Exception as e:
                print(e)
        # self.shop_key = 'nilin.en'
        # url = 'https://{}.alibaba.com/company_profile/trustpass_profile.html'.format(self.shop_key)
        # respones_data = self.albbgj_request(url)
        # self.re_xpath(respones_data)
        # self.write_data.close()


def run_albabagjaegistration():
    run_al = AlbabagjRegistration()
    # run_al.shop_redis()
    run_al.run_al_spider()


if __name__ == '__main__':
    run_albabagjaegistration()



