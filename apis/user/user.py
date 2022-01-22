#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :user.py
# @Time      :1/21/22
# @Author    :Eason Tang
from flask_restful import Resource


class LogIn(Resource):
    @staticmethod
    def post():
        """
        This function takes username and password and create a user
        :return: User info
        """
        return "This function takes username and password and create a user"


class SignUp(Resource):
    @staticmethod
    def post():
        """
        This function takes username and password, verify it and login and return the userinfo
        :return:
        """
        return "This function takes username and password, verify it and login and return the userinfo"


