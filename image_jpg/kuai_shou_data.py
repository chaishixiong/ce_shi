import requests
import re
import json
import os
import time


class KuaiShouShopGoods(object):
    def __init__(self):
        self.lu_jing = ''

    def request(self, url):
        headers = {
            "accept": "application/json",
            "accept-language": "zh-CN,zh;q=0.9",
            "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            "sec-ch-ua-mobile": "?1",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            # "trace-id": "1.66858969827253.700907784777.1628046043017.4",
            "Cookie": "_did=web_3449092D0E87BE; did=web_i79723repyiejbmwa0nid2jm4ndlirnm",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36"
        }
        parameters = {
            'itemId': '1228362363452',
            'retryLimit': 'true',
            'carrierType': '0',
            'guarantee': 'false',
            'installWechat': 'false',
            'installAlipay': 'false',
            'installWechatSdk': 'false',
            'installAlipaySdk': 'false',
            'installUnionPaySdk': 'false',
            'sigCatVer': '1',
            '__NS_sig3': ''
        }
        r = requests.get(url=url, headers=headers)
        # time.sleep(10)
        data = r.content.decode()
        return data

    def parameters(self, data):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "if-modified-since": "Tue, 03 Aug 2021 02:35:01 GMT",
            "if-none-match": "\"AA4318CB24756E9AFA6AE22721AD855B\"",
            "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            "sec-ch-ua-mobile": "?1",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36"
        }
        image_url_list = data['productDetail']['imageUrls']
        num = 1
        for image_url in image_url_list:
            r = requests.get(url=image_url, headers=headers)
            with open(self.lu_jing + '/' + str(num) + '.jpg', 'wb') as f:
                f.write(r.content)
            num += 1

    def run_kuaishou(self):
        with open('kuaishou_url_list.txt', 'r')as str_url:
            for url in str_url:
                if url == '\n':
                    print('空的')
                else:
                    id_s = re.search(r'[0-9]+', url).group()
                    path = r'C:\Users\Administrator\Desktop\测试\image_jpg'
                    url_str = 'https://app.kwaixiaodian.com/rest/app/grocery/product/self/detail?itemId={}&retryLimit=true&carrierType=0&guarantee=false&installWechat=false&installAlipay=false&installWechatSdk=false&installAlipaySdk=false&installUnionPaySdk=false&sigCatVer=1&__NS_sig3='.format(id_s)
                    os.mkdir(path + './id_{}'.format(id_s))
                    self.lu_jing = path + './id_{}'.format(id_s)
                    response = self.request(url_str)
                    data = json.loads(response)
                    if data['result'] == 400002:
                        print(url)
                    else:
                        self.parameters(data)


def run():
    r = KuaiShouShopGoods()
    r.run_kuaishou()


if __name__ == '__main__':
    run()
    # url = 'https://app.kwaixiaodian.com/merchant/shop/detail?id=1228362363452&isCopy=1'
    # id_s = re.search(r'[0-9]+', url).group()
    # print(id_s)
