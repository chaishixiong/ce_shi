from selenium import webdriver
import time
import random
import lxml
from lxml import html
from selenium.webdriver.common.action_chains import ActionChains


class SafeDriver:

    def __init__(self):
        self.count_slide = 0
        self.chrome_canshu()

    def chrome_canshu(self):

        # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        options.add_argument('--incognito')
        options.add_argument('--no-sandbox')
        options.add_argument("disable-infobars")
        options.add_argument("disable-web-security")
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_argument("--log-level=3")
        No_Image_loading = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", No_Image_loading)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(executable_path='D:\chromedriver.exe', chrome_options=options)

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        if self.driver:

            self.driver.quit()

    def run_selenium(self):
        self.driver.get('https://login.aliexpress.com')
        time.sleep(2)

        self.driver.find_element_by_name("fm-login-id").send_keys("zqw@qilingu.com")
        time.sleep(2)
        self.driver.find_element_by_name("fm-login-password").send_keys("a123456789")
        self.slide_block()

    def slide_block(self):
        time.sleep(2)
        try:
            slide = self.driver.find_element_by_id("nc_1_n1z")
            print("正在破解滑块中。。。。。")
        except Exception as error_msg:
            print("滑块错误提示：", error_msg)
            input("等待指令中。。")
        else:
            action = ActionChains(self.driver)
            action.click_and_hold(slide)
            sum = 0
            while True:
                x = random.randint(0, 10)
                action.move_by_offset(x, 0)
                time.sleep((random.randint(1, 2)) / 10)
                sum += x
                if sum >= 260:
                    break
            action.release().perform()
            time.sleep(2)
            parser = lxml.html.etree.HTML(self.driver.page_source)
            element = parser.xpath("")
            if len(element) == 0:
                flah_button = self.driver.find_element_by_xpath("")
                time.sleep(3)
                flah_button.click()
                if self.count_slide == 3:
                    print("滑块破解成功")
                    return
                self.count_slide += 1
                self.slide_block()
            else:
                print("滑块破解成功")
                return


if __name__ == '__main__':
    r = SafeDriver()
    r.run_selenium()
