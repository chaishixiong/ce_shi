# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from scrapy import signals
from scrapy.http import HtmlResponse
from twisted.internet.error import TCPTimedOutError, TimeoutError
from .settings import proxy_pool, cookies_pool
import time
from lxml import etree
import requests
import base64
import random
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

# 百度OCR识别
def BaiduOCR(image):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    params = {"image": image}
    access_token = '24.2a9081ed1bb7f176d9594e12007ba53a.2592000.1616911030.282335-23695451'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    try:
        if response.json()['words_result']:
            return response.json()['words_result'][0]['words']
        else:
            print('验证码识别失败，重新识别')
            return None
    except Exception as e:
        print("发生错误{}".format(e))
# 验证码识别
def Captcha(response,request):
    cookie = request.cookies
    ua = request.headers['User-Agent'].decode()
    session = requests.session()
    header = {
        "User-Agent": ua,
        'referer': 'https://www.amazon.com/',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'authority': 'fls-na.amazon.com',
        'method': 'GET',
        'path': '/1/remote-weblab-triggers/1/OE/ATVPDKIKX0DER:141-6401734-9560133:A2KQPV02XD3XTHB7W8DV$s:wl-client-id%3DCSMTriger%2Cwl%3DUEDATA_AA_SERVERSIDE_ASSIGNMENT_CLIENTSIDE_TRIGGER_190249%2FT1:1234',
        'scheme': 'https',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'Sec - Fetch - Dest': 'empty',
        'Sec - Fetch - Mode': 'cors',
        'Sec - Fetch - Site': 'same - site',
        'Connection': 'keep - alive'
    }
    proxies = {
        "http": random.choice(proxy_pool),
        # "http":  proxy_pool(),
        # "https": "https://12.34.56.79:9527",
    }
    html = etree.HTML(response.text)
    image_link = html.xpath('/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/img/@src')[0]
    resp = requests.get(image_link).content
    with open('save.jpg', 'wb') as f:
        f.write(resp)
    amaz = html.xpath('//div[@class="a-box-inner a-padding-extra-large"]/form/input/@value')[0]
    amaz_r = html.xpath('//div[@class="a-box-inner a-padding-extra-large"]/form/input/@value')[1]
    with open('save.jpg', 'rb') as f:
        base64_data = base64.b64encode(f.read())
        image = base64_data.decode()
    if BaiduOCR(image):
        yzm = BaiduOCR(image).strip()
    else:
        yzm = BaiduOCR(image)
    url = 'https://www.amazon.com/errors/validateCaptcha?amzn={}&amzn-r={}&field-keywords={}'.format(amaz, amaz_r, yzm)
    new_response = session.get(url=url, headers=header, proxies=proxies, cookies=cookie)
    if "To discuss automated access to Amazon data please contact api-services-support@amazon.com." not in new_response.text:
        return new_response
    else:
        print('验证码识别错误，重新识别')
        return Captcha(new_response, request)

# 代理IP设置
class ProxyMiddleware(object):


    def process_request(self,request,spider):

        proxy = random.choice(proxy_pool)
        request.meta['proxy'] = proxy
        # print(request.meta['proxy'])

    def process_exception(self, request, exception, spider):
        if isinstance(exception, TimeoutError):
            self.process_request(request, spider)  # 连接超时才启用代理ip机制
            return request

        elif isinstance(exception, TCPTimedOutError):
            self.process_request(request, spider)
            return request

# 下载中间件配置，如果出现验证码，需要先经过此中间件破解后返回新的响应
class DownloadMiddleware(object):
    def process_response(self, request, response, spider):

        if "To discuss automated access to Amazon data please contact api-services-support@amazon.com." in response.text:
            print("出现验证码")
            cookie = request.cookies
            ua = request.headers['User-Agent'].decode()
            session = requests.session()
            header = {
                "User-Agent": ua,
                'referer': 'https://www.amazon.com/',
                'sec-fetch-dest': 'image',
                'sec-fetch-mode': 'no-cors',
                'sec-fetch-site': 'same-site',
                'authority': 'fls-na.amazon.com',
                'method': 'GET',
                'path': '/1/remote-weblab-triggers/1/OE/ATVPDKIKX0DER:141-6401734-9560133:A2KQPV02XD3XTHB7W8DV$s:wl-client-id%3DCSMTriger%2Cwl%3DUEDATA_AA_SERVERSIDE_ASSIGNMENT_CLIENTSIDE_TRIGGER_190249%2FT1:1234',
                'scheme': 'https',
                'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9',
                'Sec - Fetch - Dest': 'empty',
                'Sec - Fetch - Mode': 'cors',
                'Sec - Fetch - Site': 'same - site',
                'Connection': 'keep - alive'
            }
            proxies = {
                "http": random.choice(proxy_pool),
                # "http":  proxy_pool(),
                # "https": "https://12.34.56.79:9527",
            }
            response = session.get(url=response.url, headers=header, proxies=proxies, cookies=cookie)

            if "To discuss automated access to Amazon data please contact api-services-support@amazon.com." in response.text:
                print("第二次验证码")
                response = Captcha(response, request)

                body = response.content
                respo_header = response.headers
                try:
                    encod = respo_header["Content-Encoding"]
                except Exception:
                    encod = "gzip"
                new_response_2 = HtmlResponse(url=request.url, body=body, encoding=encod, request=request)
                return new_response_2
            else:
                body = response.content
                respo_header = response.headers
                try:
                    encod = respo_header["Content-Encoding"]
                except Exception:
                    encod = "gzip"
                new_response_2 = HtmlResponse(url=request.url, body=body, encoding=encod, request=request)
                return new_response_2
        else:
            return response

# 随机请求头
class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        # user_agent = random.choice(USER_AGENTS_LIST)
        request.headers['User-Agent'] = "Mozilla/5.0 (Windows NT {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36".format(
            random.choice([
                '10.0; Win64; x64', '10.0; WOW64', '10.0',
                '6.2; WOW64', '6.2; Win64; x64', '6.2',
                '6.1', '6.1; Win64; x64', '6.1; WOW64'
            ]), random.choice([
                '70.0.3538.16', '70.0.3538.67', '70.0.3538.97', '71.0.3578.137', '71.0.3578.30', '71.0.3578.33',
                '71.0.3578.80', '72.0.3626.69', '72.0.3626.7', '73.0.3683.20', '73.0.3683.68', '74.0.3729.6',
                '75.0.3770.140', '75.0.3770.8', '75.0.3770.90', '76.0.3809.12', '76.0.3809.126', '76.0.3809.25',
                '76.0.3809.68', '77.0.3865.10', '77.0.3865.40', '78.0.3904.105', '78.0.3904.11', '78.0.3904.70',
                '79.0.3945.16', '79.0.3945.36', '80.0.3987.106', '80.0.3987.16', '81.0.4044.138', '81.0.4044.20',
                '81.0.4044.69', '83.0.4103.14', '83.0.4103.39', '84.0.4147.30', '85.0.4183.38', '85.0.4183.83',
                '85.0.4183.87', '86.0.4240.22', '87.0.4280.20', '87.0.4280.88', '88.0.4324.27'
            ]))
        # print(request.headers['User-Agent'])

# 随机cookie设置
class CookieMiddleware(object):
    def process_request(self, request, spider):

        cookie = random.choice(cookies_pool)
        cookie_dict = {data.split('=')[0]: data.split('=')[-1] for data in cookie.split("; ")}

        request.cookies = cookie_dict
        # print(request.cookies)


class AmazonSpiderSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class AmazonSpiderDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
