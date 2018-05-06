import pymysql

import pymysql.cursors
import time
from pymysql import MySQLError
from pymysql import Warning, Error, InterfaceError, DataError, \
    DatabaseError, OperationalError, IntegrityError, InternalError, \
    NotSupportedError, ProgrammingError


class ConnectMySql(object):
    def __init__(self, data_base_type):
        self.data_base_type = data_base_type
        # self.get_connect()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    # select mysql database
    def get_connect(self):
        '''
        :param
        :return:
        '''
        if self.data_base_type == 1:
            self.connect = pymysql.connect(host="101.201.78.229",
                                           port=3406, user="root",
                                           passwd="root", db="faygo",
                                           charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.connect.cursor()

    # get all data
    def get_all_data(self, sql):
        try:
            self.cur.execute(sql)
            self.connect.commit()
            result = self.cur.fetchall()
            return result if result else u"数据为空"
        except (Warning, Error, InterfaceError, DataError,
                DatabaseError, OperationalError, IntegrityError,
                InternalError, MySQLError, NotSupportedError,
                ProgrammingError) as e:
            print(e)

    # get first row data
    def get_first_row_data(self, sql):
        try:
            self.cur.execute(sql)
            self.connect.commit()
            result = self.cur.fetchone()
            return result if result else u"数据为空"
        except (Warning, Error, InterfaceError, DataError,
                DatabaseError, OperationalError, IntegrityError,
                InternalError, MySQLError, NotSupportedError,
                ProgrammingError) as e:
            print(e)

    # insert to database data
    def insert_data(self, sql):
        '''
        @param (list)
        '''
        try:
            # self.cur.execute(sql)
            map(lambda i: self.cur.execute(i), sql)
            self.connect.commit()
        except (Warning, Error, InterfaceError, DataError,
                DatabaseError, OperationalError, IntegrityError,
                InternalError, MySQLError, NotSupportedError,
                ProgrammingError) as e:
            print(e)
        else:
            print("数据插入完成")

    # insert multiple data
    '''
    :param sql = "insert into `user` (`name`) VALUES (%s)"
    :param data_tup = [[i] for i in range(50001)]
    '''

    def insert_multi_data(self, sql, data_tup):
        try:
            self.cur.executemany(sql, data_tup)
            self.connect.commit()
        except (Warning, Error, InterfaceError, DataError,
                DatabaseError, OperationalError, IntegrityError,
                InternalError, MySQLError, NotSupportedError,
                ProgrammingError) as e:
            print(e)
        else:
            print("数据插入完成")

    # delete data
    def delete_data(self, sql):
        try:
            map(lambda i: self.cur.execute(i), sql)
            self.connect.commit()
        except (Warning, Error, InterfaceError, DataError,
                DatabaseError, OperationalError, IntegrityError,
                InternalError, MySQLError, NotSupportedError,
                ProgrammingError) as e:
            print(e)
        else:
            print("数据删除成功")

    # close cursor
    def close(self):
        self.cur.close()

    # 清空表，将自增字段重置
    def emptied_table(self, table_name):
        try:
            self.cur.execute("TRUNCATE TABLE %s" % table_name)
        except (Warning, Error, InterfaceError, DataError,
                DatabaseError, OperationalError, IntegrityError,
                InternalError, MySQLError, NotSupportedError,
                ProgrammingError) as e:
            print(e)
        else:
            print("%s表已清空") % table_name


def main():
    db = ConnectMySql("work")
    db.get_connect()
    sql = "insert into `user` (`name`) VALUES (%s)"
    # a = [[i] for i in range(50001)]
    a = [[1], [2]]
    start = time.clock()
    print(start)
    db.insert_data(sql, a)
    cur = db.cur
    conn = db.connect
    cur.close() if cur else u"使用"
    conn.close() if conn else u"使用"
    end = time.clock()
    print(end)
    print("finish use %s" % (end - start))


if __name__ == "__main__":
    with ConnectMySql(data_base_type=1) as mysql:
        mysql.get_connect()
