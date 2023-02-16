import requests
from lxml import etree
import re
import time
import os


class XKWZhiShiDian(object):
    def __init__(self):
        self.pag_url = 'https://zujuan.xkw.com/gzyw/zsd184937/o2p{}'
        self.os_path = 'F:\学科网\语文\词语—词性'
        self.folio_name = ''

    def request(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            'Cookie': '__RequestVerificationToken=RLe-zcXj4BtrHWoHcMAMgnrM4sXDq7XQSzx3IuY6xbiQ_tGPrDDioizBi9ysyUrs3JksU0zEQYi5ZwSjLi9amgbtxz41; UM_distinctid=17deaf6d4d2106e-0ee8c59bd1e6b3-2343360-240000-17deaf6d4d396b; xkw-device-id=2C10D952A05701734E6B0C90700FB4BD; downSetting=%7B%22docVersion%22%3A%22pdf%22%2C%22paperSize%22%3A%22A4%22%2C%22paperType%22%3A%22normal%22%7D; bankname=czyw; Zujuan=D3BF9E3534FBB5F90D30378005F8B9264D1D6C6B3F6888D173ADF75EBDC2D2AE483F4B0AD290FFD577AEB4D3667C1CB83FE0326A1E370F540B75525D44705935DF73D174577A14E45A740DAD423CF8F5D65080C8939A2904B1F8AA3918B1808197B9AF1747BD22A3D60C2C396D540A78282ED4ACD92FE435DD417007B3033B14F899059DBB64BDE57615FF5414C4E60775E88338E9FA1903A50DF2553E03B95E3FDC5EB8; userId=59667805; usert=21f106daca2889e180fccf2998980bf8; username=%e5%8d%97%e6%b5%a601; manager=200002; schoolName=%e6%b8%a9%e5%b7%9e%e5%b8%82%e5%8d%97%e6%b5%a6%e5%ae%9e%e9%aa%8c%e4%b8%ad%e5%ad%a6; productparams_renew=%5b%7b%22eduid%22%3a2%2c%22renew%22%3a0%7d%2c%7b%22eduid%22%3a3%2c%22renew%22%3a0%7d%5d; userGuid=8f775d4e-cb07-4457-8c64-3375dbea0bc2; user_token=eyJ1c2VySWQiOiI1OTY2NzgwNSIsInVzZXJfdG9rZW4iOiJ2U3l5RnQ3eSJ9; zjut=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjU5NjY3ODA1LCJwd2QiOiIyMWYxMDZkYWNhMjg4OWUxODBmY2NmMjk5ODk4MGJmOCJ9.fI6-t-n2Dd7C6ngoGoswZsDL6cS3-eUFTehPu0K_P_g; Hm_lvt_68fb48a14b4fce9d823df8a437386f93=1640339017,1640757925,1640758179,1640827164; isshowAnswer=false; CNZZDATA1274198201=208625024-1640319147-https%253A%252F%252Fyw.zxxk.com%252F%7C1640837650; bankId=10; quesBasketVersion=1640758197437; ip2ProvinceId=-1; filter_pts=%2fgzyw%2fzsd23186%2fpts1o2%2f; filter_ds=%2fgzyw%2fzsd23186%2fds1o2%2f; Hm_lpvt_68fb48a14b4fce9d823df8a437386f93=1640844876'
        }
        r = requests.get(url=url, headers=headers)
        return r

    def re_picture_png(self, url_list):
        ii = 0
        for url in url_list:
            ii += 1
            write_png = self.request(url)
            path_pp = self.folio_name + '\{}.png'.format(ii)
            with open(path_pp, 'wb') as f:
                f.write(write_png.content)
                f.close()

    def mkdir(self, path):

        folder = os.path.exists(path)

        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            print("---  new folder...  ---")
        else:
            print("文件已存在")

    def data_list(self, response):
        list_data_list = []
        list_img_list = []
        difficulty_list = []
        r_html = etree.HTML(response.text)
        len_len = r_html.xpath('//*[@class="test-list"]/div/div/div/span[2]/span/text()')
        for n in range(1, len(len_len) + 1):
            list_data = r_html.xpath('//*[@class="test-list"]/div[{}]//div[@class="exam-item__cnt"]//text()'.format(n))
            list_img = r_html.xpath('//*[@class="test-list"]/div[{}]//div[@class="exam-item__cnt"]//img/@src'.format(n))
            difficulty = r_html.xpath('//*[@class="test-list"]/div[{}]/div/div/span[2]/span/text()'.format(n))[0]
            list_data_list.append(list_data)
            list_img_list.append(list_img)
            difficulty_list.append(difficulty)
        return list_data_list, list_img_list, difficulty_list

    def one_data_list(self, list_data, n, path_path, difficulty):
        difficulty_title = '题目难易程度：{}'.format(difficulty) + '\n'
        data_str = ''
        for data in list_data:
            data_str += str(data)
        self.folio_name = path_path + '\第{}题'.format(n)
        self.mkdir(self.folio_name)
        path_p = self.folio_name + '\题目.txt'
        with open(path_p, 'w', encoding='utf-8') as f:
            f.write(difficulty_title)
            f.write(data_str)
            f.close()

    def run_spider(self):
        for i in range(1, 21):
            response = self.request(self.pag_url.format(i))
            time.sleep(7)
            list_data_list, list_img_list, difficulty_list = self.data_list(response)
            folio_pag_name = '\第{}页'.format(i)
            path_path = self.os_path + folio_pag_name
            self.mkdir(path_path)
            print(folio_pag_name)
            n = 0
            for list_data, list_img_url, difficulty in zip(list_data_list, list_img_list, difficulty_list):
                n += 1
                self.one_data_list(list_data, n, path_path, difficulty)
                self.re_picture_png(list_img_url)


def run_xuekewang():
    run = XKWZhiShiDian()
    run.run_spider()
    # url = 'https://zujuan.xkw.com/gzsx/zsd27925/o2p1/'
    # r = run.request(url)
    # a = run.data_list(r)
    print()


if __name__ == '__main__':
    run_xuekewang()




















