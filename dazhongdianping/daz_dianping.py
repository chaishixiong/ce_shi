import requests
import re
from lxml import etree
import functools
import time
import os

css_dices = {'1': '0', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '0': '9', '店': '10', '中': '11', '美': '12', '家': '13', '馆': '14', '小': '15', '车': '16', '大': '17', '市': '18', '公': '19', '酒': '20', '行': '21', '国': '22', '品': '23', '发': '24', '电': '25', '金': '26', '心': '27', '业': '28', '商': '29', '司': '30', '超': '31', '生': '32', '装': '33', '园': '34', '场': '35', '食': '36', '有': '37', '新': '38', '限': '39', '天': '40', '面': '41', '工': '42', '服': '43', '海': '44', '华': '45', '水': '46', '房': '47', '饰': '48', '城': '49', '乐': '50', '汽': '51', '香': '52', '部': '53', '利': '54', '子': '55', '老': '56', '艺': '57', '花': '58', '专': '59', '东': '60', '肉': '61', '菜': '62', '学': '63', '福': '64', '饭': '65', '人': '66', '百': '67', '餐': '68', '茶': '69', '务': '70', '通': '71', '味': '72', '所': '73', '山': '74', '区': '75', '门': '76', '药': '77', '银': '78', '农': '79', '龙': '80', '停': '81', '尚': '82', '安': '83', '广': '84', '鑫': '85', '一': '86', '容': '87', '动': '88', '南': '89', '具': '90', '源': '91', '兴': '92', '鲜': '93', '记': '94', '时': '95', '机': '96', '烤': '97', '文': '98', '康': '99', '信': '100', '果': '101', '阳': '102', '理': '103', '锅': '104', '宝': '105', '达': '106', '地': '107', '儿': '108', '衣': '109', '特': '110', '产': '111', '西': '112', '批': '113', '坊': '114', '州': '115', '牛': '116', '佳': '117', '化': '118', '五': '119', '米': '120', '修': '121', '爱': '122', '北': '123', '养': '124', '卖': '125', '建': '126', '材': '127', '三': '128', '会': '129', '鸡': '130', '室': '131', '红': '132', '站': '133', '德': '134', '王': '135', '光': '136', '名': '137', '丽': '138', '油': '139', '院': '140', '堂': '141', '烧': '142', '江': '143', '社': '144', '合': '145', '星': '146', '货': '147', '型': '148', '村': '149', '自': '150', '科': '151', '快': '152', '便': '153', '日': '154', '民': '155', '营': '156', '和': '157', '活': '158', '童': '159', '明': '160', '器': '161', '烟': '162', '育': '163', '宾': '164', '精': '165', '屋': '166', '经': '167', '居': '168', '庄': '169', '石': '170', '顺': '171', '林': '172', '尔': '173', '县': '174', '手': '175', '厅': '176', '销': '177', '用': '178', '好': '179', '客': '180', '火': '181', '雅': '182', '盛': '183', '体': '184', '旅': '185', '之': '186', '鞋': '187', '辣': '188', '作': '189', '粉': '190', '包': '191', '楼': '192', '校': '193', '鱼': '194', '平': '195', '彩': '196', '上': '197', '吧': '198', '保': '199', '永': '200', '万': '201', '物': '202', '教': '203', '吃': '204', '设': '205', '医': '206', '正': '207', '造': '208', '丰': '209', '健': '210', '点': '211', '汤': '212', '网': '213', '庆': '214', '技': '215', '斯': '216', '洗': '217', '料': '218', '配': '219', '汇': '220', '木': '221', '缘': '222', '加': '223', '麻': '224', '联': '225', '卫': '226', '川': '227', '泰': '228', '色': '229', '世': '230', '方': '231', '寓': '232', '风': '233', '幼': '234', '羊': '235', '烫': '236', '来': '237', '高': '238', '厂': '239', '兰': '240', '阿': '241', '贝': '242', '皮': '243', '全': '244', '女': '245', '拉': '246', '成': '247', '云': '248', '维': '249', '贸': '250', '道': '251', '术': '252', '运': '253', '都': '254', '口': '255', '博': '256', '河': '257', '瑞': '258', '宏': '259', '京': '260', '际': '261', '路': '262', '祥': '263', '青': '264', '镇': '265', '厨': '266', '培': '267', '力': '268', '惠': '269', '连': '270', '马': '271', '鸿': '272', '钢': '273', '训': '274', '影': '275', '甲': '276', '助': '277', '窗': '278', '布': '279', '富': '280', '牌': '281', '头': '282', '四': '283', '多': '284', '妆': '285', '吉': '286', '苑': '287', '沙': '288', '恒': '289', '隆': '290', '春': '291', '干': '292', '饼': '293', '氏': '294', '里': '295', '二': '296', '管': '297', '诚': '298', '制': '299', '售': '300', '嘉': '301', '长': '302', '轩': '303', '杂': '304', '副': '305', '清': '306', '计': '307', '黄': '308', '讯': '309', '太': '310', '鸭': '311', '号': '312', '街': '313', '交': '314', '与': '315', '叉': '316', '附': '317', '近': '318', '层': '319', '旁': '320', '对': '321', '巷': '322', '栋': '323', '环': '324', '省': '325', '桥': '326', '湖': '327', '段': '328', '乡': '329', '厦': '330', '府': '331', '铺': '332', '内': '333', '侧': '334', '元': '335', '购': '336', '前': '337', '幢': '338', '滨': '339', '处': '340', '向': '341', '座': '342', '下': '343', '臬': '344', '凤': '345', '港': '346', '开': '347', '关': '348', '景': '349', '泉': '350', '塘': '351', '放': '352', '昌': '353', '线': '354', '湾': '355', '政': '356', '步': '357', '宁': '358', '解': '359', '白': '360', '田': '361', '町': '362', '溪': '363', '十': '364', '八': '365', '古': '366', '双': '367', '胜': '368', '本': '369', '单': '370', '同': '371', '九': '372', '迎': '373', '第': '374', '台': '375', '玉': '376', '锦': '377', '底': '378', '后': '379', '七': '380', '斜': '381', '期': '382', '武': '383', '岭': '384', '松': '385', '角': '386', '纪': '387', '朝': '388', '峰': '389', '六': '390', '振': '391', '珠': '392', '局': '393', '岗': '394', '洲': '395', '横': '396', '边': '397', '济': '398', '井': '399', '办': '400', '汉': '401', '代': '402', '临': '403', '弄': '404', '团': '405', '外': '406', '塔': '407', '杨': '408', '铁': '409', '浦': '410', '字': '411', '年': '412', '岛': '413', '陵': '414', '原': '415', '梅': '416', '进': '417', '荣': '418', '友': '419', '虹': '420', '央': '421', '桂': '422', '沿': '423', '事': '424', '津': '425', '凯': '426', '莲': '427', '丁': '428', '秀': '429', '柳': '430', '集': '431', '紫': '432', '旗': '433', '张': '434', '谷': '435', '的': '436', '是': '437', '不': '438', '了': '439', '很': '440', '还': '441', '个': '442', '也': '443', '这': '444', '我': '445', '就': '446', '在': '447', '以': '448', '可': '449', '到': '450', '错': '451', '没': '452', '去': '453', '过': '454', '感': '455', '次': '456', '要': '457', '比': '458', '觉': '459', '看': '460', '得': '461', '说': '462', '常': '463', '真': '464', '们': '465', '但': '466', '最': '467', '喜': '468', '哈': '469', '么': '470', '别': '471', '位': '472', '能': '473', '较': '474', '境': '475', '非': '476', '为': '477', '欢': '478', '然': '479', '他': '480', '挺': '481', '着': '482', '价': '483', '那': '484', '意': '485', '种': '486', '想': '487', '出': '488', '员': '489', '两': '490', '推': '491', '做': '492', '排': '493', '实': '494', '分': '495', '间': '496', '甜': '497', '度': '498', '起': '499', '满': '500', '给': '501', '热': '502', '完': '503', '格': '504', '荐': '505', '喝': '506', '等': '507', '其': '508', '再': '509', '几': '510', '只': '511', '现': '512', '朋': '513', '候': '514', '样': '515', '直': '516', '而': '517', '买': '518', '于': '519', '般': '520', '豆': '521', '量': '522', '选': '523', '奶': '524', '打': '525', '每': '526', '评': '527', '少': '528', '算': '529', '又': '530', '因': '531', '情': '532', '找': '533', '些': '534', '份': '535', '置': '536', '适': '537', '什': '538', '蛋': '539', '师': '540', '气': '541', '你': '542', '姐': '543', '棒': '544', '试': '545', '总': '546', '定': '547', '啊': '548', '足': '549', '级': '550', '整': '551', '带': '552', '虾': '553', '如': '554', '态': '555', '且': '556', '尝': '557', '主': '558', '话': '559', '强': '560', '当': '561', '更': '562', '板': '563', '知': '564', '己': '565', '无': '566', '酸': '567', '让': '568', '入': '569', '啦': '570', '式': '571', '笑': '572', '赞': '573', '片': '574', '酱': '575', '差': '576', '像': '577', '提': '578', '队': '579', '走': '580', '嫩': '581', '才': '582', '刚': '583', '午': '584', '接': '585', '重': '586', '串': '587', '回': '588', '晚': '589', '微': '590', '周': '591', '值': '592', '费': '593', '性': '594', '桌': '595', '拍': '596', '跟': '597', '块': '598', '调': '599', '糕': '600'}

