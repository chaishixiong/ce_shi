import re, os, redis
import socket
import asyncio
import time
from pyppeteer.launcher import launch  # 控制模拟浏览器用


def get_ip():
    addrs = socket.getaddrinfo(socket.gethostname(), "")
    match = re.search("'192.168.\d+.(\d+)'", str(addrs))
    ip_num = "000"
    if match:
        ip_num = match.group(1)
    return ip_num


def connect(name, password):
    name = "宽带连接"
    username = '{}'.format(name)
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
        self.cache_queue = 'tmall_shop_url_queque'
        self.main_queue = "tmall_shop_url"
        self.page = None
        self.browser = None
        self.url = ''
        # self.huan_ip()

    def run(self):
        # with open(r'C:\Users\Administrator\Desktop\测试\mei_tuan\tmall_shop_url.txt', 'r', encoding='utf-8') as f:
        #     for i in f:
        #         url = 'https://{}'.format(i.strip('\n'))
        #         self.r.sadd(self.main_queue, url)
        # 领取并执行采集任务
        print('--------------------------开始采集--------------------------')
        while True:
            if self.r.exists(self.main_queue):
                self.run_task()
            else:
                print('------未找到任务队列--------')
                time.sleep(60)
                break
            time.sleep(60)

    def run_task(self):
        while True:
            loop = asyncio.get_event_loop()  # 协程，开启个无限循环的程序流程，把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
            loop.run_until_complete(self.main())
            time.sleep(10)

    async def main(self):  # 定义main协程函数，
        # 以下使用await 可以针对耗时的操作进行挂起
        self.browser = await launch({'headless': False, 'args': ['--no-sandbox'], 'dumpio': True,
                                     "userDataDir": r"D:\spider_data\taobao_pyppeteer"})  # 启动pyppeteer 属于内存中实现交互的模拟器 process.stdout 和 process.stderr 对象，默认是 False。
        browser_context = await self.browser.createIncognitoBrowserContext()
        self.page = await browser_context.newPage()  # 启动个新的浏览器页面
        # await self.page.setUserAgent(
        #     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
        await self.goto_page()
        await self.page.close()
        await self.browser.close()

    async def goto_page(self):
        # ip = get_ip()
        file = open(r'C:\Users\Administrator\Desktop\测试\mei_tuan\企业变更店铺.txt', 'a', encoding='utf-8')
        file_cuowu = open(r'C:\Users\Administrator\Desktop\测试\mei_tuan\错误店铺.txt', 'a', encoding='utf-8')
        while True:
            # ---------------------------------------------------------------------
            shop_id = self.r.spop(str(self.main_queue))
            # 将获取的数据存储到另外一个集合中，防止程序中途停止导致数据丢失
            try:
                yes_on = await self.get_page(shop_id)
                if yes_on == "是":
                    file.write(shop_id + '\n')  # 保存文本
                    file.flush()
                elif yes_on == "错误":
                    file_cuowu.write(shop_id + '\n')  # 保存文本
                    file_cuowu.flush()
            except Exception as e:
                print(shop_id)

    async def get_page(self, id):
        url = id
        await self.page.goto(url)
        await self.page.evaluate(
            '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果。
        data_txt = await self.page.content()  # 获取网页源码
        shop_name = re.search(r'点击查看变更信息', data_txt)
        login = re.search(r'密码登录', data_txt)
        none_shop = re.search(r'没有找到相应的店铺信息', data_txt)
        await asyncio.sleep(2)
        if shop_name != None:
            print(shop_name.group())
            return "是"
        elif login != None:
            return "错误"
        elif none_shop != None:
            return "错误"
        else:
            return "不是"


if __name__ == "__main__":
    get = smt_pz_info()
    get.run()


