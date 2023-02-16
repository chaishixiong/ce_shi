from DBUtils.PooledDB import PooledDB
import pymysql
pool = PooledDB(
    creator=pymysql,
    maxconnections=5,
    mincached=2,
    maxcached=5,
    maxshared=3,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=0,
    port=9227,
    host='192.168.0.227',
    user='update',
    password="change227NRIAT!#$",
    db="oridata_taobao",
    charset='utf8'
)

pool_smt = PooledDB(
    creator=pymysql,
    maxconnections=5,
    mincached=2,
    maxcached=5,
    maxshared=3,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=0,
    port=9227,
    host='192.168.0.227',
    user='update',
    password="change227NRIAT!#$",
    db="ec_cross_border",
    charset='utf8'
)


pool_tmall = PooledDB(
    creator=pymysql,
    maxconnections=5,
    mincached=2,
    maxcached=5,
    maxshared=3,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=0,
    port=9227,
    host='192.168.0.227',
    user='update',
    password="change227NRIAT!#$",
    db="oridata_tmall",
    charset='utf8'
)