#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :db.py
# @Time      :1/22/22
# @Author    :Eason Tang
import pymysql.cursors


class DB():
    def __init__(self):
        # Connect to the database
        # Proxy is required
        self.init_connection()

    # def query(self, sql, have_response: bool):
    #     """
    #     This function queries sql
    #     :param sql:
    #     :param have_response:
    #     :return:
    #     """
    #     with self.connection:
    #         with self.connection.cursor() as cursor:
    #             # sql = "SELECT * FROM user JOIN test_relation ON user.id = test_relation.user_id"
    #             cursor.execute(sql)
    #             if "INSERT" in sql:
    #                 self.connection.commit()
    #             # if have_response:
    #             #     ret = cursor.fetchall()
    #             #     if ret:  # Has response
    #             #         return 0, None, ret
    #             #     else:
    #             #         return 0, None, None
    #             ret = cursor.fetchall()
    #             return 0, None, ret
    #
    #
    #     return -1, "Some Error Occurs", None

    def init_connection(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='password',
                                          database='test',
                                          cursorclass=pymysql.cursors.DictCursor)

    def query(self, sql):
        """
        This function queries sql
        :param sql:
        :param have_response:
        :return:
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            if "INSERT" in sql:
                self.connection.commit()
            ret = cursor.fetchall()
            return 0, None, ret
        except pymysql.err.Error:
            return -1, None, None

    def close(self):
        self.connection.close()


if __name__ == '__main__':
    # For test
    test = DB()
    status, err, ret = test.query("SELECT * FROM test.user;")
    print(ret)
