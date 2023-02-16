import requests
import json
import time


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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        r = requests.get(url=url, headers=headers)
        data = r.content
        return data

    def processing_data(self, pricture_data):
        data_dict = json.loads(pricture_data)
        data_list = data_dict['list']
        for pict_data in data_list:
            pict_url = pict_data.get('url800')
            if pict_url != None:
                self.p_url_list.append(pict_url)

    def run_spider(self):
        num = 0
        for i in range(1, 61):
            url = 'https://www.vcg.com/api/common/searchAllImage?page={}&phrase=%E5%A3%AB%E5%85%B5'.format(i)  # 士兵
            pricture_data = self.request(url)
            self.processing_data(pricture_data.decode())
            print('第', i, '页', num)
            time.sleep(10)
            for pic_url in self.p_url_list:
                num += 1
                pict_jpg = self.request('https:' + pic_url)
                with open(r'G:\vcg_picture\士兵\{}.jpg'.format(num), 'wb') as f:
                    f.write(pict_jpg)


def r_pricture():
    r = Pricture()
    r.run_spider()
    # phrase_list = ['教师', '建筑', '行人', '士兵']


if __name__ == '__main__':
    r_pricture()
















