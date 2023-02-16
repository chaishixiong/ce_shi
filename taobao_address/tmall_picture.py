import requests
import base64


def access_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=A7bq2cHRhByDDjLAIx6HETdG&client_secret=a7C2wLUxKARL9Y1xutqFEy0hqoQkGFiR'
    response = requests.get(host)
    if response:
        accesstoken = response.json()
        access_token = accesstoken['access_token']
        print(accesstoken)
        return access_token


def picture_data(pict_name):
    '''
    通用文字识别（高精度版）
    '''
    # access_token()
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/webimage"
    # 二进制方式打开图片文件
    f = open(pict_name, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    accesstoken = '24.112672c2836254f99482cb4c7eed7bb0.2592000.1664074349.282335-27169308'
    request_url = request_url + "?access_token=" + accesstoken
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.text)
        return response.text


if __name__ == '__main__':
    import re
    a = '润元医疗器械专营店.png'
    # picture_data(a)
    aaa = re.search(r'(.*?).png', a)
    print(aaa.group(1))
