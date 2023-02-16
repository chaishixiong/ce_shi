import requests
from lxml import etree
import re
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import shop_1_4_pool

site_type_dict = {
    "iit": "五星/顶级",
    "iim": "五星/豪华",
    "iij": "四星/高档",
    "iir": "三星/舒适",
    "iiu": "经济型",
    "iif": "度假村",
    "iis": "会议中心",
    "iiv": "酒吧/咖啡厅",
    "iiml": "餐厅",
    "iimm": "培训中心",
    "iimj": "剧院",
    "iimo": "会所",
    "iimf": "艺术中心",
    "iimr": "体育馆",
    "iims": "轰趴馆",
    "iimt": "校园场地",
    "iimu": "摄影棚",
    "iio": "其他"
}
site_xing_dict = {
    "iit": "顶级五星",
    "iim": "豪华五星",
    "iij": "四星",
    "iir": "三星",
    "iiu": "二星",
    "iif": "二星",
    "iis": "二星",
    "iiv": "二星",
    "iiml": "二星",
    "iimm": "二星",
    "iimj": "二星",
    "iimo": "二星",
    "iimf": "二星",
    "iimr": "二星",
    "iims": "二星",
    "iimt": "二星",
    "iimu": "二星",
    "iio": "二星"
}


class HotelGGSpider(object):
    def __init__(self):
        self.session_1_4 = DataBaseSession(shop_1_4_pool)
        self.item = {
            "最大会议厅面积": "",
            "最多可容纳人数": "",
            "会议厅数量": "",
            "客房数量": "",
            "double_number": "",
            "single_table": "",
            "annual_meeting": "",
        }

    def gg_request(self, url):
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
        r = requests.get(url=url, headers=headers)
        return r.text

    def list_pame_data(self, response_data):
        html_list_pame_data = etree.HTML(response_data)
        hotel_list = html_list_pame_data.xpath(r'//ul[@class="hotel_list"]/li/div/div/h3/a/@href')
        suaixuan_list = html_list_pame_data.xpath(r'//div[@class="args"]/a/text()')
        self.item["province"] = "浙江省"  # 省份
        self.item["city"] = "杭州市"  # 城市
        return hotel_list

    def hotel_pame_data(self, hotel_response_data):
        html_hotel_pame_data = etree.HTML(hotel_response_data)
        hotel_data_re = hotel_response_data.replace(' ', '').replace('\r', '').replace('\n', '')
        # hotel_neme = html_hotel_pame_data.xpath(r'//div[@class="hotel-info clearfix"]/h3/text()')  # 酒店名称
        hotel_neme = re.search(r'class="htl_name">(.*)</strong>', hotel_response_data).group(1)  # 酒店名称
        suaixuan_list = html_hotel_pame_data.xpath(r'//p[@class="hotel-address clearfix"]/span/text()')
        self.item["hotel_neme"] = hotel_neme  # 酒店名称
        self.item["county"] = str(suaixuan_list[1])  # 区域
        self.item["site_type_xing"] = site_xing_dict[self.site_type_es]  # 星级
        self.item["site_type"] = site_type_dict[self.site_type_es]  # 场地类型
        self.item["address"] = str(suaixuan_list[2])  # 具体地址
        self.hotel_room_data(html_hotel_pame_data)
        self.item["council_chamber_num"] = self.item["会议厅数量"]  # 会议厅个数
        self.item["room_number"] = self.item["客房数量"]  # 客房数量
        guestroom = html_hotel_pame_data.xpath(r'//p[@class="hotel-base-guestroom clearfix"]')
        if guestroom:
            double_number = re.search(r'<span>双标房：(.*?)间</span>', hotel_data_re)
            single_table = re.search(r'餐标：￥(.*?)/桌起', hotel_data_re)
            annual_meeting = re.search(r'年会餐标：￥(.*?)/桌起', hotel_data_re)
            room_reference_price = re.search(r'客房参考价：￥(.*?)</span>', hotel_data_re)
            self.item["double_number"] = self.re_group(1, double_number)  # 双标数量
            self.item["single_table"] = self.re_group(1, single_table)  # 圆桌餐饮
            self.item["annual_meeting"] = self.re_group(1, annual_meeting)  # 年会餐饮
            self.item["room_reference_price"] = self.re_group(1, room_reference_price)  # 客房参考价
        room_data_list = re.findall(r'<trclass="evenodd">(.*?)</tr>', hotel_data_re)
        room_xiaoguo_list = re.findall(r'trclass="evenhgg-even-hack">(.*?)</tr>', hotel_data_re)
        if len(room_data_list) == len(room_xiaoguo_list):
            for room_data, room_xiaoguo in zip(room_data_list, room_xiaoguo_list):
                self.item["hall_name"] = re.search(r'mt_name"><strong>(.*?)</strong>', room_data).group(1)  # 大厅名称
                self.item["square_measure"] = re.search(r'"area_dark">(.*?)<supclass', room_data).group(1)  # 面积
                self.item["fishbone"] = re.search(r'"hd_td_clear">(.*?)</td>', room_data).group(1)  # 鱼骨
                data_data = re.findall(r'"center">(.*?)</td>', room_data)
                self.item["theater"] = data_data[2]  # 剧院
                self.item["desk"] = data_data[3]  # 课桌
                self.item["U_shape"] = data_data[4]  # U型
                self.item["palindrome"] = data_data[5]  # 回字
                self.item["round_table"] = data_data[6]  # 圆桌
                floor = re.search(r'位于(\d+)楼', room_xiaoguo)
                length_width = re.search(r'尺寸(.*?)m</span>', room_xiaoguo)
                high = re.search(r'高(.*?)m</span>', room_xiaoguo)
                whether_split = re.search(r'可拆分|不可拆分', room_xiaoguo)
                yn_column = re.search(r'有柱|无柱', room_xiaoguo)
                yn_window = re.search(r'有窗|无窗', room_xiaoguo)
                self.item["floor"] = self.re_group(1, floor)  # 所在楼层
                self.item["length_width"] = self.re_group(1, length_width)  # 长宽
                self.item["high"] = self.re_group(1, high)  # 高
                self.item["whether_split"] =self.re_group(0, whether_split)  # 是否可拆分
                self.item["yn_column"] = self.re_group(0, yn_column)  # 有无立柱
                self.item["yn_window"] = self.re_group(0, yn_window)  # 有无窗户
                self.insertion_hotel_data()
                # self.item["whether_regularity"] = re.search(r'可拆分|不可拆分', room_data)  # 是否规整
                # hall_name_list = re.findall(r'class="mt_name"><strong>(.*?)</strong>', hotel_response_data)
                # square_measure_list = re.findall(r'class="area_dark">(.*?)<sup', hotel_response_data)
        # self.item["all_day_price"] = ''  # 全天价
        # self.item["half_day_price"] = ''  # 半天价
        # self.item["site_type"] = ''  # 场地类型
        # self.item["site_type"] = ''  # 场地类型
        # self.item["site_type"] = ''  # 场地类型
        # self.item["site_type"] = ''  # 场地类型

    def insertion_hotel_data(self):
        data_list = [self.item["hotel_neme"], self.item["province"], self.item["city"], self.item["county"], self.item["address"], self.item["site_type_xing"], self.item["site_type"], self.item["hall_name"], self.item["square_measure"], self.item["length_width"], self.item["high"], self.item["floor"], self.item["whether_split"], self.item["yn_column"], self.item["yn_window"], self.item["theater"], self.item["desk"], self.item["fishbone"], self.item["U_shape"], self.item["palindrome"], self.item["round_table"], self.item["room_number"], self.item["double_number"], self.item["room_reference_price"], self.item["single_table"], self.item["annual_meeting"]]
        insertion_sql = "insert into hotel_room_data (hotel_neme, province, city, county, address, site_type_xing, site_type, hall_name, square_measure, length_width, high, floor, whether_split, yn_column, yn_window, theater, desk, fishbone, U_shape, palindrome, round_table, room_number, double_number, room_reference_price, single_table, annual_meeting) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print(data_list)
        # 插入库名： session_227_tb
        self.session_1_4.insertion_data(insertion_sql, data_list)

    def re_group(self, num, data):
        if data:
            return data.group(num)
        else:
            return ' '

    def hotel_room_data(self, html_hotel_pame_data):
        room_num_data = html_hotel_pame_data.xpath(r'//ul[@class="base-parameter"]/li/p[2]/text()')
        room_name_data = html_hotel_pame_data.xpath(r'//ul[@class="base-parameter"]/li/p[3]/text()')
        for name_data, num_data in zip(room_name_data, room_num_data):
            self.item[name_data] = str(num_data)

    def run_hptel_gg(self):
        one_url = 'https://www.hotelgg.com/venue/miouoiojjviim/'
        self.site_type_es = re.search(r'iit|iim|iij|iir|iiu|iif|iis|iiv|iiml|iimm|iimj|iimo|iimf|iimr|iims|iimt|iimu|iio', one_url).group(0)
        print(self.site_type_es)
        response_data = self.gg_request(one_url)
        hotel_url_list = self.list_pame_data(response_data)
        for hotel_url in hotel_url_list:
            hotel_url = "https://www.hotelgg.com" + hotel_url
            print(hotel_url)
            hotel_response_data = self.gg_request(hotel_url)
            self.hotel_pame_data(hotel_response_data)


def run_hotel_spider():
    run = HotelGGSpider()
    run.run_hptel_gg()


if __name__ == '__main__':
    run_hotel_spider()







