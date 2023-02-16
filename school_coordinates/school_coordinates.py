import requests
from urllib import parse


class SchoolCoordinates(object):
    def __init__(self):
        pass

    def request(self, school_name):
        school_name_utf8 = parse.quote(school_name)
        # url = 'https://apis.map.qq.com/jsapi?qt=geoc&addr=%E8%90%A7%E5%B1%B1%E5%8C%BA%E5%8D%97%E9%83%BD%E5%B0%8F%E5%AD%A6'
        aa = parse.unquote('%E8%90%A7%E5%B1%B1%E5%8C%BA%E5%8D%97%E9%83%BD%E5%B0%8F%E5%AD%A6')
        bb = parse.unquote('%E8%90%A7%E5%B1%B1%E4%BF%A1%E6%81%AF%E6%B8%AF%E5%B0%8F%E5%AD%A6')
        url = 'https://apis.map.qq.com/jsapi?qt=geoc&addr=' + school_name
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        }
        r = requests.get(url, headers=headers)
        data = r.content.decode('utf-8')
        print(r)

    def data_data(self):
        pass

    def run_spider(self):
        with open(r'C:\Users\Administrator\Desktop\测试\school_coordinates\school_name.txt', 'r', encoding='utf-8')as f:
            for i in f:
                school_name = i.strip('\n')
                print(school_name)
                data_dict = self.request(school_name)


def run_school():
    run = SchoolCoordinates()
    run.run_spider()


if __name__ == '__main__':
    run_school()

