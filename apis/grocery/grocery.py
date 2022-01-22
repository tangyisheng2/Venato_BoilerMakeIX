#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :grocery.py
# @Time      :1/21/22
# @Author    :Eason Tang
from flask import request
from flask_restful import Resource, reqparse


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

class Search(Resource):
    def post(self):
        """
        This function takes user input and searches & return all nutrition
        :return: Grocery.id[]
        """
        json_data = request.get_json()
        return json_data
