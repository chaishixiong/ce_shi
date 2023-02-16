import requests
from lxml import etree


def redis_hotelgg_url(url):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "zh-CN,zh;q=0.9",
        "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    responts = requests.get(url=url, headers=headers)
    html_data = etree.HTML(responts.text)
    return html_data


def run_hotelgg():
    url = 'https://www.hotelgg.com/venue/miouo'
    html_data = redis_hotelgg_url(url)
    url_url = html_data.xpath(r'//div[@class="location-filter-item clearfix region_id"]/a/@href')
    for a_url in url_url:
        q_x_urldata = redis_hotelgg_url(a_url)
        asdsad_url = q_x_urldata.xpath(r'//div[@class="select_block clearfix"]/a/@href')
        for cdlx_url in asdsad_url:
            with open(r'dlwz_cdlx_url.txt', 'a', encoding='utf-8') as w:
                w.write(cdlx_url + '\n')
                w.flush()
    w.close()


run_hotelgg()


