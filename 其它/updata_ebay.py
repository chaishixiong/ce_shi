from sql.mysqlhelper import MySqLHelper


def open_sql(sql, param=None):
    import redis
    num = 0
    db = MySqLHelper()
    ret = db.selectall(sql=sql, param=param)
    redisPool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=2, decode_responses=True, password="nriat.123456")
    redis = redis.Redis(connection_pool=redisPool)
    redis.delete('updata_eb')
    for up_data in ret:
        str_str = up_data[0] + ',' + up_data[1]
        redis.sadd('updata_eb', str_str)


def ger_redis():
    import redis
    import time
    while True:
        a = time.time()
        db = MySqLHelper()
        redisPool = redis.Redis(host='127.0.0.1', port=6379, db=2, decode_responses=True, password="nriat.123456")
        data = redisPool.spop('updata_eb')
        list_data = data.split(',')
        updata_sql = 'UPDATE ebay_goodsinfo_202105_copy1 SET good_id = %s WHERE good_name = %s'
        t_param = (list_data[0], list_data[1])
        print(list_data)
        new_data = db.selectall(sql=updata_sql, param=t_param)
        b = time.time()
        c = b-a
        print(c)


if __name__ == '__main__':
    sql = 'select good_id,good_name from ebay_goodsinfo_202104 limit 100'
    # open_sql(sql)
    ger_redis()

    # for i in range(5):
    #     t = Thread(target=ger_redis)
    #     t.start()



