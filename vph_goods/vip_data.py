import requests
import re
from lxml import etree


class VipDtaa():
    def __init__(self):
        pass

    def request_get(self):
        pass

    def dict_item(self):
        pass


class CsEbay(object):
    def __init__(self):
        self.number = 0
        self.i = 1
        self.cookie_num = 0

    def request(self, url):
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
        cookies_list = [
            '__gads=ID=9bc276b1fedc8d26:T=1614061756:S=ALNI_MYvtCBnG-TUZ8DcTnmuX7hI9bQAGA; ak_bmsc=A56CA806829273DD0ABD0BBD89C8248717215EBE4A4D0000454F8660330AAE6B~plVJwvFaagYWlFjJO0ZLA7OVBIBW+XNvpFJnGvwMk3p3y2bH5oXI05yo7l1g9YMSUueoXGbTpu9Rufvk7XqqhHN+0huSqNapeBwXoZAWhD/1ec8f6EC7eldu96ryNwhH2RaSsWeO2TAbLpyaVrf9thXz+pmzeO74R8QUBP82XTeQRMeLaGY/zSpZ36PtuLfMFXKvcG3BxzYF+f2G3zHyJRLWwAkkLr6ZN1vsD/Hoy55FA=; cssg=2fcbf5681720aaecbb65c943ff8d7404; JSESSIONID=18E7B3207330140FDE768E8FE39E4A9B; nonsession=CgAAIABxgrfX1MTYxOTQxOTMyMngxNjQ3OTc3MTIyMzR4MHgyWQDKACBkSM/1MmZjYmY1NjgxNzIwYWFlY2JiNjVjOTQzZmY4ZDc0MDQAywACYIZv/TU0CkID0Q**; ns1=BAQAAAXguCEiyAAaAANgATGJnnHVjNzJ8NjAxXjE2MTU1MTI1MDk4MTZeXjFeM3wyfDV8NHw3fDExXjFeMl40XjNeMTJeMTJeMl4xXjFeMF4xXjBeMV42NDQyNDU5MDc11o3dG4uGvo6mopGtEkPfFaKiLMg*; s=CgADuAGBgh7p0MwZodHRwczovL3d3dy5lYmF5LmNvbS9zY2gvc3l6YXFzeS9tLmh0bWw/X25rdyZfYXJtcnM9MSZfZnJvbSZydD1uYyZMSF9QcmVmTG9jPTYjaXRlbTRkYmI3MGNjMTgHAPgAIGCHunQyZmNiZjU2ODE3MjBhYWVjYmI2NWM5NDNmZjhkNzQwNMiWI3g*; bm_sv=AF8E0B203AF950137DAB87326DBB7213~Ycar43PWZSg1iyrlocWH3Z9CPvdx7OK8uY0tJ7sTo08imJ0Y5ipbrcivdCTX5Vu/fef3IVdBpOKHXwk0dSg0t7AGUuwggF0BwK+mqij7xbjRuwq9v3gNSdr9whaaxLFU+yL2u5lfnuQIeVtycscjZ21Hitc9asSJeNVA3PrmPqA=; npii=btguid/2fcbf5681720aaecbb65c943ff8d74046448d04b^cguid/2fcbfdec1720a6e5b576ccd7d3b85a946448d04b^; ebay=%5Ejs%3D1%5Ecv%3D15555%5Esbf%3D%2341c00000000010000100100%5Epsi%3DACfr13XA*%5E; ds2=sotr/b7piCzQMzNfz^; dp1=bu1p/QEBfX0BAX19AQA**6448cff5^pbf/#e000e000008100020000006448d067^tzo/-1e06448d067^bl/CN6448cff5^'
        ]
        cookie_dict = {i.split('=')[0]: i.split('=')[1] for i in cookies_list[self.cookie_num].split(';')}
        response_1 = requests.get(url, headers=headers, cookies=cookie_dict)
        self.cookie_num += 1
        print(self.cookie_num)
        return response_1

    def print_shop_num(self, url, us_name):
        response = self.request(url)
        r_txt = response.text
        r_html = etree.HTML(r_txt)
        youxiao = "rcnt|sm-md"
        if re.search(youxiao, r_txt):
            if r_html.xpath('//ul[@id="ListViewInner"]'):
                goods_urls = r_html.xpath(
                    '//ul[@id="ListViewInner"]/li/h3/a/@href')
                print('商品链接长度', len(goods_urls))

                goods_num = r_html.xpath('//*[@id="cbelm"]/div[3]/span[1]/text()')
                if len(goods_num) == 0:
                    print('{}店铺下有{}条商品'.format(us_name, self.number))
                    print(100 * '_')
                    return None
                goods_num = goods_num[0]
                print(goods_urls)
                shop_num = ''
                for n in goods_num:
                    if n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        shop_num += n
                if shop_num:
                    self.i += 1
                    self.number += 200
                    url = "https://www.ebay.com/sch/m.html?_nkw=&_armrs=1&_from=&_ssn={}&LH_PrefLoc=6&_pgn={}&_skc={}&rt=nc".format(
                        us_name, self.i, self.number)
                    print(self.number)
                    self.print_shop_num(url, us_name)
                    '''https://www.ebay.com/sch/m.html?_nkw=&_armrs=1&_from=&_ssn=2014jingjingstore&LH_PrefLoc=6&_pgn=5&_skc=200&rt=nc'''

    def open_txt(self):
        # with open(r'W:/scrapy_seed/ebayinfo_goods.txt') as f:
        #     ebay_text = f.readlines()
        #     for i in ebay_text:
        #         us_name = i.strip()
        #         self.request(us_name)
        #         print(us_name)
        #     f.close()
        # pass
        us_name = '2014jingjingstore'
        url = 'https://www.ebay.com/sch/{}/m.html?_nkw&_armrs=1&_from&rt=nc&LH_PrefLoc=6'.format(us_name)
        self.print_shop_num(url, us_name)


def run_cs_ebay():
    run_cs = CsEbay()
    run_cs.open_txt()


if __name__ == '__main__':
    run_cs_ebay()

