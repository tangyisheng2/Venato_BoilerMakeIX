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

    def post(self):
        """
        This function adds a meal to the user database
        CreateMeal(User.id, name, Grocery.id[], grocery_weights[]): Meal
        # will delete corresponding amounts of grams from Groceries. If the amount of grams in “grocery_weights” is greater than or equal to Grocery.amt_g then change the “grocery_weight” to match it and delete the grocery from the user
        # and create meal
        :return: Meal[]
        """
        self.db_session.init_connection()
        try:
            json_data = request.get_json()
            # todo refine api
            if len(json_data) >= 3 and "user_id" in json_data and "name" in json_data and "grocery" in json_data:
                # todo parse ingredient data to subtract from grocery
                # Insert Data
                user_id = json_data['user_id']
                name = json_data['name']
                grocery = json_data['grocery']
                # sql = 'INSERT INTO production.meal (user_id, name, image_url) VALUES ("%d", "%s", "%s")' \
                #       % (user_id, name, grocery)
                sql = 'INSERT INTO production.meal (user_id, name, image_url) VALUES ("%d", "%s", "%s")' \
                      % (user_id, name, None)
                status, err, ret = self.db_session.query(sql)
                # Get the last insert ID
                sql = "SELECT last_insert_id()"
                status, err, ret = self.db_session.query(sql)
                last_id = ret[0]['last_insert_id()']
                # Fetch the inserted data
                sql = 'SELECT * FROM production.meal WHERE id = %d LIMIT 1' % last_id
                status, err, ret = self.db_session.query(sql)
                if status == 0:
                    return {"status": status, "msg": ret}
                else:
                    return {"status": status, "msg": "Some thing went wrong"}
            else:
                return {"status": -1, "msg": "invalid input"}
        finally:
            self.db_session.close()
