import requests
import json


class KaoLaHaiGou(object):
    def __init__(self):
        pass

    def request(self):
        url = 'https://search.kaola.com/api/category/16061/16064.html'
        headers = {
            "content-type": "application/json;charset=UTF-8",
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36',
        }
        data = {
            "pageSize": 100,
            "pageNo": 1,
            "stickGoods": "",
            "bucketIds": "",
            "sortType": 0,
            "desc": 1,
            "categoryId": "16061",
            "subCategoryId": "16064"
        }
        r = requests.post(url=url, headers=headers, data=json.dumps(data))
        data_dict = r.content.decode()
        print(data_dict)

    def goods_list(self):
        pass

    def kaola_data(self):
        pass

    def run_spider(self):
        self.request()


def run_kaola():
    run = KaoLaHaiGou()
    run.run_spider()


if __name__ == '__main__':
    run_kaola()




