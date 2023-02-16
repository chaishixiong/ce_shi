from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import kuajing_227_pool
import pandas as pd



class UpdataCounty(object):
    def __init__(self):
        self.country_list = ['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BW', 'BY', 'BZ', 'CA', 'CF', 'CG', 'CH', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CS', 'CU', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FJ', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GH', 'GI', 'GM', 'GN', 'GR', 'GT', 'GU', 'GY', 'HK', 'HN', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KP', 'KR', 'KT', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'MG', 'ML', 'MM', 'MN', 'MO', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PR', 'PT', 'PY', 'QA', 'RO', 'RU', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SY', 'SZ', 'TD', 'TG', 'TH', 'TJ', 'TM', 'TN', 'TO', 'TR', 'TT', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE', 'VN', 'YE', 'YU', 'ZA', 'ZM', 'ZR', 'ZW', 'HR', 'KM', 'UM', 'MK', 'VG', 'TL', 'BT', 'NC']
        self.country_name_list = ['安道尔共和国', '阿拉伯联合酋长国', '阿富汗', '安提瓜和巴布达', '安圭拉岛', '阿尔巴尼亚', '亚美尼亚', '安哥拉', '阿根廷', '奥地利', '澳大利亚', '阿塞拜疆', '巴巴多斯', '孟加拉国', '比利时', '布基纳法索', '保加利亚', '巴林', '布隆迪', '贝宁', '巴勒斯坦', '百慕大群岛', '文莱', '玻利维亚', '巴西', '巴哈马', '博茨瓦纳', '白俄罗斯', '伯利兹', '加拿大', '中非共和国', '刚果', '瑞士', '库克群岛', '智利', '喀麦隆', '中国', '哥伦比亚', '哥斯达黎加', '捷克', '古巴', '塞浦路斯', '捷克', '德国', '吉布提', '丹麦', '多米尼加共和国', '阿尔及利亚', '厄瓜多尔', '爱沙尼亚', '埃及', '西班牙', '埃塞俄比亚', '芬兰', '斐济', '法国', '加蓬', '英国', '格林纳达', '格鲁吉亚', '法属圭亚那', '加纳', '直布罗陀', '冈比亚', '几内亚', '希腊', '危地马拉', '关岛', '圭亚那', '香港特别行政区', '洪都拉斯', '海地', '匈牙利', '印度尼西亚', '爱尔兰', '以色列', '印度', '伊拉克', '伊朗', '冰岛', '意大利', '牙买加', '约旦', '日本', '肯尼亚', '吉尔吉斯坦', '柬埔寨', '朝鲜', '韩国', '科特迪瓦共和国', '科威特', '哈萨克斯坦', '老挝', '黎巴嫩', '圣卢西亚', '列支敦士登', '斯里兰卡', '利比里亚', '莱索托', '立陶宛', '卢森堡', '拉脱维亚', '利比亚', '摩洛哥', '摩纳哥', '摩尔多瓦', '马达加斯加', '马里', '缅甸', '蒙古', '澳门', '蒙特塞拉特岛', '马耳他', '毛里求斯', '马尔代夫', '马拉维', '墨西哥', '马来西亚', '莫桑比克', '纳米比亚', '尼日尔', '尼日利亚', '尼加拉瓜', '荷兰', '挪威', '尼泊尔', '瑙鲁', '新西兰', '阿曼', '巴拿马', '秘鲁', '法属玻利尼西亚', '巴布亚新几内亚', '菲律宾', '巴基斯坦', '波兰', '波多黎各', '葡萄牙', '巴拉圭', '卡塔尔', '罗马尼亚', '俄罗斯', '沙特阿拉伯', '所罗门群岛', '塞舌尔', '苏丹', '瑞典', '新加坡', '斯洛文尼亚', '斯洛伐克', '塞拉利昂', '圣马力诺', '塞内加尔', '索马里', '苏里南', '圣多美和普林西比', '萨尔瓦多', '叙利亚', '斯威士兰', '乍得', '多哥', '泰国', '塔吉克斯坦', '土库曼斯坦', '突尼斯', '汤加', '土耳其', '特立尼达和多巴哥', '台湾', '坦桑尼亚', '乌克兰', '乌干达', '美国', '乌拉圭', '乌兹别克斯坦', '圣文森特岛', '委内瑞拉', '越南', '也门', '南斯拉夫', '南非', '赞比亚', '扎伊尔', '津巴布韦', '克罗地亚', '科摩罗', '美属萨摩亚', '马其顿', '不列颠岛(英) ', '土耳其', '不丹', '新喀里多尼亚']
        self.country_dict = dict()
        self.sql_227_kj = DataBaseSession(kuajing_227_pool)
        self.data_list = []
        self.file_write = open(r"C:\Users\Administrator\Desktop\data\amazonus_shopinfo_202201_sales_new.txt", "w",
                          encoding="utf-8")

    def query_data(self):
        sql = "SELECT * FROM `amazonus_shopinfo_202112_sales`"
        daima_res = self.sql_227_kj.query_tuple_data(sql)
        return daima_res

    def insertion_data(self):
        inser_sql = "insert into amazonus_shopinfo_202112_sales_new_copy1 (shop_id,shop_name,shop_info,company,company_address,country,postcode,html,goodrate_mouth,middlerate_mouth,badrate_mouth,comment_mouth,goodrate_quarterly,middlerate_quarterly,badrate_quarterly,comment_quarterly,goodrate_year,middlerate_year,badrate_year,comment_year,goodrate_total,middlerate_total,badrate_total,comment_total,province,city,county,main_sales,average_price,sales,sales_money,sales_y,sales_money_y) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.sql_227_kj.insertion_data_list(inser_sql, self.data_list)

    def re_data(self, query_data):
        num = 0
        for item in query_data:
            num += 1
            item_list = list(item)
            country = item[7][-2:]
            country_name = self.country_dict.get(country)
            if country_name == None:
                # data_tuple = tuple(item_list)
                self.file_write.write(",".join(item_list) + "\n")
                # self.data_list.append(data_tuple)
            else:
                item_list[5] = country_name
                self.file_write.write(",".join(item_list) + "\n")
                # self.data_list.append(data_tuple)
            if num % 10000 == 0:
                # self.insertion_data()
                # self.data_list = []
                print(num)
        # if len(self.data_list) > 0:
        #     print(num)
        #     self.insertion_data()
        #     self.data_list = []

    def updata_data(self):
        pass

    def run_spider(self):
        for country, country_name in zip(self.country_list, self.country_name_list):
            self.country_dict[country] = country_name
        query_data = self.query_data()
        re_data = self.re_data(query_data)
        # updata_data = self.updata_data()
        # insertion_data = self.insertion_data()


def run_amazon_county():
    run = UpdataCounty()
    run.run_spider()


if __name__ == '__main__':
    run_amazon_county()
    # aa = '7 Sobrisco StAirmontny10952US'
    print()




