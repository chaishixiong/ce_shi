import requests
import time
from lxml import etree
import openpyxl as op
from urllib.parse import quote
from fake_useragent import UserAgent
from KuaJing_youbian.k_j_settings import brazil_list


class Brazil_YouBian(object):
    def __init__(self):
        self.wb = op.Workbook()  # 创建工作簿对象
        self.ws = self.wb['Sheet']  # 创建子表
        self.ws.append(['邮编号', '地名/城市', '州/市', '纬度', '经度'])  # 添加表头
        self.num = 0

    def request_get(self, url):
        ua = UserAgent()
        headers = {
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'cookies': '_ga=GA1.2.amp-bUATe4IVThe8ZjdnBt-TBA; __gads=ID=54fbfaaa17ba7ccc-2222ea686ad40055:T=1655262728:RT=1655262728:S=ALNI_MZqV8BrLdJbnMbNELAdHUUMka_pNg; ASPSESSIONIDSWDBTCTB=OFMOCLDBJDMALKANIIAMKKAJ; ASPSESSIONIDSUCATCSB=HLGCIKMAPFOAAMBCJPJPGLBN; ASPSESSIONIDSWDCQCSA=JFBKJEPALFJHNGLMKBDLNHMP; ASPSESSIONIDQWCBQDSA=MDJNLKBBFLBCMOFNEFCFBFJO; ASPSESSIONIDSWBDTCSA=EGGPINJADGKCLACFMAHHEDMK; ASPSESSIONIDSUADTDSB=GONMJGOBEGNFCJNMKKHNHJIF; ASPSESSIONIDQUDCSDSA=AJDOGGJBFILHCHENAKMNGDCN; ASPSESSIONIDQWDDQCSA=EGPPFJGBOBPKOLHFNNHIOEOK; ASPSESSIONIDSUBCTCSB=CNEKHAMBNOPIAEODAEMOOJLH; ASPSESSIONIDSWADTDSA=GNHOIOHDIDBHNMJMEJOFJCHB; ASPSESSIONIDQUBASDTA=NKPAGIFDDLNJOMIOFHKCLGDE; ASPSESSIONIDSWCBTDTA=JJLJBNMDBGGGHMJKIDMPHMDK; ASPSESSIONIDSUCBSDSB=GMNPPOJDLPINNKGPBCHDANHJ; ASPSESSIONIDQWABSCSA=HENCEKPDEKMPLCOBIICMAAOB; ASPSESSIONIDSWAASCSA=EDOBEECACBPKDBEBHLJGCAFI; ASPSESSIONIDQWBCTDSA=BJHPGKEAFDAKGBKJIOGJLHID; ASPSESSIONIDQUDCSDSB=BAMMNKGAIAKBGBNJBEBLAHKL; ASPSESSIONIDQWAAQDTB=HLGFBJJAKKENPFKGGINEEFMI; ASPSESSIONIDQUCBSDTA=JCMCBGMAACNLEOLHIDILCJFJ; ASPSESSIONIDQUCAQDSB=EBAHCAPAADIHMEIKGGLBHPNP; ASPSESSIONIDSWBARCSB=OBPJLGDBPMCENOLNBLLCOKBN; ASPSESSIONIDQUBDQDSB=KACAGFMBALKAKLCCMFGBNNJJ; ASPSESSIONIDSUCBSDTA=MIDAHMMBABPMDFABEKMPOCJO; ASPSESSIONIDQUBCTCTB=CBPDOEGBPHPHFLDDCIEAMPJO; ASPSESSIONIDQWDBTCTB=MKLHGGBBBDJIBAIMIJDEDMPE; ASPSESSIONIDSUDASDSA=NAGCEGDAAJJMKIBKHCFLEMDK; ASPSESSIONIDSWCATCSA=NHHADJCAGPNKPDNGGNAOPBLJ; _gid=GA1.2.1905029438.1656310962; ASPSESSIONIDSWDCQDSB=PNKMLFPDEOHAEAFCHMKHDBKN; __gpi=UID=000006a4366463c7:T=1655262728:RT=1656381759:S=ALNI_Mb7hAVut6JJVz1HkNW_xHbsiiK46A; ASPSESSIONIDSWBAQCTA=FOKMJBMANMBNELKKBCLEPMOA; ASPSESSIONIDQWAATCSB=JJPGCCABPDCIHEIHOAGJPMFJ; ASPSESSIONIDSWDATDSB=CBIBNBBBCCKIKAEEDCJGHEHP; ASPSESSIONIDSUACSCSA=NLEGBFPAJNGFBOONIKLDHPFM; ASPSESSIONIDSUCBTDTA=DDCGKEJABIHDDNKEELPHPMMH'
        }

        request = requests.get(url=url, headers=headers)
        return request

    def xpath_html(self, response_data, xpath_str):
        response_html = etree.HTML(response_data.text)
        city_list = response_html.xpath(xpath_str)
        return city_list

    def json_data(self):
        pass

    def op_toExcel(self, data, fileName):  # openpyxl库储存数据到excel
        # wb = op.Workbook()  # 创建工作簿对象
        # ws = wb['Sheet']  # 创建子表
        # ws.append(['邮编号', '地名/城市', '县/郡', '州/市', '纬度', '经度'])  # 添加表头
        d = (data[0], data[1], data[2], data[3], data[4], data[5])
        self.ws.append(d)  # 每次写入一行
        self.wb.save(fileName)

    def city_data(self, america_province, response_data):
        city_xpath_str = "//div[@class='col-xs-12']/div/a/@href"
        city_list = self.xpath_html(response_data, city_xpath_str)
        for city in city_list:
            str_city = str(city)
            city_url = 'https://www.nowmsg.com/findzip/{}'.format(str_city)
            city_response_data = self.request_get(city_url)
            self.data_list(city_response_data, america_province, city)

    def county_data(self, city_response_data, america_province, city, city_xpath_str):
        county_list = self.xpath_html(city_response_data, city_xpath_str)
        for county in county_list:
            num = 0
            try:
                self.data_list(america_province, city, county)
            except Exception as e:
                num += 1
                if num < 4:
                    self.data_list(america_province, city, county)
                else:
                    print(num)
                    print(e)

    # def data_list(self, america_province, city, county):
    def data_list(self, url):
        if url == '\n':
            return None
        city_url = 'https://www.nowmsg.com/findzip/{}'.format(url)
        city_response_data = self.request_get(url)
        county_xpath_str = "//table[@class='table table-hover']/tbody/tr/td/text()"
        # county_url = 'https://www.nowmsg.com/findzip/postal_code.asp?country=BR&state={}&county={}&city={}'.format(
        #     america_province, city, county)
        # county_response_data = self.request_get(county_url)
        county_data = self.xpath_html(city_response_data, county_xpath_str)
        if self.num >= 5:
            with open(r'bazil_url_erry.txt', 'a', encoding='utf-8') as f:
                f.write(city_url + '\n')
                f.flush()
            self.num = 0
            print('重试第' + str(self.num) + '次')
        elif len(county_data) >= 6:
            self.op_toExcel(county_data, 'brazil_yb.xlsx')
            print(county_data)
        else:
            self.num += 1
            print('county_data长度' + str(len(county_data)))
            self.data_list(url)

    def run_spider(self):
        for america_province in brazil_list:
            url = 'https://www.nowmsg.com/findzip/county.asp?country=BR&state={}'.format(america_province)
            response_data = self.request_get(url)
            self.city_data(america_province, response_data)


def run_BR_YouBian_spider():
    run_us_yb = Brazil_YouBian()
    with open(r'brazil_url', 'r', encoding='utf-8') as url_list:
        for url in url_list:
            num = 0
            run_us_yb.data_list(url)


if __name__ == '__main__':
    # aaa = 'Acrelândia'
    # print(quote(aaa))
    run_BR_YouBian_spider()

