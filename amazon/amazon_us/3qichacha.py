import requests
from requests_toolbelt import MultipartEncoder
import time
import os
import re
import xlrd
cookies = input("cookies:")
judge_last = ""
url = "https://www.qcc.com/more_getbatchlist"


def get_batchlist():
    headers_str = '''accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
                    accept-encoding: gzip, deflate, br
                    accept-language: zh-CN,zh;q=0.9
                    cache-control: no-cache
                    pragma: no-cache
                    sec-fetch-mode: navigate
                    sec-fetch-site: none
                    sec-fetch-user: ?1
                    upgrade-insecure-requests: 1
                    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'''
    url = "https://www.qcc.com/more_batchlist"
    headers = headers_todict(headers_str)
    headers["cookie"] = cookies
    num = 0
    while num<5:
        num+=1
        req = requests.get(url,headers=headers)
        match = re.search('''"/firm/[^\.]*\.html" target="_blank">([^<]*)</a>''',req.text)
        # print(match)
        if not match:
            match = re.search('"error errorh0" ?data-name="(.*?)"', req.text)
        if "小查匹配成功"in req.text and match:
            judge_url = match.group(1)
            global judge_last
            if judge_url != judge_last:
                print("查询列表更新了")
                #上传成功了
                time.sleep(1)
                status_excel = atchlist_excel()
                if not status_excel:
                    raise Exception("输出结果错误")
                judge_last = judge_url
                return 1
            else:
                pass
        else:
            pass
        time.sleep(10)


def headers_todict(header_str):
    header = header_str.split("\n")
    headers = {}
    for cookie in header:
        if ":" in cookie:
            cookie_split = cookie.split(":",1)
            name = cookie_split[0].strip()
            values = cookie_split[1].strip()
            headers[name] = values
        else:
            headers[cookie] = ""
    return headers


def atchlist_excel():
    headers_str1 = '''accept: */*
    accept-encoding: gzip, deflate, br
    accept-language: zh-CN,zh;q=0.9
    cache-control: no-cache
    pragma: no-cache
    referer: https://www.qcc.com/more_batchlist
    sec-fetch-mode: cors
    sec-fetch-site: same-origin
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
    x-requested-with: XMLHttpRequest'''
    headers1 = headers_todict(headers_str1)
    headers1["cookie"] = cookies
    url = "https://www.qcc.com/more_batchlistExcel?code="
    num = 0
    while num<5:
        num+=1
        req = requests.get(url, headers=headers1)
        if '"success":true' in req.text:
            print("导出数据成功")
            return 1
        time.sleep(10)


headers_str = '''Host: www.qcc.com
                Connection: keep-alive
                Content-Length: 89001
                Accept: application/json
                Cache-Control: no-cache
                X-Requested-With: XMLHttpRequest
                User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
                Content-Type: multipart/form-data; boundary=----WebKitFormBoundarywaJUeVOITKu1L1Jr
                Origin: https://www.qcc.com
                Sec-Fetch-Site: same-origin
                Sec-Fetch-Mode: cors
                Sec-Fetch-Dest: empty
                Referer: https://www.qcc.com/more_batchsearch  
                Accept-Encoding: gzip, deflate, br
                Accept-Language: zh-CN,zh;q=0.9'''
headers = headers_todict(headers_str)
headers["cookie"] = cookies
now = int(input("输入文件数字："))  # 5000
file_num = int(input("输入文件个数："))
for i in range(now, now+file_num*5000, 5000):
    file_name = "gmnriat{}.xlsx".format(i)
    # `````````````````--------------------------！！！！！！！！-----------------修改要处理的文件名
    path_name = r"D:\Data\工商地址库/10/{}".format(file_name)

    # path_name = r"D:\Data\工商地址库/taobao_add/{}".format(file_name)
    file = open(path_name,"rb")
    file.seek(0)
    data = MultipartEncoder({
    'file': (file_name, file, 'application/octet-stream'),
    }, boundary="----WebKitFormBoundarywaJUeVOITKu1L1Jr")
    req = requests.post(url=url,data=data, headers=headers)
    file.close()
    if '"success":true' in req.text:
        print("{}已上传".format(file_name))
        time.sleep(1)
        status = get_batchlist()
        if not status:
            break
        new_name = path_name.replace(".xlsx","_end.xlsx")
        os.rename(path_name,new_name)
    else:
        print("{}上传失败".format(file_name))
        break
    time.sleep(10)
else:
    print("本cookies所有文件完成")


