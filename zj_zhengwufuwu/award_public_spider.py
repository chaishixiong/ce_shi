'''
浙江政务服务网爬虫

'''
import requests
import json
import time
from sql.mysqlhelper import MySqLHelper


class AwardPublic(object):
    def __init__(self):
        pass

    def request_post(self, start):
        url = 'http://reward.wenzhou.gov.cn/app/publicity/all'
        header = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "x-requested-with": "XMLHttpRequest",
            "Cookie": "csrftoken=35M3BwgvLQdBTP6MzdJrdff0iYbk1nMQj22XiNrOc86TgFfqIuXOPvgJl8PCPkZy; area=%E5%85%A8%E5%9C%B0%E5%8C%BA"
        }
        data = {
            'csrfmiddlewaretoken': '61k0LNzZCy52cEoIqDABwMQY5yBNLnSlmYAUs4Ki3QYkzuxmzUOY82RH8If5zk53',
            'draw': '0',
            'start': start,
            'length': '100',
            'p_area': '全地区'
        }
        r = requests.post(url=url, headers=header, data=data)
        d = r.content.decode('unicode-escape').replace('\t', '')
        return d

    def data_parser(self, data):
        item = dict()
        item['inst_id'] = data['inst_id']  # 编号
        item['company_name'] = data['company_name']  # 申报单位
        item['project_name'] = data['project_name']  # 奖补项目
        item['reward'] = data['reward']  # 补奖金额
        item['start_dt'] = data['start_dt']  # 开始时间
        item['end_dt'] = data['end_dt']  # 结束时间
        item['proc_sts'] = data['proc_sts']  # 状态

        detail_item_data = tuple(item.values())
        return detail_item_data


    def open_sql(self, sql, param=None):
        db = MySqLHelper()
        ret = db.insertone(sql=sql, param=param)

    def run_spider(self):
        start = 0
        while True:
            list_list = []
            data_str = self.request_post(start)
            data_dict = json.loads(data_str)
            data_list = data_dict['data']
            for data in data_list:
                d = self.data_parser(data)
                list_list.append(d)
            detail_sql = "insert into zj_zhengwufuwu (inst_id, company_name, project_name, reward, start_dt, end_dt, proc_sts) VALUES (%s,%s,%s,%s,%s,%s,%s);"
            self.open_sql(detail_sql, list_list)
            time.sleep(3)
            print(start)
            start += 100
            if start > 263400:
                break


if __name__ == '__main__':
    r = AwardPublic()
    r.run_spider()
    # a = "浙江省瑞安经济开发区管理委员会	"
    # print(a)


