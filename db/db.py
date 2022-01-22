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
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='password',
                                          database='test',
                                          cursorclass=pymysql.cursors.DictCursor)

    def query(self, sql, have_respond: bool):
        """
        This function queries sql
        :param sql:
        :param have_respond:
        :return:
        """
        with self.connection:
            with self.connection.cursor() as cursor:
                # sql = "SELECT * FROM user JOIN test_relation ON user.id = test_relation.user_id"
                cursor.execute(sql)
                if have_respond:
                    ret = cursor.fetchall()
                    return 0, None, ret

                else:
                    return 0, None


if __name__ == '__main__':
    # For test
    test = DB()
    status, err, ret = test.query("SELECT * FROM test.user;", True)
    print(ret)
