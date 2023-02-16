import requests
import time
from lxml import etree
import openpyxl as op
from fake_useragent import UserAgent
from KuaJing_youbian.k_j_settings import america_province_list


class America_YouBian(object):
    def __init__(self):
        self.wb = op.Workbook()  # 创建工作簿对象
        self.ws = self.wb['Sheet']  # 创建子表
        self.ws.append(['邮编号', '地名/城市', '县/郡', '州/市', '纬度', '经度'])  # 添加表头

    def request_get(self, url):
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
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
        city_xpath_str = "//div[@class='col-xs-12']/div/a/text()"
        city_list = self.xpath_html(response_data, city_xpath_str)
        for city in city_list:
            city_url = 'https://www.nowmsg.com/findzip/city.asp?country=US&state={}&county={}'.format(america_province,
                                                                                                      city)
            city_response_data = self.request_get(city_url)
            self.county_data(city_response_data, america_province, city, city_xpath_str)

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

    def data_list(self, america_province, city, county):
        county_xpath_str = "//table[@class='table table-hover']/tbody/tr/td/text()"
        county_url = 'https://www.nowmsg.com/findzip/postal_code.asp?country=US&state={}&county={}&city={}'.format(
            america_province, city, county)
        county_response_data = self.request_get(county_url)
        county_data = self.xpath_html(county_response_data, county_xpath_str)
        if len(county_data) >= 7:
            self.op_toExcel(county_data, 'americle_yb.xlsx')
            print(america_province, city, county)
        else:
            print('county_data长度' + str(len(county_data)))
            time.sleep(5)
            self.data_list(america_province, city, county)


    def run_spider(self):
        for america_province in america_province_list:
            url = 'https://www.nowmsg.com/findzip/county.asp?country=US&state={}'.format(america_province)
            response_data = self.request_get(url)
            self.city_data(america_province, response_data)


def run_US_YouBian_spider():
    run_us_yb = America_YouBian()
    run_us_yb.run_spider()


if __name__ == '__main__':
    run_US_YouBian_spider()

