import re, os, redis
import socket
import asyncio
import time
from pyppeteer.launcher import launch  # 控制模拟浏览器用
import random, numpy


def get_ip():
    addrs = socket.getaddrinfo(socket.gethostname(), "")
    match = re.search("'192.168.\d+.(\d+)'", str(addrs))
    ip_num = "000"
    if match:
        ip_num = match.group(1)
    return ip_num


def connect(name_ip,password):
    name = "宽带连接"
    username = '{}'.format(name_ip)
    password = '{}'.format(password)
    cmd_str = "rasdial %s %s %s" % (name, username, password)
    res = os.system(cmd_str)
    if res == 0:
        print("连接成功")
    else:
        print(res)


def disconnect():
    name = "宽带连接"
    cmdstr = "rasdial %s /disconnect" % name
    os.system(cmdstr)
    print('断开成功')


def huan_ip(name, password):
    # 断开网络
    disconnect()
    # 开始拨号
    connect(name, password)


class smt_pz_info(object):
    def __init__(self):
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True, password="nriat.123456")
        self.cache_queue = 'smt_pzinfo_cache_queque'
        self.main_queue = "smt_pzinfo"
        self.page = None
        self.browser = None
        # self.huan_ip()

    def run_task(self, url):
        await self.main(url)

    async def main(self, url):  # 定义main协程函数，
        # 以下使用await 可以针对耗时的操作进行挂起
        self.browser = await launch({'headless': False, 'args': ['--no-sandbox'], 'dumpio': True, "userDataDir": r"D:\spider_data\taobao_pyppeteer"})
        browser_context = await self.browser.createIncognitoBrowserContext()
        self.page = await browser_context.newPage()  # 启动个新的浏览器页面
        await self.login(url)

    async def login(self, url):
        # url_l = 'https://gianxijj.tmall.com/?spm=a220o.1000855.1997427721.d4918089.637d72dbEyNoaD'
        url_l = 'https://{}'.format(url)
        await self.page.goto(url_l)  # 访问登录页面
        await self.page.evaluate(
            '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果。
        time.sleep(3)
        pege_text = await self.page.content()  # 获取网页源码
        shop_name = re.search(r'点击查看变更信息', pege_text)
        if shop_name !=None:
            print(shop_name.group())
        # self.page.click()


if __name__ == "__main__":
    get = smt_pz_info()
    with open(r'tmall_shop_url.txt', 'r', encoding='utf-8') as f:
        for i in f:
            url = i.strip('\n')
            get.run_task(url)
