#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :user.py
# @Time      :1/21/22
# @Author    :Eason Tang
from flask import request
from flask_restful import Resource, reqparse


class LogIn(Resource):
    def post(self):
        """
        This function takes username and password and create a user
        :return: User info
        """
        json_data = request.get_json()  # Where it takes json data
        return json_data


class SignUp(Resource):
    def post(self):
        """
        This function takes username and password, verify it and login and return the userinfo
        :return:
        """
        json_data = request.get_json()
        return json_data
        return "This function takes username and password, verify it and login and return the userinfo"
