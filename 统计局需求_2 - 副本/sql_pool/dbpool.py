from DBUtils.PooledDB import PooledDB
import pymysql
tm_pool = PooledDB(
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

tm_104_pool = PooledDB(
    creator=pymysql,
    maxconnections=5,
    mincached=2,
    maxcached=5,
    maxshared=3,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=0,
    port=3306,
    host='192.168.7.104',
    user='root',
    password="hzAllroot",
    db="oridata_tmall",
    charset='utf8'
)

tm_228_pool = PooledDB(
    creator=pymysql,
    maxconnections=5,
    mincached=2,
    maxcached=5,
    maxshared=3,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=0,
    port=9228,
    host='192.168.0.228',
    user='update',
    password="up228JSDF!76avx",
    db="e_commerce",
    charset='utf8'
)

tb_228_pool = PooledDB(
    creator=pymysql,
    maxconnections=5,
    mincached=2,
    maxcached=5,
    maxshared=3,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=0,
    port=9228,
    host='192.168.0.228',
    user='update',
    password="up228JSDF!76avx",
    db="e_commerce",
    charset='utf8'
)

tb_pool = PooledDB(
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


tb_104_pool = PooledDB(
    creator=pymysql,
    maxconnections=5,
    mincached=2,
    maxcached=5,
    maxshared=3,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=0,
    port=3306,
    host='192.168.7.104',
    user='root',
    password="hzAllroot",
    db="oridata_taobao",
    charset='utf8'
)


jd_pool = PooledDB(
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
    db="oridata_jd",
    charset='utf8'
)

jd_104_pool = PooledDB(
    creator=pymysql,
    maxconnections=5,
    mincached=2,
    maxcached=5,
    maxshared=3,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=0,
    port=3306,
    host='192.168.7.104',
    user='root',
    password="hzAllroot",
    db="oridata_jd",
    charset='utf8'
)

e_commerce_104 = PooledDB(
    creator=pymysql,
    maxconnections=5,
    mincached=2,
    maxcached=5,
    maxshared=3,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=0,
    port=3306,
    host='192.168.7.104',
    user='root',
    password="hzAllroot",
    db="e_commerce",
    charset='utf8'
)

shop_228_pool = PooledDB(
    creator=pymysql,
    maxconnections=5,
    mincached=2,
    maxcached=5,
    maxshared=3,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=0,
    port=9228,
    host='192.168.0.228',
    user='update',
    password="up228JSDF!76avx",
    db="e_commerce",
    charset='utf8'
)

jh_228_pool = PooledDB(
    creator=pymysql,
    maxconnections=5,
    mincached=2,
    maxcached=5,
    maxshared=3,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=0,
    port=9228,
    host='192.168.0.228',
    user='update',
    password="up228JSDF!76avx",
    db="jh_online_retail",
    charset='utf8'
)


suning_227_pool = PooledDB(
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
    db="oridata_ec_other",
    charset='utf8'
)


kuajing_227_pool = PooledDB(
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

life_227_pool = PooledDB(
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
    db="life_server",
    charset='utf8mb4'
)

company_pool = PooledDB(
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
    db="oridata",
    charset='utf8'
)




