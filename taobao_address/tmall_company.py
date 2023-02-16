import os
import requests
import base64
import re


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
        return response.text


def tmall_pic_data(data_pic):
    compay_name = re.search(r'企业名称:(.*?)"}', data_pic)
    address = re.search(r'主所:(.*?)"}|所:(.*?)"}', data_pic)
    compayname = ''
    addressname = ''
    if compay_name:
        compay_name_group1 = compay_name.group(1)
        if compay_name_group1:
            compayname = compay_name_group1
    if address:
        address_name_group1 = address.group(1)
        address_name_group2 = address.group(2)
        if address_name_group1:
            addressname = address_name_group1
        elif address_name_group2:
            addressname = address_name_group2
    return compayname, addressname


def run_tmall_pic_data():
    file_dir = "D:\影刀\图片\天猫企业信息图片"
    data_name = open(r'data_data.txt', 'a', encoding='utf-8')
    for root, dirs, files in os.walk(file_dir, topdown=False):
        for pict_name in files:
            pict_name_f = file_dir + '\\' + pict_name
            data_pic = picture_data(pict_name_f)
            compayname, addressname = tmall_pic_data(data_pic)
            shop_name = re.search(r'(.*?).png', pict_name).group(1)
            if 'shop' in addressname:
                province = ''
                city = ''
                county = ''
            elif len(addressname) < 4:
                province = ''
                city = ''
                county = ''
            else:
                province = addressname[0:3]
                city = addressname[3:6]
                county = addressname[6:9]
            data_l = [shop_name, compayname, addressname, province, city, county]
            data_name.write(','.join(data_l) + '\n')


if __name__ == '__main__':
    run_tmall_pic_data()




