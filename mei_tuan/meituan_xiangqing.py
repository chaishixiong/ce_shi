# --*--coding: utf-8 --*--
import re
import requests
import redis
import time


class MeTuanXiangQing(object):
    def __init__(self):
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True, password="nriat.123456")
        self.key_id = "meitun_shop_id"
        self.shopid = ''

    def request_xingqing(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'cookie': '_samesite_flag_=true; cookie2=109d0fa17f3d42892ec7292bd5dbc17e; t=35624d2d5712d90f9512cdf717a17a21; _tb_token_=fe4471b5efeb8; cna=8nlmG9B89CkCAXrrxL/k5zg6; xlly_s=1; sgcookie=E100gPH0fk5hctjq%2FUurFJlfQJ5c6isVWzDEpu8ZKUfqeyWu8uECrbiYDn3hi9QZWSZHhENgYHCYUiQuO8xdPa9SaXJ6bYdYbGlmx6p5YEmjJtKqWHzHF1sBfV5MecGo6ZkJ; unb=2939628735; uc1=cookie21=WqG3DMC9Fbk9noNn3aVF&existShop=true&cookie14=UoexOtZG9aiA0A%3D%3D&pas=0&cookie15=W5iHLLyFOGW7aA%3D%3D&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D; uc3=nk2=AHLWi99bKHhvbGaJhn7t1F6F1A%3D%3D&id2=UUGhZWhFdIbxug%3D%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D&vt3=F8dCv4JhT8mRmPELey0%3D; csg=02fc1996; lgc=changliuhai63756878; cancelledSubSites=empty; cookie17=UUGhZWhFdIbxug%3D%3D; dnk=changliuhai63756878; skt=b9ce35213b338421; existShop=MTY1ODgxNzU4MQ%3D%3D; uc4=nk4=0%40AhyAi1SKbIeVCqbfRCDcqRk%2BVMT%2FQ%2BxL5Td%2FseRP&id4=0%40U2OW57HlZ9Ma4p44zPKAWYZPAxL3; tracknick=changliuhai63756878; _cc_=UIHiLt3xSw%3D%3D; _l_g_=Ug%3D%3D; sg=856; _nk_=changliuhai63756878; cookie1=B0BbjKS7HkQwGor1iRTipR6l6FNnkzcraBKNBk44EtQ%3D; enc=GXPsPGKyC1dkiI8yJ0OmeUwHNsOQuzX0EHuz9PtNWBjsM9SJSaPq0ZAn8dTxcKIs1G3CZhFGwqT0CbWZ2a28CA%3D%3D; thw=cn; isg=BFZW_cdoKP6FBhxafAdPzE5EpwxY95oxB4a9HMC_QjnUg_YdKIfqQbxxGx9vMJJJ; tfstk=cpWdBP2uxP4HRddXNMFMaRsPIXUcwRFpWDtteTSfps-RJF1mFtXx6hNB7E8LX; l=eBE4NRfuL9CFS1eDBOfanurza77OSIRYYuPzaNbMiOCPO7fB5NrPW6v3amL6C3GVh63HR3Wrj_IwBeYBqQAonxv98yvNIODmn'
        }
        url = 'https://meishi.meituan.com/i/poi/{}'.format(self.shopid)
        response = requests.get(url, headers=headers)
        return response

    def write_data(self, response):
        response_data = response.text
        all_comment_num = re.search('"MarkNumbers":(.*?),"scoreSource"', response_data)
        if all_comment_num:
            all_comment = all_comment_num.group(1)
        else:
            all_comment = '0'
        data_item = [self.shopid, all_comment]
        with open('shop_all_comment_num.txt', 'a', encoding='utf-8') as f:
            f.write(','.join(data_item) + '\n')
            f.flush()

    def run_xingqing_spider(self):
        while True:
            try:
                if self.r.exists(self.key_id):
                    self.shopid = self.r.spop(self.key_id)
                    responds = self.request_xingqing()
                    self.write_data(responds)
                else:
                    print('------未找到任务队列--------')
                    time.sleep(60)
                    break
            except Exception as e:
                print(e)


if __name__ == '__main__':
    run = MeTuanXiangQing()
    run.run_xingqing_spider()


