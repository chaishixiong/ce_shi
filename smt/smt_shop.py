import requests


class SmtShopScore(object):
    def __init__(self):
        pass

    def request(self):
        pass

    def data_analysis(self):
        pass

    def run_spider(self):
        pass


def run_smt():
    r = SmtShopScore()
    r.run_spider()


if __name__ == "__main__":
    # 导入pymysql模块
    import pymysql
    # 连接database
    aa = ('6260', 'A正确答案为{b7722c76082f161e240595cdd88f5437}')
    conn = pymysql.connect(host="192.168.0.227", user="update", password="change227NRIAT!#$", port=9227, database="life_server", charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    # 定义要执行的SQL语句
    sql = """insert into qb_analysis_ceshi (title_id, content) VALUES (6260,'A正确答案为{b7722c76082f161e240595cdd88f5437}')"""
    # 执行SQL语句
    cursor.execute(sql)
    conn.commit()
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()



