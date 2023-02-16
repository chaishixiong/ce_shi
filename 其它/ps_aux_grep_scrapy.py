# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time      : 2018/12/12 9:58
# @Author    : lmh
# @File      : monitor.py
#
#
# import sys
# import psutil
# import datetime
# import time
# import os
# import requests
# import json
#
#
# def monitor(pid):
#     # 设定监控时间  默认3天
#     CYCLE_TIME = datetime.timedelta(weeks=0, days=3, hours=00, minutes=0, seconds=5, microseconds=0,
#                                     milliseconds=0)  # 60*60*24
#     start_time = datetime.datetime.today()
#     # 判断进程是否存在
#     if (psutil.pid_exists(pid)):
#         p = psutil.Process(pid)  # 实例化一个进程
#         pName = p.name()  # 进程名
#         # 设置日志名
#         logName = pName + "_" + str(pid) + "_stress_monitoring_record.log"  # log文件
#         logfile = open(logName, "a")
#     else:
#         print("pid is not exists please enter true pid!!!")
#         return
#     wTime = 30  # 等待时间
#
#     while (True):
#         # 判定监控时间
#         if ((datetime.datetime.today() - start_time) > CYCLE_TIME):
#             break
#
#         recTime = time.strftime('%Y-%m-%d\t%H:%M:%S', time.localtime(time.time()))  # datetime.datetime.today() #记录时间
#
#         # 判断进程是否存在
#         if (psutil.pid_exists(pid)):
#             vmm = p.memory_info().vms  # 虚存 单位字节
#             mm = p.memory_info().rss  # 实际使用内存 单位字节
#             pCpu = p.cpu_percent(interval=1)  # CPU百分比
#             nFiles = len(p.open_files())  # 打开文件数   这个不太准感觉，暂不记录
#             nThreads = p.num_threads()  # 线程数
#             nHandles = p.num_handles()  # 句柄数
#             # 记录进程详细信息
#             monitor_content = str(recTime) + "\t" + str(vmm) + "\t" + str(mm) + "\t" + str(pCpu) + "\t" + str(
#                 nThreads) + "\t" + str(nHandles) + "\n"
#
#         else:
#             monitor_content = str(datetime.datetime.today()) + "\t" + str(pid) + "  is not running!!!!!!!!!\n"
#             break
#
#         print(monitor_content)
#         logfile.flush()
#         logfile.write(monitor_content)  # 写入log文件
#         time.sleep(wTime)  # 循环等待
#
#     logfile.close()
#
#
# def isRunning(process_name):
#     try:
#         print('tasklist | findstr '+process_name)
#         process=len(os.popen('tasklist | findstr '+process_name).readlines())
#         print(process)
#         if process >=1 :
#             return True
#         else:
#             return False
#     except:
#         print("程序错误")
#         return False
#
#
# def sendDingDing(text):
#     print(text)
#     headers = {'Content-Type': 'application/json'}
#     webhook = "https://oapi.dingtalk.com/robot/send?access_token=1036f93e984033ac8f575ad3c035d46b"
#     data = {
#         "msgtype": "text",
#         "text": {
#             "content": text+'\n'
#         },
#         "at": {
#             "atMobiles": [
#
#             ],
#             "isAtAll": False
#         }
#     }
#
#     x = requests.post(url=webhook, data=json.dumps(data), headers=headers)
#
#
# def send_msg(url):
#     headers = {'Content-Type': 'application/json;charset=utf-8'}
#     data = {
#         "msgtype": "link",
#         "link": {
#             "text": '点我跳转百度',
#             "title": "点我",
#             "picUrl": "图片链接",      # 可以加，可以不加
#             "messageUrl": "https://www.baidu.com"
#
#         },
#     }
#     r = requests.post(url, data=json.dumps(data), headers=headers)
#     return r.text
#
#
# if __name__ == '__main__':
#     access_token = '1036f93e984033ac8f575ad3c035d46b'
#     url = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(access_token)
#     text = 'adsadadadsadsd'
#     sendDingDing(text)
#     # print(send_msg(url))


# !/usr/bin/python3
import time
import hmac
import hashlib
import base64
import urllib.parse
import os


def main():
    timestamp = str(round(time.time() * 1000))
    secret = 'nVXJ_qgqGGAEi_wMpm5EaQWH8osNqqspg_9F70c5xwiIslV1376Fv_zS0rJqvTdz'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    # print(timestamp)
    # print(sign)
    webhookurl = 'https://oapi.dingtalk.com/robot/send?access_token=1036f93e984033ac8f575ad3c035d46b' + '&timestamp=' + timestamp + '&sign=' + sign
    os.environ['url'] = webhookurl
    # os.environ['xiantime'] = time.strftime('%H:%M:%S')
    os.environ['xiantime'] = time.ctime()
    os.system(
        ''' curl ${url} -H 'Content-Type: application/json' -d '{"msgtype": "text","text":{"content":"现在时间是 '"$xiantime"'   ！"}}' ''')
    # print(webhookurl)


if __name__ == "__main__":
    main()


