import time
from datetime import datetime, timedelta

# from pics.base import util

# datetime_now = datetime.now()
# time_time = time.time()
# time_local = time.localtime()
# datetime_utcnow = datetime.utcnow()
#
# # 本地时间
# print(datetime_now)  # 2019-07-08 11:32:11.738098
# print(time_time)        # 1562556731.738098
# print(time.strftime("%Y-%m-%d %H:%M:%S",time_local))   # time.struct_time(tm_year=2019, tm_mon=7, tm_mday=8, tm_hour=11, tm_min=48, tm_sec=56, tm_wday=0, tm_yday=189, tm_isdst=0)
# time_time = 1626932771000
# time_time_date = datetime.fromtimestamp(time_time)
# print(time_time_date)   # 2019-07-08 11:34:33.822897
#
# # 零时区 # 格林威治时间
# print(datetime_utcnow)  # 2019-07-08 03:32:11.738098
#
# # 本地时间的昨天明天
# yestday = datetime_now - timedelta(days=1)
# tomorrow = datetime_now + timedelta(days=1)
# print(yestday)   # 2019-07-07 11:36:08.371032
# print(tomorrow)     # 2019-07-09 11:36:08.371032

# 有效期的到期日

# print(t_b)


# 时区转换 (零时区转为东八区)
# from datetime import datetime, timedelta
#
# now_time = datetime.utcnow()  # 2019-07-08 10:54:04.376723
#
# utc_time = now_time + timedelta(hours=8)  # UTC只是比北京时间提前了8个小时,所以零时区时间加上八小时
#
# utc_time = utc_time.strftime("%Y-%m-%d %H:%M:%S")  # 2019-07-08 18:54:04
# timestamp = 1626932771
#
#
# #转换成localtime
# time_local = time.localtime(timestamp)
# #转换成新的时间格式(2016-05-05 20:28:54)
# dt = time.strftime("%Y-%m-%d", time_local)
# print(dt)

dt = '2021-07'
ts = int(time.mktime(time.strptime(dt, "%Y-%m")))
print(ts)
1626932771
1625068800