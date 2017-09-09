# coding:utf-8
import MySQLdb
import MySQLdb.cursors
from MySQLdb import MySQLError
from _mysql_exceptions import Warning, Error, InterfaceError, DataError, \
    DatabaseError, OperationalError, IntegrityError, InternalError, \
    NotSupportedError, ProgrammingError


class ConnectMySql(object):
    def __init__(self, data_base_type):
        self.data_base_type = data_base_type
        self.get_connect()
        self.cur = self.get_cusor

    # select mysql database
    def get_connect(self):
        if self.data_base_type == "work":
            self.connect = MySQLdb.connect(host="47.94.226.148",
                                           port=3306, user="root",
                                           passwd="root123", db="mydb",
                                           cursorclass=MySQLdb.cursors.DictCursor)

    # use with automatic get cursor
    @property
    def get_cusor(self):
        with self.connect as cur:
            self.connect.autocommit(True)
            return cur

    # get all data
    def get_all_data(self, sql):
        try:
            self.cur.execute(sql)
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
            result = self.cur.fetchone()
            return result if result else u"数据为空"
        except (Warning, Error, InterfaceError, DataError,
                DatabaseError, OperationalError, IntegrityError,
                InternalError, MySQLError, NotSupportedError,
                ProgrammingError) as e:
            print e

    # insert to database data
    def insert_data(self, sql):
        try:
            self.cur.execute(sql)
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
        except (Warning, Error, InterfaceError, DataError,
                DatabaseError, OperationalError, IntegrityError,
                InternalError, MySQLError, NotSupportedError,
                ProgrammingError) as e:
            print e
        else:
            print u"数据删除成功"

    # 清空表，将自增字段重置
    def emptied_table(self,table_name):
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
    db.emptied_table("user")

if __name__ == "__main__":
    main()
