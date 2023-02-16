import re, os, redis
import socket
import asyncio
import time
from pyppeteer.launcher import launch  # 控制模拟浏览器用
import random, numpy
from pyppeteer.errors import TimeoutError


def get_ip():
    addrs = socket.getaddrinfo(socket.gethostname(), "")
    match = re.search("'192.168.\d+.(\d+)'", str(addrs))
    ip_num = "000"
    if match:
        ip_num = match.group(1)
    return ip_num


def connect(account,password):
    name = "宽带连接"
    username = '{}'.format(account)
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


def huan_ip(name,password):
    # 断开网络
    disconnect()
    # 开始拨号
    connect(name,password)


class smt_pz_info(object):
    def __init__(self):
        self.page = None
        self.browser = None
        # self.huan_ip()

    # 检测当前程序进程pid,并存入文本中
    def write(self):
        pid = os.getpid()
        with open('pid.txt', 'w', encoding='utf-8') as f:
            f.write(str(pid))

    # ----------------------自动拨号更换IP-----------------------------

    def run(self):
        # 领取并执行采集任务
        print('--------------------------开始采集--------------------------')
        while True:
            self.run_task()

    def run_task(self):
        while True:
            loop = asyncio.get_event_loop()  # 协程，开启个无限循环的程序流程，把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
            loop.run_until_complete(self.main())
            time.sleep(10)

    async def main(self):  # 定义main协程函数，
        self.browser = await launch(options={'headless': False, 'args': ['--no-sandbox'], "userDataDir": r"D:\spider_data\taobao_pyppeteer"})  # 启动pyppeteer 属于内存中实现交互的模拟器 process.stdout 和 process.stderr 对象，默认是 False。
        browser_context = await self.browser.createIncognitoBrowserContext()
        self.page = await browser_context.newPage()  # 启动个新的浏览器页面
        await self.login()
        await self.page.close()
        await self.browser.close()

    async def goto_page_txt(self):  # 测试废弃，从文本得到shopid

        num = 0
        with open(r"C:\Users\Administrator\Desktop\{smt_shopid}[shopid].txt", "r", encoding="utf-8") as f:
            for i in f:
                print(num)
                num += 1
                i = i.strip()
                await self.get_page(i)

    async def login(self,):
        smt_name = 'tb95487286'
        smt_pw = 'chai0001566764'
        url = 'https://login.taobao.com/member/login.jhtml?style=mini&css_style=b2b&from=b2b&full_redirect=true&redirect_url=https://login.1688.com/member/jump.htm?target=https://login.1688.com/member/marketSigninJump.htm?Done=http://login.1688.com/member/taobaoSellerLoginDispatch.htm&reg= http://member.1688.com/member/join/enterprise_join.htm?lead=http://login.1688.com/member/taobaoSellerLoginDispatch.htm&leadUrl=http://login.1688.com/member'
        await self.page.goto(url)  # 访问登录页面
        await self.page.evaluate(
            '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果。
        await self.page.type('#fm-login-id', smt_name, {'delay': self.input_time_random() - 50})
        await self.page.type('#fm-login-password', smt_pw, {'delay': self.input_time_random()})
        # slider = await self.page.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块
        slider = 0
        if slider:
            print('当前页面出现滑块')
            # await page.screenshot({'path': './headless-login-slide.png'}) # 截图测试
            statue = await self.mouse_slide()  # js拉动滑块过去。
            if statue:
                # await page.keyboard.press('Enter')  # 确保内容输入完毕，少数页面会自动完成按钮点击
                print("print enter", statue)
                await self.page.evaluate(
                    '''document.querySelector(".fm-button").click()''')  # 如果无法通过回车键完成点击，就调用js模拟点击登录按钮。
                await self.page.waitForNavigation()
        else:
            await self.page.keyboard.press('Enter')
            print("print enter")
            await self.page.evaluate(
                '''document.querySelector(".fm-button").click()''')
            try:
                await self.page.waitForNavigation()
            except TimeoutError as te:
                print(te)

    async def get_page(self, id):
        try:
            url = "https://sellerjoin.aliexpress.com/credential/showcredential.htm?storeNum={}".format(id)
            await self.page.goto(url)
            await self.page.evaluate(
                '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果。
            await asyncio.sleep(1)
            statue = await self.mouse_slide()
            # await page.waitForNavigation()
            shopid = id
            if statue:
                company_dict = {"shopid": shopid,
                                "Company name：": "",
                                "VAT number：": "",
                                "registration number：": "",
                                "Address：": "",
                                "Corporate：": "",
                                "Scope：": "",
                                "Established：": "",
                                "authority：": ""}
                content = await self.page.content()
                if "No Data" in content:
                    return 1,company_dict
                elif "information" in content and "something's wrong" not in content:
                    text_elements = await self.page.xpath('//div[@id="container"]/div')
                    for item in text_elements:
                        title_str = await (await item.getProperty('textContent')).jsonValue()
                        for text_i in company_dict:
                            if text_i in title_str:
                                data = title_str.split(text_i)[-1].strip()
                                data = data.replace(",", "，")
                                data = data.replace("\n", "")
                                company_dict[text_i] = data
                    return 1,company_dict
                else:
                    return 0,{}
            else:
                return 0, {}
        except Exception as e:
            print(e)
            return 0, {}


    # 获取登录后cookie
    async def get_cookie(self,page):
        # res = await page.content()
        cookies_list = await page.cookies()
        cookies = ''
        for cookie in cookies_list:
            str_cookie = '{0}={1};'
            str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
            cookies += str_cookie
        print(cookies)
        return cookies

    def get_path(self,distance):
        result = []
        current = 0
        mid = distance * 4 / 5
        t = 0.2
        v = 0
        while current < (distance - 10):
            if current < mid:
                a = 2
            else:
                a = -3
            v0 = v
            v = v0 + a * t
            s = v0 * t + 0.5 * a * t * t
            current += s
            result.append(round(s))
        return result

    def random_linspace(self,num, length):
        '''辅助函数
        传入要分成的几段 -> num ；长度 -> length, 生成一个递增的、随机的、不严格等差数列
        '''
        # 数列的起始值 、 结束值。 这里以平均值的 0.5 作为起始值，平均值的 1.5倍作为结束值。
        start, end = 0.5 * (length / num), 1.5 * (length / num)
        # 借助三方库生成一个标准的等差数列，主要是得出标准等差 space
        origin_list = numpy.linspace(start, end, num)
        space = origin_list[2] - origin_list[1]
        # 在标准等差的基础上，设置上下浮动的大小，（上下浮动10%）
        min_random, max_random = -(space / 10), space / 10
        result = []
        # 等差数列的初始值不变，就是我们设置的start
        value = start
        # 将等差数列添加到 list
        result.append(value)
        # 初始值已经添加，循环的次数 减一
        for i in range(num - 1):
            # 浮动的等差值 space
            random_space = space + random.uniform(min_random, max_random)
            value += random_space
            result.append(value)
        return result

    def slide_list(self,total_length):
        '''等差数列生成器，根据传入的长度，生成一个随机的，先递增后递减，不严格的等差数列'''
        # 具体分成几段是随机的
        total_num = random.randint(10, 15)
        # 中间的拐点是随机的
        mid = total_num - random.randint(3, 5)
        # 第一段、第二段的分段数
        first_num, second_num = mid, total_num - mid
        # 第一段、第二段的长度，根据总长度，按比例分成
        first_length, second_length = total_length * (first_num / total_num), total_length * (second_num / total_num)
        # 调用上面的辅助函数，生成两个随机等差数列
        first_result = self.random_linspace(first_num, first_length)
        second_result = self.random_linspace(second_num, second_length)
        # 第二段等差数列进行逆序排序
        slide_result = first_result + second_result[::-1]
        # 由于随机性，判断一下总长度是否满足，不满足的再补上一段
        if sum(slide_result) < total_length:
            slide_result.append(total_length - sum(slide_result))
        return slide_result

    def retry_if_result_none(self,result):
        return result is None

    async def mouse_slide(self):
        await asyncio.sleep(1)
        try:
            # 鼠标移动到滑块，按下，滑动到头（然后延时处理），松开按键
            await self.page.hover('#nc_1_n1z')  # 不同场景的验证码模块能名字不同。
            await self.page.mouse.down()
            # for x in get_path(5)
            a = self.page.mouse._x
            for i in self.slide_list(500):
                a += i
                await self.page.mouse.move(a, 0, )
            await self.page.mouse.up()
        except Exception as e:
            print(e, ':验证失败')
            return None
        else:
            await asyncio.sleep(1)
            return 1

    def input_time_random(self):
        return random.randint(100, 151)


if __name__ == "__main__":
    # python配置文件路径
    ip = get_ip()
    if ip in [59, 56, 98, 99]:
        ADSL_name = "057762355592"
        ADSL_pwd = "928858"
    else:
        ADSL_name = "057762355594"
        ADSL_pwd = "045805"
    get = smt_pz_info()
    get.run()
