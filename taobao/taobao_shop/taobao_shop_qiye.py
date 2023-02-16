import requests
import re
import redis


class TaobaoShop(object):
    def __init__(self):
        self.id_nema = 'id_nema.txt'
        self.qiye_id_nema = 'qiye_id_nema.txt'
        self.erry_id_nema = 'erry_id_nema.txt'
        self.redisPool = redis.Redis(host='127.0.0.1', port=6379, db=1, decode_responses=True, password="nriat.123456")

    def get_request(self, shop_id):
        url = 'https://lukangdayaofang.tmall.com'
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
            "authority": "shop94.taobao.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "zh-CN,zh;q=0.9",
            "cookie": "thw=cn; _samesite_flag_=true; cookie2=16af8e8dce750e68cb4c64be2fb81844; t=be3bc604706fc4a5a42889ac8f3c8e04; _tb_token_=5ea33336b1758; cna=UFDAGlBKIk0CAX14bA/x0nK6; xlly_s=1; _m_h5_tk=598a2725eae494441e022c3cfbc818c0_1656652438773; _m_h5_tk_enc=67e56e19d9a90e24875251295d97d331; sgcookie=E100dOCKuB5NoAFy5GANUdDRF6KwCd4EtCwOdG6TbuNm59N8rwTWBxHEhjFP%2FtoOm37HM9XCUZoYJ9V0lVd4%2FHc6irQW4jtZv9tYqTQ9YfYpMg71iDevT%2F3sSl9j8Jj2w2zM; unb=2103455748; uc1=pas=0&cookie14=UoexND3iNQugbw%3D%3D&cookie21=VFC%2FuZ9aiKcVcS5M9%2B3X&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&existShop=false&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dCvCPR%2F1kt9LrsrfY%3D&id2=UUkO1%2BLahLblCw%3D%3D&nk2=F5RMHK6PLjrWyQ%3D%3D; csg=368d5ef9; lgc=tb95487286; cancelledSubSites=empty; cookie17=UUkO1%2BLahLblCw%3D%3D; dnk=tb95487286; skt=0ad83c1d1541dbed; existShop=MTY1NjY0NDE2NQ%3D%3D; uc4=nk4=0%40FY4HWUiuhU2ELf%2BnMxKr3xeNR%2Fkf&id4=0%40U2uCuLZXEe%2Fl8gAXJJZuYtJNhrjV; tracknick=tb95487286; _cc_=WqG3DMC9EA%3D%3D; _l_g_=Ug%3D%3D; sg=688; _nk_=tb95487286; cookie1=BqbgAZBKLZ%2BfLKcRqFKvBrM4QyuYcsCJPyv7Oojo5FM%3D; x5sec=7b2273686f7073797374656d3b32223a223630666139653338386134326439333834353033333730623036386336666139434d62452b5a5547454e4b716d6332623834764972514561444449784d444d304e5455334e4467374d54444c753944322b2f2f2f2f2f3842227d; pnm_cku822=098%23E1hvhvvUvbZvUpCkvvvvvjiWRLdO6jYnPFsvQjnEPmPUsjiWnLLhljYPn2FUgji8Rs9CvvpvvvvvvvhvC9vhvvCvpv9CvhQhZMgvCASXS47BhC3qVUcnDOvXecIUDajxALwpEcqUaNoxdXyaWXxrsj7J%2B3%2BiafmxfBAKNB3rgj7%2B%2BulsbdmxfwkK5eU%2Flw2UkByKuvhvmvvv9W2zBY83kvhvCQ9v9OC1pwkgvpvIvvvvvhCvvvvvvvpvphvWAQvvCvCvpCvmvvvhvhCvhVhvvvpvphvpOpgCvvpvvPMMi9hvCvvv9UU%3D; linezing_session=TgmkBt46FcsUtegspZxLfxoS_1656644765381JCT6_2; isg=BOXl06mw61o3Rg-nUEPRHOEL9KEfIpm0PPIDAOfKmJwr_gVwr3PMhHLfiGKIfrFs; l=eBIXVQEnL29PXR7iBOfZhurza77T9IRAguPzaNbMiOCP_XCH5TRlW6beQWTMCnGVh6FwR3SVatiMBeYBq_C-nxvOeLaD0dDmn; tfstk=ckF1BFj4dhxsxAB2_P_FQBCRpalVagRIkOg85MUkTzfdF1zsvsXDa0Nlp-xmgq3C.",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
        }
        response = requests.request("GET", url, headers=headers)
        data = response.text
        return data

    def text_data(self, data_text, shop_id):
        no_title = re.search('没有找到相应的店铺信息', data_text)
        title = re.search('该用户已通过企业卖家认证', data_text)
        msg = re.search('页面-验证码', data_text)
        if msg != None:
            print(msg.group(0))
            self.with_open(self.erry_id_nema, shop_id)
        elif no_title == None:
            if title == None:
                self.with_open(self.id_nema, shop_id)
            elif title.group(0) == '该用户已通过企业卖家认证':
                print(title.group(0))
                self.with_open(self.qiye_id_nema, shop_id)
        else:
            print(no_title.group(0))
            self.with_open(self.erry_id_nema, shop_id)

    def with_open(self, name, shop_id):
        with open(r'{}'.format(name), 'a', encoding='utf-8') as write:
            write.write(str(shop_id) + '\n')
            write.flush()

    def bool_write(self, bool, shop_id):
        if bool == True:
            self.with_open(self.qiye_id_nema, shop_id)
        else:
            self.with_open(self.id_nema, shop_id)

    def run_spider(self):
        # for i in range(1, 150):
        #     self.redisPool.sadd('taobao_shop_id', i)
        while True:
            # shop_id = self.redisPool.spop('taobao_shop_id')
            shop_id = '86697'
            if shop_id != None:
                data_text = self.get_request(shop_id)
                self.text_data(data_text, shop_id)
                # print(bool)
            else:
                break


def run_tabao_shop():
    run_tb = TaobaoShop()
    run_tb.run_spider()


if __name__ == '__main__':
    run_tabao_shop()



