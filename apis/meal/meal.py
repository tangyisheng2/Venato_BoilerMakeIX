#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :meal.py
# @Time      :1/21/22
# @Author    :Eason Tang
from flask import request
from flask_restful import Resource, reqparse
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
            parser = reqparse.RequestParser()
            parser.add_argument('user_id', type=int, required=True, help="Invalid user_id, should be int")
            parser.add_argument('start_date', type=str, required=True, help="Invalid user_id, shoule be in YYYY-MM-DD")
            parser.add_argument('end_date', type=str, required=True, help="Invalid user_id, shoule be in YYYY-MM-DD")
            args = parser.parse_args()
            user_id = args['user_id']
            start_date = args['start_date']
            end_date = args['end_date']
            # Check if user id is existed
            sql = "SELECT id FROM production.user WHERE id = %d" % user_id
            status, err, ret = self.db_session.query(sql)
            if not ret:
                return {"status": -1, "msg": "User id does not exist"}
            # Get Meals from user id
            # todo Take care of the limit here
            # sql = 'SELECT * FROM production.meal ' \
            #       'WHERE date >= "%s" AND date <= "%s" ' \
            #       'AND user_id = %d LIMIT 20' % (start_date, end_date, user_id)
            sql = 'SELECT m.*, i.amount_g, n.* FROM production.meal AS m ' \
                  'JOIN production.ingredient AS i ON m.id = i.meal_id ' \
                  'JOIN production.nutrition AS n ON i.nutrition_id = n.id ' \
                  'WHERE user_id = %d AND date >= "%s" AND date <= "%s"' % (user_id, start_date, end_date)
            status, err, ret = self.db_session.query(sql)
            # Convert date time to string
            if ret:
                for record in ret:
                    if 'date' in record:
                        record['date'] = str(ret[0]['date']).split(" ")[0]
                if status == 0:
                    return {"status": 0, "msg": ret}
                else:
                    return {"status": status, "msg": "Something went wrong"}
            else:
                return {"status": status, "msg": "Something went wrong"}
        finally:
            self.db_session.close()

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
            if json_data and len(
                    json_data) >= 3 and "user_id" in json_data and "name" in json_data and "ingredient" in json_data:
                # todo parse ingredient data to subtract from grocery
                # Insert Data to meal
                user_id = json_data['user_id']
                name = json_data['name']
                ingredient = json_data['ingredient']
                # sql = 'INSERT INTO production.meal (user_id, name, image_url) VALUES ("%d", "%s", "%s")' \
                #       % (user_id, name, grocery)
                sql = 'INSERT INTO production.meal (user_id, name, image_url) VALUES ("%d", "%s", "%s")' \
                      % (user_id, name, None)
                status, err, ret = self.db_session.query(sql)
                # Get the last insert ID
                sql = "SELECT last_insert_id()"
                status, err, ret = self.db_session.query(sql)
                last_id = ret[0]['last_insert_id()']
                # Insert Data to Ingredient
                for record in ingredient:
                    if 'nutrition_id' in record and 'amount_g' in record:
                        nutrition_id = record['nutrition_id']
                        amount_g = record['amount_g']
                        sql = 'INSERT INTO production.ingredient (meal_id, nutrition_id, amount_g, date) ' \
                              'VALUES (%d, %d, %f, null)' % (last_id, nutrition_id, amount_g)
                        status, err, ret = self.db_session.query(sql)
                    else:
                        return {"status": -1, "msg": "Failed to parse ingredient"}
                # Fetch the inserted data
                sql = 'SELECT * FROM production.meal WHERE id = %d LIMIT 1' % last_id
                status, err, ret = self.db_session.query(sql)
                # Convert date time to string
                if ret:
                    for record in ret:
                        if 'date' in record:
                            record['date'] = str(ret[0]['date']).split(" ")[0]
                    if status == 0:
                        return {"status": status, "msg": ret}
                    else:
                        return {"status": status, "msg": "Some thing went wrong"}
                else:
                    return {"status": status, "msg": "Some thing went wrong"}
            else:
                return {"status": -1, "msg": "invalid input"}
        finally:
            self.db_session.close()
