import pymysql


class DataBaseSession(object):
    def __init__(self, pool):
        self.__conn = pool.connection()

    @property
    def connection(self):
        return self.__conn

    def begin(self):
        self.__conn.begin()

    def rollback(self):
        self.__conn.rollback()

    def commit(self):
        self.__conn.commit()

    def updata_data(self, sql: str, args=None):
        cursor = self.__conn.cursor()
        cursor.execute(sql)
        self.commit()
        res = cursor.fetchall()
        # 关闭游标对象
        cursor.close()
        return res

    def query_tuple_data(self, sql: str, args=None):
        cursor = self.__conn.cursor()
        cursor.execute(sql, args)
        self.commit()
        res = cursor.fetchall()
        # 关闭游标对象
        cursor.close()
        return res

    def insertion_data(self, sql: str, args=None):
        cursor = self.__conn.cursor()
        cursor.execute(sql, args)
        self.commit()
        res = cursor.fetchall()
        # 关闭游标对象
        cursor.close()
        return res

    def insertion_data_list(self, sql: str, args=None):
        cursor = self.__conn.cursor()
        cursor.executemany(sql, args)
        self.commit()
        res = cursor.fetchall()
        # 关闭游标对象
        cursor.close()
        return res

    def query_dict_fetchall(self, sql: str, args=None):
        cursor = self.__conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        res = cursor.fetchall()
        # 关闭游标对象
        cursor.close()
        return res

    def execute(self, sql: str, args=None):
        cursor = self.__conn.cursor()
        lines = cursor.execute(sql, args)
        return lines

    def __del__(self):
        self.__conn.close()
