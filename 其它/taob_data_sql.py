import requests
import re


title_list = ['浙江省教育经费统计执行情况', '浙江省高校优秀教师信息', '浙江省教育经费统计执行情况']

for title in title_list:
    url = 'http://search.zj.gov.cn/jrobotfront/interfaces/cateSearch.do'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "x-requested-with": "XMLHttpRequest"
    }
    params = {
        'websiteid': '330000000000007',
        'tpl': '2330',
        'sortType': '2',
        'q': title,
        'cateid': '370',
        'pg': '10'
    }
    r = requests.get(url=url, headers=headers, params=params)
    d = r.content.decode()
    url_list = re.findall(r'[a-zA-z]+://[^\s]*', d)
    for url in url_list:
        url_l = re.search(r'[a-zA-z]+://[^\s]*', url).group()
    print(d)

