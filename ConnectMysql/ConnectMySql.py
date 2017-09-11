# coding:utf-8
import MySQLdb
import MySQLdb.cursors
import time
from MySQLdb import MySQLError
from _mysql_exceptions import Warning, Error, InterfaceError, DataError, \
    DatabaseError, OperationalError, IntegrityError, InternalError, \
    NotSupportedError, ProgrammingError


class ConnectMySql(object):
    def __init__(self, data_base_type):
        self.data_base_type = data_base_type
        self.get_connect()

    # select mysql database
    def get_connect(self):
        if self.data_base_type == "work":
            self.connect = MySQLdb.connect(host="47.94.226.148",
                                           port=3306, user="root",
                                           passwd="root123", db="mydb",
                                           cursorclass=MySQLdb.cursors.DictCursor)
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
            print e

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
            print e

    # insert to database data
    def insert_data(self, sql,data_list):
        try:
            self.cur.execute(sql,data_list)
            self.connect.commit()
        except (Warning, Error, InterfaceError, DataError,
                DatabaseError, OperationalError, IntegrityError,
                InternalError, MySQLError, NotSupportedError,
                ProgrammingError) as e:
            print e
        else:
            print u"数据插入完成"

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
            print e
        else:
            print u"数据插入完成"
    # delete data
    def delete_data(self, sql):
        try:
            self.cur.execute(sql)
            self.connect.commit()
        except (Warning, Error, InterfaceError, DataError,
                DatabaseError, OperationalError, IntegrityError,
                InternalError, MySQLError, NotSupportedError,
                ProgrammingError) as e:
            print e
        else:
            print u"数据删除成功"

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
            print e
        else:
            print "%s表已清空" % table_name


def main():
    db = ConnectMySql("work")
    db.get_connect()
    sql = "insert into `user` (`name`) VALUES (%s)"
    # a = [[i] for i in range(50001)]
    a = [[1],[2]]
    start = time.clock()
    print start
    db.insert_data(sql, a)
    cur = db.cur
    conn = db.connect
    cur.close() if cur else u"使用"
    conn.close() if conn else u"使用"
    end = time.clock()
    print end
    print "finish use %s" % (end - start)


if __name__ == "__main__":
    main()
    # ConnectMySql("work").emptied_table('user')
