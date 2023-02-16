import hashlib
import random, re
import json
import http.client
from urllib import parse
from 统计局需求_2.sql_pool.pymysql_pool import DataBaseSession
from 统计局需求_2.sql_pool.dbpool import kjoridata_1_4_pool, kj_1_4_pool
company_mysql = DataBaseSession(kj_1_4_pool)
company_mysql_oridata = DataBaseSession(kjoridata_1_4_pool)


# 英文翻译成中文
def translate_t(q_s):
    httpClient = None
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    fromLang = 'auto'  # 原文语种[自动检测]
    toLang = 'zh'  # 译文语种[中文]
    appid = '20230202001547745'
    salt = random.randint(32768, 65536)
    if 'img' not in q_s and q_s != '':
        q_t = q_s.replace('.', '')
        sign = appid + q_t + str(salt) + 'z5ifAci54XGjckF76eP_'
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl1 = myurl + '?q=' + parse.quote(q_t) + '&from=' + fromLang + '&to=' + toLang + '&appid=' + appid + '&salt=' + str(
            salt) + '&sign=' + sign
        ## http://api.fanyi.baidu.com/api/trans/vip/translate?q=apple&from=en&to=zh&appid=2015063000000001&salt=1435660288&sign=f89f9594663708c1605f3d736d01d2d4
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl1)
            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            jg = (result['trans_result'][0]['dst'])
        except Exception as e:
            print(e)
            jg = '接口请求出错'
        finally:
            if httpClient:
                httpClient.close()
        return jg
    else:
        return q_s


def fanyi_comapy_mysql():
    with open(r'X:\数据库\速卖通\速卖通_拍照信息\{速卖通牌照信息_001}[公司名称,地址].txt', 'r', encoding='utf-8') as company_list:
        for company in company_list:
            company_name = company.strip().split(',')
            new_company_list = []
            for i in company_name:
                if 'img' not in i and i != '':
                    qs = i.replace('.', '')
                    q_f = translate_t(qs)
                    new_company_list.append(q_f)
            if len(new_company_list) == 2:
                insertion_sql = "insert into company_crossname_2212 (company, company_address) VALUES (%s,%s)"
                company_mysql_oridata.insertion_data(insertion_sql, new_company_list)
            else:
                print(company_name)


def fanyi_comapy():
    new_txt = open(r'X:\数据库\速卖通\{速卖通牌照信息_本月_备份}[店铺ID,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关,省,市,区].txt', 'w', encoding='utf-8')
    with open(r'X:\数据库\速卖通\{速卖通牌照信息_001}[店铺ID,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关].txt', 'r', encoding='utf-8') as company_list:
        for company in company_list:
            company_name_list = company.strip().split(',')
            company_name = translate_t(company_name_list[1])
            company_addres = translate_t(company_name_list[4])
            company_name_list[1] = company_name
            company_name_list[4] = company_addres
            new_txt.write(','.join(company_name_list) + '\n')
            new_txt.flush()
            print(company_name, company_addres)
        new_txt.close()


if __name__ == '__main__':
    fanyi_comapy()

