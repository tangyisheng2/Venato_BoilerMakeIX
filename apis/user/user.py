#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :user.py
# @Time      :1/21/22
# @Author    :Eason Tang
from flask import request
from flask_restful import Resource, reqparse
import db


class LogIn(Resource):
    def __init__(self):
        self.db_session = db.DB()

    def post(self, username):
        """
        This function takes username and password and create a user
        :return: User info
        """
        json_data = request.get_json()  # Where it takes json data
        if json_data['username'] and json_data['password']:
            sql = f'SELECT t.*  FROM test.user t  ' \
                  f'WHERE username = "{str(json_data["username"])}" ' \
                  f'AND password = "{str(json_data["password"])}" LIMIT  1'
            status, errmsg, ret = self.db_session.query(sql)
            if status == 0:  # Login Success
                return {"status": 0, "userid": ret[0]['id'], "username": ret[0]['username']}
            else:
                return {"status": status, "errmsg": errmsg}
        else:
            return {"status": -1, "errmsg": "Login Failed"}


class SignUp(Resource):
    def __init__(self):
        self.db_session = db.DB()

    def post(self):
        """
        This function takes username and password, verify it and login and return the userinfo
        :return:
        """
        json_data = request.get_json()
        if json_data['username'] and json_data['password']:
            # Register User
            sql = f'INSERT INTO test.user (username,password) ' \
                  f'VALUES ("{json_data["username"]}","{json_data["password"]}")'
            status, errmsg, ret = self.db_session.query(sql)
            if status == 0:  # Login Success
                # Fetch User
                sql = f'SELECT t.*  FROM test.user t  ' \
                      f'WHERE username = "{str(json_data["username"])}" ' \
                      f'AND password = "{str(json_data["password"])}" LIMIT  1'
                status, errmsg, ret = self.db_session.query(sql)
                if status == 0:
                    return {"status": 0, "userid": ret[0]['id'], "username": ret[0]['username']}
                else:
                    return {"status": status, "errmsg": errmsg}
            else:
                return {"status": -1, "errmsg": "Some error occur, registration failed, the username might already taken"}
        else:
            return {"status": -2, "errmsg": "Username and password no valid"}
