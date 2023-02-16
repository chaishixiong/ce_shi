import requests
import re
import json
import os
import time
from lxml import etree


class YouZanShopGoods(object):
    def __init__(self):
        self.lu_jing = ''

    def request(self, url):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            "sec-ch-ua-mobile": "?1",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
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
        time.sleep(5)
        print(r.status_code)
        return r

    def parameters(self, r):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36"
        }
        html_str = r.content.decode()
        main_picture = html_str.replace('\n', '').replace(' ', '')
        data = re.search(r'window._global=(.*)if\(_global.url&&', main_picture).group(1)
        json_data = json.loads(data)
        image_jlist = json_data.get('goodsData')
        num = 1
        if image_jlist is not None:
            image_jpg = image_jlist.get('goods').get('pictures')
            for image in image_jpg:
                r = requests.get(url=image['url'], headers=headers)
                with open(self.lu_jing + '/' + str(num) + '.jpg', 'wb') as f:
                    f.write(r.content)
                num += 1

    def run_youzan(self):
        id_list = []
        with open('youzan.txt', 'r')as str_url:
            for url in str_url:
                if url == '\n':
                    print('空的')
                # elif "youzan" in url:
                #     pass
                else:
                    id_id = re.search(r'detail/(.*)', url).group(1)
                    if id_id not in id_list:
                        id_list.append(id_id)
                        print(id_id)
                        path = r'C:\Users\Administrator\Desktop\测试\image_jpg\youzan'
                        os.mkdir(path + '/id_{}'.format(id_id))
                        os.mkdir(path + '/id_{}/zhu_tu'.format(id_id))
                        self.lu_jing = path + '/id_{}/zhu_tu'.format(id_id)
                        r = self.request(url)
                        self.parameters(r)


def run():
    r = YouZanShopGoods()
    r.run_youzan()


if __name__ == '__main__':
    run()
    # url = 'https://app.kwaixiaodian.com/merchant/shop/detail?id=1228362363452&isCopy=1'
    # id_s = re.search(r'[0-9]+', url).group()
    # print(id_s)
    # headers = {
    #     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #     "accept-language": "zh-CN,zh;q=0.9",
    #     "cache-control": "no-cache",
    #     "pragma": "no-cache",
    #     "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
    #     "sec-ch-ua-mobile": "?0",
    #     "sec-fetch-dest": "document",
    #     "sec-fetch-mode": "navigate",
    #     "sec-fetch-site": "none",
    #     "sec-fetch-user": "?1",
    #     "upgrade-insecure-requests": "1",
    #     "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36"
    # }
    # url = 'https://img01.yzcdn.cn/upload_files/2021/04/09/Fk8sk5fzy0CKsT9ufRpXUblONWIm.jpg'
    # r = requests.get(url=url, headers=headers)
    # with open('1111.jpg', 'wb') as f:
    #     f.write(r.content)
    # print(r)
