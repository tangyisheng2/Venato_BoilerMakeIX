#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :meal.py
# @Time      :1/21/22
# @Author    :Eason Tang
from flask_restful import Resource


class Meal(Resource):
    @staticmethod
    def get():
        """
        This function gets all the meals that the user have
        :return: Meal:id
        """
        return "This function gets all the meals that the user have"

    @staticmethod
    def post():
        """
        This function adds a meal to the user database
        :return: Meal[]
        """
        return "This function adds a meal to the user database"