cate_list = {
    '10': '美食',
    '15': 'K歌',
    '20': '购物',
    '25': '电影演出赛事',
    '30': '休闲娱乐',
    '35': '周边游',
    '40': '宴会',
    '45': '运动健身',
    '50': '丽人',
    '55': '结婚',
    '60': '酒店',
    '65': '爱车',
    '70': '亲子',
    '75': '学习培训',
    '80': '生活服务',
    '85': '医疗健康',
    '90': '家居',
    '95': '宠物',
}


# 最大重试次数/重试间隔(单位秒）
def retry(stop_max_attempt_number=10, wait_fixed=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            retry_num = 0
            while retry_num < stop_max_attempt_number:
                rs = None
                try:
                    rs = func(*args, **kw)
                    break
                except Exception as e:
                    run_ip()
                    retry_num += 1
                    time.sleep(wait_fixed)
                    if retry_num == stop_max_attempt_number:
                        raise Exception(e)
                finally:
                    if rs:
                        return rs
        return wrapper

    return decorator


class BroadbandDial_up(object):
    def connect(self):
        name = "宽带连接"
        username = '057762355592'
        password = "928858"
        cmd_str = "rasdial %s %s %s" % (name, username, password)
        res = os.system(cmd_str)
        if res == 0:
            print("连接成功")
        else:
            print(res)

    def disconnect(self):
        name = "宽带连接"
        cmdstr = "rasdial %s /disconnect" % name
        os.system(cmdstr)
        print('断开成功')

    def huan_ip(self):
        # 断开网络
        self.disconnect()
        # 开始拨号
        self.connect()


def run_ip():
    r = BroadbandDial_up()
    r.huan_ip()


class DaZongDP(object):
    def __init__(self):
        self.css_url = None
        self.review_tag = None
        self.shop_num = None
        self.tag_name = None
        self.address = None
        self.cat_name = None
        self.next_url = [1]

    def __len__(self):
        pass

    def request(self, url):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xmlq=0.9,image/webp,image/apng,*/*q=0.8,application/signed-exchangev=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Cookie': 'navCtgScroll=100; _lxsdk=1766018886cc8-04d7ab8077d427-5437971-4a574-1766020c6400; _lxsdk_cuid=1766018886cc8-04d7ab8077d427-5437971-4a574-1766020c6400; switchcityflashtoast=1; _hc.v=ce0d9b7c-277f-582f-7204-2d40c1c9a9cc.1614744421; s_ViewType=10; _tr.u=KmpIrpU4VFRQEB9E; _dp.ac.v=28882ee0-66fa-400f-a218-97da5a749b5b; ctu=2a2d9a661eb30bb6d36de26436e1fdf1857c55c22c0f2809953c81468300ca3a; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1619679169; source=m_browser_test_33; PHOENIX_ID=0a48873f-1791c776a08-610f; info="{\"query_id\":\"9dce19f9-c2a9-4884-99c4-0fe41c38b073\",\"ab_id\":\"exp000095_a\"}"; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_3713187639; uamo=18779340395; cityid=106; cy=106; cye=quzhou; fspop=test; pvhistory="6L+U5ZuePjo8L3F1emhvdS9jaCU3Qj46PDE2MjAzNzcxNDUyMTVdX1s="; m_flash2=1; default_ab=citylist%3AA%3A1%7Cshop%3AA%3A11%7Cindex%3AA%3A3%7CshopList%3AA%3A5%7Cmap%3AA%3A1%7Cmyinfo%3AA%3A1; thirdtoken=e9214815-06a0-41d9-a0ef-2ed692fff555; _thirdu.c=35551c46e88dbc3a47a53c2e949b3cbd; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1619677706,1619681417,1619753965,1620379992; aburl=1; Hm_lpvt_dbeeb675516927da776beeb1d9802bd4=1620380041; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1620640617; _lxsdk_s=17955b15b65-97b-196-418%7C%7C103',
            'Host': 'www.dianping.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }
        response = requests.get(url=url, headers=headers)
        # code = [200, '200']
        # r = response.text
        # if response.status_code not in code:
        #     self.huan_ip()
        return response

    def process_html(self, response):
        html = etree.HTML(response.text)
        ul_li = html.xpath('//*[@id="shop-all-list"]/ul/li')  # 多少个li标签
        number = len(ul_li)
        self.next_url = html.xpath('//*[@class="next"]/@href')
        self.css_url = 'https:' + str(re.findall('//s3plus\.meituan\.net.+?\.css', (response.text))[0])
        for i in range(1, number + 1):
            # 详情url
            details_url = html.xpath("//li[{}]//div[@class='tit']/a[1]/@href".format(i))[0]
            # 标题
            title = html.xpath("//li[{}]//div[@class='tit']/a[1]/h4/text()".format(i))[0]
            # 评分
            score = html.xpath('//li[1]//div[@class="nebula_star"]/div[2]/text()'.format(i))[0]
            # 评论数
            comment_str = html.xpath('//li[{}]//a[@class="review-num"]/b//text()'.format(i))
            comment = self.str_data('shop_num', comment_str)
            # 人均价
            people_money_str = html.xpath(
                "//ul/li[{}]/div[@class='txt']/div[@class='comment']/a[@class='mean-price']/b//text()".format(i))
            people_money = self.str_data('shop_num', people_money_str)
            details_responts = self.request(details_url)
            category_name = self.category_name(details_responts)
            process_data = self.process_item(title, score, comment, people_money, category_name)
            data_mysql = self.data_warehousing(process_data)

    def category_name(self, details_responts):
        html = etree.HTML(details_responts.text)
        category_list = html.xpath('//div[@class="breadcrumb"]/a/text()')
        return category_list

    @retry(stop_max_attempt_number=2, wait_fixed=1)
    def css_data_dict(self, cat_num):
        url = "https://www.dianping.com/quzhou/ch{}".format(cat_num)
        responts = self.request(url)
        self.css_url = 'https:' + str(re.findall('//s3plus\.meituan\.net.+?\.css', (responts.text))[0])
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 's3plus.meituan.net',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }
        r = requests.get(self.css_url, headers=headers).content.decode()
        css_woff_list = re.findall(',url\("(.*?)"\);} ', r)
        css_name = re.findall(';}.(.*?){font', r)
        data_list = []
        for url_s in css_woff_list:
            woff_url = 'https:' + url_s
            r = requests.get(woff_url, headers=headers).content
            from fontTools.ttLib import TTFont
            with open('responts.woff', 'wb')as f:
                f.write(r)
                f.close()
            addressfont = TTFont('responts.woff')
            addressfont.saveXML('responts.xml')
            address_TTGlyphs = addressfont['cmap'].tables[0].ttFont.getGlyphOrder()[2:]
            decrypt_data = {}
            address_dict = {}
            for i, x in enumerate(address_TTGlyphs):
                address_dict[x] = str(i)
            for k, v in zip(address_dict.keys(), css_dices.keys()):
                decrypt_data[k] = v
            data_list.append(decrypt_data)
        self.review_tag = data_list[2]
        self.shop_num = data_list[0]
        self.tag_name = data_list[3]
        self.address = data_list[1]

    def process_item(self, title, score, comment, people_money, category_name):
        item = dict()
        item['title'] = str(title).strip(' ')
        item['score'] = str(score)
        item['comment'] = comment
        item['price_text'] = people_money
        for i in range(0, len(category_name)):
            if i == 0:
                item['city_name'] = str(category_name[0]).strip(' ')
            elif i == 1:
                item['category_name'] = str(category_name[1]).strip(' ')
            elif i == 2:
                item['region_name'] = str(category_name[2]).strip(' ')
            elif i == 3:
                item['precise_name'] = str(category_name[3]).strip(' ')
        item['cat_name'] = self.cat_name
        print(item)
        return item

    def str_data(self, css_name, xpath_str):
        num_name = ''
        if css_name == 'shop_num':
            css_encryption = self.shop_num
        elif css_name == 'tag_name':
            css_encryption = self.tag_name
        elif css_name == 'address':
            css_encryption = self.address
        else:
            css_encryption = {}
        for i in range(0, len(xpath_str)):
            un_ue_str = str(xpath_str[i].encode('raw_unicode_escape').replace(b'\\', b''), 'utf-8')
            text = 'uni' + un_ue_str[1::1]
            if text in css_encryption.keys():
                num_name += css_encryption[text]
            else:
                num_name += str(xpath_str[i])
        return num_name

    def data_warehousing(self, process_data):
        with open('dazhongdianp.txt', 'a', encoding='utf-8')as f:
            for item_str in process_data.values():
                f.write(item_str)
            f.write('\n')

    def run_begin(self, cat_num, cat_name):
        self.css_data_dict(cat_num)
        self.next_url = "https://www.dianping.com/quzhou/ch{}".format(cat_num)
        self.cat_name = cat_name
        while True:
            responts = self.request(self.next_url)
            self.process_html(responts)
            if self.next_url == None:
                break


def run_d_z():
    run = DaZongDP()
    for cat_num, cat_name in zip(cate_list.keys(), cate_list.values()):
        run.run_begin(cat_num, cat_name)


if __name__ == '__main__':
    run_d_z()
