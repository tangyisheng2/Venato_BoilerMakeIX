#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :grocery.py
# @Time      :1/21/22
# @Author    :Eason Tang
from flask_restful import Resource


class Grocery(Resource):
    @staticmethod
    def get():
        """
        This function takes user id and return all groceries the user have
        :return: Grocery.id[]
        """
        return "This function takes user id and return all groceries the user have"

    @staticmethod
    def post():
        """
        This function Add groceries to the database
        :return: Grocery.id[]
        """
        return "This function Add groceries to the database"
