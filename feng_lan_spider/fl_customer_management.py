import requests
import json
import time
from feng_lan_spider.feng_lan_settings import headers, parmas_detail, parmas_list, parmas_all
from sql.mysqlhelper import MySqLHelper


class FengLanCustomerManagement(object):
    def __init__(self):
        self.num = 1
        self.item_id = ''
        self.log_in = {
                    "account": "shenhailong@findland.cn",
                    "agentId": "2",
                    "password": "qwe123qwe",
                    "platform": 2
        }
        #
        # self.token_str = 'ab0c04c6bb7c422c918944bf1f5f1942'

    def request_post(self, url, parmas):
        # headers['tokrn'] = self.token_str
        r = requests.request('POST', url=url, headers=headers, data=json.dumps(parmas))
        data = r.content.decode()
        data_dict = json.loads(data)
        # if data_dict['code'] == 13010000 and data_dict['msg'] == '登录超时或会话已失效！':
        #     self.token_str, times = self.log_in_token(self.log_in)
        #     headers['tokrn'] = self.token_str
        #     # headers['timestamp'] = times
        #     r = requests.request('POST', url=url, headers=headers, data=json.dumps(parmas))
        #     data_str = r.content.decode()
        #     data_data = json.loads(data_str)
        #     return data_data
        return data_dict

    def process_item(self, rccords, detail_data, contact_data, call_log_data, site_data):
        detail_item = dict()
        contact_item = dict()
        call_log_item = dict()
        site_item = dict()
        detail_data = detail_data['data']
        contact_data = contact_data['data']
        call_log_data = call_log_data['data']
        site_data = site_data['data']

        # 基本信息
        detail_item['crm'] = '客户管理'  # CRM
        detail_item['system_id'] = detail_data['id']  # 系统编号
        detail_item['company_name'] = detail_data['name']  # 客户名称
        detail_item['company_email'] = detail_data['email']  # 公司邮箱
        detail_item['area'] = str(detail_data['area'].split(',')) if len(detail_data['area']) > 0 else ''  # 客户区域
        detail_item['source_id'] = detail_data['sourceId']  # 客户来源
        detail_item['industry'] = rccords['industry']  # 客户行业 。。。。。
        detail_item['level'] = rccords['level']  # 客户级别 。。。。。
        detail_item['login_email'] = detail_data['loginEmail']  # 登录邮箱
        detail_item['seller_name'] = rccords['sellerName']  # 客户经理 。。。。。
        detail_item['website'] = detail_data['website']  # 客户网址
        detail_item['company_phone'] = detail_data['phone']  # 公司电话
        detail_item['address'] = detail_data['address']  # 公司地址
        if detail_data['state'] == 0:
            detail_item['state'] = '公海客户'  # 客户状态 。。。。。
        elif detail_data['state'] == 1:
            detail_item['state'] = '保留客户'  # 客户状态 。。。。。
        elif detail_data['state'] == 2:
            detail_item['state'] = '签约客户'
        elif detail_data['state'] == 3:
            detail_item['state'] = '断约客户'
        else:
            detail_item['state'] = ''
        detail_item['products'] = detail_data['products']  # 主营产品
        detail_item['password'] = detail_data['password']  # 登录密码
        detail_item['create_time'] = self.times_time(detail_data['createTime'])  # 创建时间
        detail_item['keep_time'] = self.times_time(detail_data['keepTime'])  # 认领时间 *****
        detail_item['update_time'] = self.times_time(detail_data['updateTime'])  # 最后修改时间
        detail_item['contact_time'] = self.times_time(detail_data['contactTime'])  # 最后联系时间
        detail_item['remark'] = detail_data['remark']  # 备注
        # with open('detail_text.txt', 'a', encoding='utf-8')as f:
        #     for i in detail_item.values():
        #         f.write(i + ',')
        #     f.write('\n')
        detail_sql = "insert into feng_lan_detail_copy1 (crm, system_id, company_name, company_email, area, source_id, industry, level, login_email, seller_name, website, company_phone, address, state, products, password, create_time, keep_time, update_time, contact_time, remark) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        detail_item_data = tuple(detail_item.values())
        self.open_sql(detail_sql, detail_item_data)
        if len(contact_data) != 0:
            # 联系人
            for c_data in contact_data:
                contact_item['crm'] = '客户管理'  # CRM
                contact_item['system_id'] = detail_data['id']  # 系统编号
                contact_item['contact_name'] = c_data['realName']  # 姓名
                contact_item['contact_position'] = c_data['position']  # 职位
                contact_item['contact_phone'] = c_data['phone']  # 座机号
                contact_item['contact_mobile'] = c_data['mobile']  # 手机号
                contact_item['contact_email'] = c_data['email']  # 邮箱
                contact_item['contact_wechat'] = c_data['wechat']  # 微信
                contact_item['contact_remark'] = c_data['remark']  # 备注
                # with open('contact_text.txt', 'a', encoding='utf-8')as f:
                #     for i in contact_item.values():
                #         f.write(i + ',')
                #     f.write('\n')
                contact_sql = "insert into feng_lan_contact_copy1 (crm, system_id, contact_name, contact_position, contact_phone, contact_mobile, contact_email, contact_wechat, contact_remark) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                contact_item_data = tuple(contact_item.values())
                self.open_sql(contact_sql, contact_item_data)
        if len(call_log_data) != 0:
            # 联系记录
            for cl_data in call_log_data:
                call_log_item['crm'] = '客户管理'  # CRM
                call_log_item['system_id'] = detail_data['id']  # 系统编号
                call_log_item['call_log_contactman'] = cl_data['contactMan']  # 姓名
                call_log_item['call_log_operator'] = cl_data['operator']  # 客户经理
                call_log_item['call_log_contactmethod'] = cl_data['contactMethod']  # 联系方式
                call_log_item['call_log_createtime'] = self.times_time(cl_data['createTime'])  # 联系日期
                call_log_item['call_log_remark'] = cl_data['remark']  # 跟进情况
                # with open('call_log_text.txt', 'a', encoding='utf-8')as f:
                #     for i in call_log_item.values():
                #         f.write(i + ',')
                #     f.write('\n')
                call_log_sql = "insert into feng_lan_call_log_copy1 (crm, system_id, call_log_contactman, call_log_operator, call_log_contactmethod, call_log_createtime, call_log_remark) VALUES (%s,%s,%s,%s,%s,%s,%s);"
                call_log_item_data = tuple(call_log_item.values())
                self.open_sql(call_log_sql, call_log_item_data)
            # 客户站点
        if len(site_data) != 0:
            print('-----------------------------{}-----------------------------'.format(detail_data['id']))
            site_item['site_name'] = ''  # 网站名称
            site_item['domain_name'] = ''  # 域名
            site_item['language_version'] = ''  # 语言版本
            site_item['creation_time'] = ''  # 创建时间
            site_item['expire_date'] = ''  # 到期时间
        print(detail_item)
        print(contact_item)
        print(call_log_item)
        print('---------------------------------------------------------------')

    def times_time(self, times):
        expired_at = times // 1000
        timeArray = time.localtime(expired_at)
        time_times = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
        return time_times

    def open_sql(self, sql, param=None):
        db = MySqLHelper()
        ret = db.insertone(sql=sql, param=param)

    def run_feng_lan(self):
        for self.num in range(1, 831):
            list_url = 'https://api.fomille.com/agent/api/merchant/merchant/customer-paging'
            detail_url = 'https://api.fomille.com/agent/api/merchant/merchant/detail'
            contact_url = 'https://api.fomille.com/agent/api/merchant/contact/list'
            call_log_url = 'https://api.fomille.com/agent/api/merchant/track/list'
            site_url = 'https://api.fomille.com/merchant/api/site/site/list-by-merchant'
            parmas_list["current"] = self.num
            response = self.request_post(list_url, parmas_list)
            # rccords_dict = self.rccords_str(response)
            rccords_list = response['data']['records']
            try:
                for rccords in rccords_list:
                    self.item_id = rccords['id']
                    parmas_detail["id"] = self.item_id
                    parmas_all['merchantId'] = self.item_id
                    detail_data = self.request_post(detail_url, parmas_detail)
                    contact_data = self.request_post(contact_url, parmas_all)
                    call_log_data = self.request_post(call_log_url, parmas_all)
                    site_data = self.request_post(site_url, parmas_all)
                    data_data = self.process_item(rccords, detail_data, contact_data, call_log_data, site_data)
                    # print(detail_data)
            except Exception as e:
                print(e)

    def log_in_token(self, parmas):
        times = str(int(time.time() * 1000))
        long_in_url = 'https://api.fomille.com/platform/api/member/member/login'
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "app": "fomille",
            "content-type": "application/json;charset=UTF-8",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sign": "c48d15e93d8478ed88ff9949246c3178",
            "timestamp": times,
            "token": "undefined"
        }
        r = requests.request('POST', url=long_in_url, headers=headers, data=json.dumps(parmas))
        data = r.content.decode()
        data_dict = json.loads(data)
        token_str = data_dict['data']['token']
        return token_str, times


def run_feng_lan():
    run = FengLanCustomerManagement()
    run.run_feng_lan()


if __name__ == '__main__':
    run_feng_lan()
