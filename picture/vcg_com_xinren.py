import requests
import json
import time
import re


class Pricture(object):
    def __init__(self):
        self.p_url_list = []

    def request(self, url):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "zh-CN,zh;q=0.9",
            "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        }
        r = requests.get(url=url, headers=headers)
        data = r.content
        return data

    def data_str(self, html_data):
        str = html_data.decode()
        data_str = str.replace(' ', '').replace('\n', '')
        da = re.search(r'"searchImage":(.*),"topicsChannel"', data_str)[1]
        data_dict = json.loads(da)
        return data_dict

    def processing_data(self, pricture_data):
        data = pricture_data.get('data')
        if data == None:
            return None
        data_list = data.get('list')
        for pict_data in data_list:
            pict_url = pict_data.get('url800')
            if pict_url != None:
                self.p_url_list.append(pict_url)

    def run_spider(self):
        num = 0
        for i in range(1, 61):
            url = 'https://www.vcg.com/creative-image/xingren/?page={}'.format(i)  # 行人
            html_data = self.request(url)
            pricture_data = self.data_str(html_data)
            self.processing_data(pricture_data)
            print('第', i, '页', num)
            time.sleep(10)
            for pic_url in self.p_url_list:
                num += 1
                pict_jpg = self.request('https:' + pic_url)
                with open(r'G:\vcg_picture\行人\{}.jpg'.format(num), 'wb') as f:
                    f.write(pict_jpg)


def r_pricture():
    r = Pricture()
    r.run_spider()
    # phrase_list = ['教师', '建筑', '行人', '士兵']
    # url = 'https://www.vcg.com/creative-image/300/?page=2'
    # r.request(url)


if __name__ == '__main__':
    r_pricture()
















