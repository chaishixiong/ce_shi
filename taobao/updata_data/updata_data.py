#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("120.24.100.34", "reader", "reader", "elecb_data", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT * FROM `taobao_qiye_shopinfo_202011_cp` where province = '浙江省'")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchall()
# 关闭数据库连接
db.close()