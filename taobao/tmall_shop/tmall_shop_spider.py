import re
import time
import os
import pandas as pd
import base64

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



from bs4 import BeautifulSoup
from PIL import Image

# from fateadm_api import FateadmApi


EXCEL_PATH="src/excel"
SCREENSHOT_PATH="src/temp_screenshot.png"
CAPTCHA_PATH="src/temp_captcha.png"


class TmallShopSpider(object):
    def __init__(self, username, password, chromedriver_path):
        self.url = 'https://login.taobao.com/member/login.jhtml'  # 淘宝登录地址
        self.username = username  # 接收传入的 账号
        self.password = password  # 接收传入的 密码
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片，加快访问速度
        options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 设置为开发者模式，防止被各大网站识别出来使用了Selenium
        self.browser = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)  # 接收传入的 chromedriver地址 和设置好的 options
        self.browser.maximize_window()  # 设置窗口最大化
        self.wait = WebDriverWait(self.browser, 10)  # 设置一个智能等待为10秒

    def login(self,on_login_web):
        if not on_login_web:
            self.browser.get(self.url)
        # username_password_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.login-box.no-longlogin.module-quick > .hd > .login-switch')))  # 用css选择器选择 用账号密码登录按钮
        # username_password_button.click()  # 点击 用账号密码登录按钮
        weibo_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))  # 用css选择器选择 用微博登录按钮
        weibo_button.click()  # 点击 用微博登录按钮
        input_username = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="username"]')))  # 用xpath选择器选择 账号框
        input_username.send_keys(self.username)  # 输入 账号
        input_password = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))  # 用xpath选择器选择 密码框
        input_password.send_keys(self.password)  # 输入 密码
        time.sleep(10)
        try:
            captcha=self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="verifycode"]')))
            # 处理登录验证码
        except:
            print("无验证码，直接登录")
        login_button = self.wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="登录"]')))  # 用xpath选择器选择 登录按钮
        login_button.click()  # 点击 登录按钮


    def getPageTotal(self):
        # 存在登录后进入滑动验证码页面的情况，此时无法获取页数，做法是回退一步再次登录
        try:
            page_total = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-page-skip > form')))  # 用css选择器选择 商品列表页 总页数框
            page_total = page_total.text
            page_total = re.match('.*?(\d+).*', page_total).group(1)  # 清洗
            return page_total
        except:
            if self.sliderVerification():
                # self.browser.back()
                self.login(on_login_web=True)
                return self.getPageTotal()


    def dropDown(self):
        # 模拟人类 向下滑动浏览（下拉有加速度）
        for i in range(1, 52):
            drop_down = "var q=document.documentElement.scrollTop=" + str(i*100)
            self.browser.execute_script(drop_down)
            time.sleep(0.01)
            if i == 5:
                time.sleep(0.7)
            if i == 15:
                time.sleep(0.5)
            if i == 29:
                time.sleep(0.3)
            if i == 44:
                time.sleep(0.1)
        # 直接下拉到最底部
        # drop_down = "var q=document.documentElement.scrollTop=10000"
        # self.browser.execute_script(drop_down)

    def nextPage(self):
        # 获取 下一页的按钮 并 点击
        next_page_submit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-page-next')))
        next_page_submit.click()

    def sliderVerification(self):
        # 滑块验证有滑动，但验证失败，失败后人工滑动验证也会失败

        # 每次翻页后 检测是否有 滑块验证
        try:
            slider_button = WebDriverWait(self.browser, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'nc_1_n1z')))
            # action = ActionChains(self.browser)
            # action.click_and_hold(slider_button).perform()
            # action.reset_actions()
            # # 模拟人类 向左拖动滑块（拖动有加速度）
            # for i in range(100):
            #     action.move_by_offset(i*1, 0).perform()
            #     time.sleep(0.01)
            # action.reset_actions()

            # 尝试出现验证码后返回上一页
            self.browser.back()
            return True
        except:
            print('没有检测到滑块验证码')
            return False

    def crawlShops(self, category):
        # self.login(on_login_web=False)
        self.browser.get('https://list.tmall.com/search_product.htm?q={0}'.format(category))  # 天猫商品列表页地址，format()里面输入要爬取的类目
        shop_button=self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.fType-w ')))
        shop_button.click()
        self.login(on_login_web=True)
        page_total = self.getPageTotal()  # 获取 商品列表页 总页数
        print(''.join(['爬取的类目一共有：', page_total, '页']))
        shop_data=[]
        for page in range(2, int(page_total)):  # 遍历 全部 商品列表页
            page_frame = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-page-skipTo')))  # 获取 当前页数框
            page_now = page_frame.get_attribute('value')  # 获取 当前页数
            print(''.join(['当前页数：', page_now, ' ', '总页数：', page_total]))
            html = self.browser.page_source  # 获取 当前页面的 源代码
            soup=BeautifulSoup(html,'lxml')
            shop_list=soup.find_all(class_="shopHeader-info")
            for shop in shop_list:
                one_data={}
                one_data['种类']=category
                one_data["店名"]=shop.find(class_="sHi-title").text
                one_data["链接"]="https://list.tmall.com/"+shop.find(class_="sHi-title")['href']
                one_data["页数"]=page_now
                shop_data.append(one_data)
                pd.DataFrame(shop_data).to_excel(category+".xlsx")

            self.dropDown()  # 执行 下拉动作
            self.nextPage()  # 执行 按下一页按钮动作
            time.sleep(1)
            self.sliderVerification()  # 检测是否有 滑块验证
            time.sleep(1)
            self.checkNotFoundWebPage()
            time.sleep(1)
        pd.DataFrame(shop_data).to_excel(category+".xlsx")

    def checkNotFoundWebPage(self):
        # 翻页时有时会出现无法找到相关店铺的页面，但其实还不是最后一页店铺，
        # 此时按返回上一步再次进入下一页
        try:
            search_tip = WebDriverWait(self.browser, 5, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.searchTip-kw')))

            # 尝试出现验证码后返回上一页
            self.browser.back()
            return True
        except:
            print('没有检测到无法搜索店铺的页面')
            return False

    def getShopList(self):
        # 从excel中读取店铺名字与链接
        data_path=os.path.join(EXCEL_PATH,self.keyword+".xlsx")
        if not os.path.exists(data_path):
            raise Exception("找不到关于【"+self.keyword+"】的excel表，程序结束")
        shop_list=pd.DataFrame(pd.read_excel(data_path))

        col_names = shop_list.columns.tolist()
        if "资质信息图片位置" not in col_names:
            col_names.append("资质信息图片位置")
            # print(col_names)
            shop_list = shop_list.reindex(columns=col_names)
            shop_list.to_excel(data_path)
            shop_list = pd.DataFrame(pd.read_excel(data_path))

        pic_col=[]
        for i,shop in shop_list.iterrows():
            if os.path.exists(os.path.join("src","pic",self.keyword,shop["店名"]+".png")):
                 pic_col.append(os.path.join("src","pic",self.keyword,shop["店名"]+".png"))
            else:
                pic_col.append("nan")
        shop_list["资质信息图片位置"]=pic_col
        shop_list.to_excel(data_path)
        return shop_list

    def getAllShopPublicInfo(self,keyword):
        self.keyword=keyword

        # 更新文件夹
        if not os.path.exists(os.path.join("src","pic",keyword)):
            os.mkdir(os.path.join("src","pic",keyword))

        # 获取从excel表中读取的所有店铺的经营者相关资质信息
        shop_list = self.getShopList()

        for i, shop in shop_list.iterrows():
            print(shop["资质信息图片位置"])
            if str(shop["资质信息图片位置"])!="nan":
                # 已经下载了资质信息图片
                print("跳过一家店铺")
                continue
            self.getShopPublicInfo(shop)

    def getShopPublicInfo(self,shop):
        # 获取一个店铺的经营者相关资质信息
        print("正在获取店铺 "+shop["店名"]+" 的资质信息")
        self.current_shop_name=shop["店名"]
        self.browser.get(shop["链接"])

        # 判断是否需要登录
        try:
            log_win=self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.login-password')))
            print("处于登录页面，需要登录")
            self.login(on_login_web=True)
        except:
            print("无需登录，直接访问")
        shop_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sHe-shop')))
        shop_button.click()

        to_handle = self.browser.window_handles
        self.browser.switch_to.window(to_handle[1])
        time.sleep(2)

        while True:
            main_info=self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.main-info')))
            actions=ActionChains(self.browser)
            actions.move_to_element(main_info)
            actions.perform()
            time.sleep(5)
            try:
                info_button=self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tm-gsLink')))
                info_button.click()
                break
            except:
                # 如果找不到弹窗按钮的话再次移动鼠标
                pass

        # 切换到查看经营者信息前的验证码网页
        to_handle = self.browser.window_handles
        self.browser.switch_to.window(to_handle[2])
        time.sleep(2)

        self.handleCaptcha()

        self.getBusinessLicense()
        # 处理完验证码拿到执照信息后关闭页面
        self.browser.close()
        self.browser.switch_to.window(to_handle[1])
        time.sleep(2)

        # 关闭当前窗口，切换回第一个窗口
        self.browser.close()
        self.browser.switch_to.window(to_handle[0])
        time.sleep(2)

    def handleCaptcha(self):
        # 处理获取营业执照前的验证码

        self.saveCaptcha()

        captcha_result=self.scanCaptcha()

        text=self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="checkCode"]')))
        text.send_keys(captcha_result)

        confirm_button=self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.short-btn')))
        confirm_button.click()

        # 如果验证码还在说明验证失败，自动刷新验证码重新验证
        try:
            captcha = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_CheckCode')))
            self.handleCaptcha()
        except:
            print("验证码输入正确")




    def saveCaptcha(self):
        # 截图二维码保存在本地

        captcha = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_CheckCode')))

        self.browser.save_screenshot(SCREENSHOT_PATH)
        print(captcha.location)

        left = captcha.location['x']
        top = captcha.location['y']
        right = captcha.location['x'] + captcha.size['width']
        bottom = captcha.location['y'] + captcha.size['height']

        screenshot = Image.open(SCREENSHOT_PATH)
        captcha_img = screenshot.crop((left, top, right, bottom))
        captcha_img.save(CAPTCHA_PATH)

    def scanCaptcha(self):
        # 通过打码平台识别验证码

        # 打码平台需要的参数，表示四个字母的数字字母混合的验证码
        PRED_TYPE = "30400"
        # scan_api=FateadmApi(app_id,app_key,pd_id,pd_key)
        # scan_result=scan_api.Predict(PRED_TYPE,open(CAPTCHA_PATH,'rb'))
        # scan_result = scan_result.pred_rsp.value
        # print("验证码识别结果为："+scan_result)
        # return scan_result
        pass

    def getBusinessLicense(self):
        # 获取营业执照照片
        license = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='box-item img-box'] img")))
        license_base64=license.get_attribute("src")
        # 去掉开头的信息以及把base64中的空格（编码为%0A）去掉
        license_base64=license_base64.replace("data:image/png;base64,","").replace("%0A","")
        # print((license_base64))
        img_data=base64.b64decode(license_base64)
        file=open(os.path.join("src","pic",self.keyword,self.current_shop_name+".png"),"wb")
        file.write(img_data)
        file.close()



username = ''  # 你的 微博账号
password = ''  # 你的 微博密码

# 打码平台所需参数
app_id=""
app_key=""
pd_id=""
pd_key=""
# 你的 selenium驱动 存放地址
chromedriver_path = 'chromedriver.exe'
# 你要爬取的 搜索关键词
category = "职业装"

if __name__ == '__main__':
    # 爬取关键词相关的店铺信息
    a = TmallShopSpider(username, password, chromedriver_path)
    a.crawlShops(category)

    # 读取excel获取店铺的经营者相关资质信息
    # try:
    #     spider = TmallShopSpider(username, password, chromedriver_path)
    #     spider.getAllShopPublicInfo(category)
    # except Exception as e:
    #     print("程序出现异常，30s后关闭浏览器")
    #     print(e)
    #     time.sleep(30)
    #     spider.browser.close()
