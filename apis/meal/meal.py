#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :meal.py
# @Time      :1/21/22
# @Author    :Eason Tang
from flask import request
from flask_restful import Resource
import db


class Meal(Resource):
    def __init__(self):
        self.db_session = db.DB()

    def get(self):
        """
        This function gets all the meals that the user have
        :return: Meal:id
        """
        self.db_session.init_connection()
        try:
            json_data = request.get_json()
            if "user_id" in json_data:
                user_id = json_data['user_id']
                # Check if user id is existed
                sql = "SELECT id FROM production.user WHERE id = %d" % user_id
                status, err, ret = self.db_session.query(sql)
                if not ret:
                    return {"status": -1, "msg": "User id does not exist"}
                # Get Meals from user id
                # todo Take care of the limit here
                sql = "SELECT * FROM production.meal WHERE user_id = %d LIMIT 20" % user_id
                status, err, ret = self.db_session.query(sql)
                if status == 0:
                    return {"status": 0, "msg": ret}
                else:
                    return {"status": status, "msg": "Something went wrong"}
        finally:
            self.db_session.close()
        return "This function gets all the meals that the user have"

    @staticmethod
    def post():
        """
        This function adds a meal to the user database
        :return: Meal[]
        """
        return "This function adds a meal to the user database"
