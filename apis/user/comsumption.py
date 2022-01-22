#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :comsumption.py
# @Time      :1/21/22
# @Author    :Eason Tang
from flask_restful import Resource


class Comsumption(Resource):
    @staticmethod
    def post():
        """
        This function takes meal id and subtract the eaten groceries in the stock
        :return: User daily consumption
        """
        return "This function takes meal id and subtract the eaten groceries in the stock"

    @staticmethod
    def get():
        """
        This function takes user id and get the daily consumption from user database
        :return: DailyConsumption
        """
        return "This function takes user id and get the daily consumption from user database"
