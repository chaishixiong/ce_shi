import re
import requests
from lxml import etree


class AmazonShop(object):
    def __init__(self):
        pass

    def requesr_spider(self, url):
        headers = {
            "authority": "www.amazon.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "cookie": 'session-id=137-0489966-7453666; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn=^\^"L5Z9:CN^\^"; ubid-main=132-2961476-4810337; session-id-jp=355-9057861-4050835; ubid-acbjp=357-3763949-7715242; s_pers=^%^20s_fid^%^3D227B8ED09C84DAE8-27437224EA0E76B0^%^7C1807154523899^%^3B^%^20s_dl^%^3D1^%^7C1649389923899^%^3B^%^20gpv_page^%^3DSC^%^253AJP^%^253AWP-Welcome^%^7C1649389923900^%^3B^%^20s_ev15^%^3D^%^255B^%^255B^%^2527SCJPWPDirect^%^2527^%^252C^%^25271649388123902^%^2527^%^255D^%^255D^%^7C1807154523902^%^3B; lc-main=en_US; session-token="gxKnV85Nk0UX7vscqe81xiQ5Ip1ffb8ZUMp9BMjxznzUaIxdavNTiZh5sDe7YAg+LHIvjvaW/0H2wugJRuJ9f39w5/HJLcrzAdgE71VUpS7KLTAEq8+ChbBe21cD66Fgyy4W8uG/0mJHjgITfY95/UkRczuSgm3W91xuFH06yVYsYTwqOeBMkLHJiGSq1ToaX221cqjl2llElfu9sHlQzg=="; csm-hit=tb:H7A1FB3QABF4XQM684T1+s-H7A1FB3QABF4XQM684T1^|1658734392026&t:1658734392026&adb:adblk_no',
            "device-memory": "8",
            "downlink": "6.3",
            "dpr": "1.25",
            "ect": "4g",
            "rtt": "50",
            "sec-ch-device-memory": "8",
            "sec-ch-dpr": "1.25",
            "sec-ch-ua": '.Not/A)Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"103^\^", ^\^"Chromium^\^";v=^\^"103^\^"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-ch-viewport-width": "1638",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "viewport-width": "1638",

              }
        r = requests.get(url, headers=headers)
        return r

    def parse_data(self, data_da):
        text = data_da.text
        text_html = etree.HTML(data_da.text)
        shop_name_match = re.search('sellerName-rd">([^<]*)</h1>', text)
        if shop_name_match:
            shop_name = shop_name_match.group(1)
        shop_info_match = re.search('"a-row a-spacing-none spp-expander-more-content">([^/]*)</div>', text)
        if shop_info_match:
            shop_info = shop_info_match.group(1)
        company_match = re.search('</span><span>([^<]*)</span></div><div class="a-row a-spacing-none"><span class="a-text-bold">', text)
        if company_match:
            company = company_match.group(1)
        company_address = text_html.xpath('//div[@id="page-section-detail-seller-info"]/div/div/div//div[4]/span/text()')[0]
        country_match = re.search('<span>(CN)</span></div>', text)
        if country_match:
            country = country_match.group(1)
        postcode_match = text_html.xpath('//div[@class="a-row a-spacing-none indent-left"][4]/span/text()')[0]
        html_list = text_html.xpath('//div[@class="a-row a-spacing-none indent-left"]/span/text()')
        html = ''
        if len(html_list) > 1:
            for i in html_list:
                html += i
        goodrate_mouth = data_da.css("#feedback-summary-table").xpath("./tr[2]/td[2]").xpath("string(.)").get(
            "").strip()
        middlerate_mouth = data_da.css("#feedback-summary-table").xpath("./tr[3]/td[2]").xpath("string(.)").get(
            "").strip()
        badrate_mouth = data_da.css("#feedback-summary-table").xpath("./tr[4]/td[2]").xpath("string(.)").get(
            "").strip()
        comment_mouth = data_da.css("#feedback-summary-table").xpath("./tr[5]/td[2]").xpath("string(.)").get(
            "").strip()
        comment_mouth = comment_mouth.replace(",", "")
        goodrate_quarterly = data_da.css("#feedback-summary-table").xpath("./tr[2]/td[3]").xpath("string(.)").get(
            "").strip()
        middlerate_quarterly = data_da.css("#feedback-summary-table").xpath("./tr[3]/td[3]").xpath("string(.)").get(
            "").strip()
        badrate_quarterly = data_da.css("#feedback-summary-table").xpath("./tr[4]/td[3]").xpath("string(.)").get(
            "").strip()
        comment_quarterly = data_da.css("#feedback-summary-table").xpath("./tr[5]/td[3]").xpath("string(.)").get(
            "").strip()
        comment_quarterly = comment_quarterly.replace(",", "")
        goodrate_year = data_da.css("#feedback-summary-table").xpath("./tr[2]/td[4]").xpath("string(.)").get(
            "").strip()
        middlerate_year = data_da.css("#feedback-summary-table").xpath("./tr[3]/td[4]").xpath("string(.)").get(
            "").strip()
        badrate_year = data_da.css("#feedback-summary-table").xpath("./tr[4]/td[4]").xpath("string(.)").get("").strip()
        comment_year = data_da.css("#feedback-summary-table").xpath("./tr[5]/td[4]").xpath("string(.)").get("").strip()
        comment_year = comment_year.replace(",", "")
        goodrate_total = data_da.css("#feedback-summary-table").xpath("./tr[2]/td[5]").xpath("string(.)").get(
            "").strip()
        middlerate_total = data_da.css("#feedback-summary-table").xpath("./tr[3]/td[5]").xpath("string(.)").get(
            "").strip()
        badrate_total = data_da.css("#feedback-summary-table").xpath("./tr[4]/td[5]").xpath("string(.)").get(
            "").strip()
        comment_total = data_da.css("#feedback-summary-table").xpath("./tr[5]/td[5]").xpath("string(.)").get(
            "").strip()
        comment_total = comment_total.replace(",", "")
        province = ""
        city = ""
        county = ""
        main_sales = ""
        average_price = ""

    def run_amazonshop_spide(self):
        url = 'https://www.amazon.com/sp?ie=UTF8&isCBA=&language=en_US&seller=A3QAMPS64TICKF&tab=&vasStoreID='
        data_da = self.requesr_spider(url)
        self.parse_data(data_da)
        print(data_da)


if __name__ == '__main__':
    run = AmazonShop()
    run.run_amazonshop_spide()



