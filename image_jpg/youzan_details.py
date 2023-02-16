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
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
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
        data = r.content.decode()
        json_data = json.loads(data)
        image_jlist = json_data.get('data')
        num = 1
        if image_jlist is not None:
            image_jpg = image_jlist.get('components')
            if len(image_jpg) > 0:
                image_l = image_jpg[0].get('content')
                if image_l is not None:
                    image_list = re.findall(r'[a-zA-z]+://[^\s]*', image_l)
                    new_list = list(set(image_list))
                    for image in new_list:
                        imag = image.replace('"', '').replace(' ', '')
                        headers = {
                            'authority': 'img01.yzcdn.cn',
                            'cache-control': 'max-age=0',
                            'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
                            'sec-ch-ua-mobile': '?0',
                            'upgrade-insecure-requests': '1',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'sec-fetch-site': 'none',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-user': '?1',
                            'sec-fetch-dest': 'document',
                            'accept-language': 'zh-CN,zh;q=0.9',
                            # 'if-none-match': '^\\^FlHYLF_yq8Fou8fI68_D7_3DVCvN^\\^',
                            # 'if-modified-since': 'Sat, 15 Aug 2020 08:57:14 GMT',
                        }

                        # response = requests.get('https://img01.yzcdn.cn/upload_files/2020/08/15/FlHYLF_yq8Fou8fI68_D7_3DVCvN.jpg',
                        #                         headers=headers)
                        r = requests.get(imag, headers=headers)
                        with open(self.lu_jing + '/' + str(num) + '.jpg', 'wb') as f:
                            f.write(r.content)
                        num += 1

    def run_youzan(self):
        with open('youzan.txt', 'r')as str_url:
            for url in str_url:
                if url == '\n':
                    print('空的')
                # elif "youzan" in url:
                #     pass
                else:
                    id_id = re.search(r'detail/(.*)', url).group(1)
                    print(id_id)
                    path = r'C:\Users\Administrator\Desktop\测试\image_jpg\youzan'
                    os.mkdir(path + '/id_{}/xiang_qin'.format(id_id))
                    self.lu_jing = path + '/id_{}/xiang_qin'.format(id_id)
                    url_x_q = 'https://shop90916053.m.youzan.com/wscgoods/detail-api/showcase-components.json?alias={}&isGdt=&version=&ggType=&platform=unknown&isFastBuy=&danger=0&cdnSpeedUp=inpage&host=shop90916053.m.youzan.com&kdt_id=90723885'.format(id_id)
                    r = self.request(url_x_q)
                    self.parameters(r)


def run():
    r = YouZanShopGoods()
    r.run_youzan()


if __name__ == '__main__':
    run()
    # import requests
    #
    # headers = {
    #     'authority': 'img01.yzcdn.cn',
    #     'cache-control': 'max-age=0',
    #     'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
    #     'sec-ch-ua-mobile': '?0',
    #     'upgrade-insecure-requests': '1',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'sec-fetch-site': 'none',
    #     'sec-fetch-mode': 'navigate',
    #     'sec-fetch-user': '?1',
    #     'sec-fetch-dest': 'document',
    #     'accept-language': 'zh-CN,zh;q=0.9',
    #     # 'if-none-match': '^\\^FlHYLF_yq8Fou8fI68_D7_3DVCvN^\\^',
    #     # 'if-modified-since': 'Sat, 15 Aug 2020 08:57:14 GMT',
    # }
    #
    # response = requests.get('https://img01.yzcdn.cn/upload_files/2020/08/15/FvHDocwHULRILADXNhwy0pi0WvVM.jpg',
    #                         headers=headers)
    # print(response.content)
