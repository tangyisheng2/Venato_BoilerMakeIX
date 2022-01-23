#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :comsumption.py
# @Time      :1/21/22
# @Author    :Eason Tang
from flask import request
from flask_restful import Resource, reqparse
import db


class Comsumption(Resource):
    def __init__(self):
        self.db_session = db.DB()

    def post(self):
        """
        This function takes meal id and subtract the eaten groceries in the stock
        :return: User daily consumption
        """
        self.db_session.init_connection()
        try:
            json_data = request.get_json()
            if "meal_id" in json_data and "user_id" in json_data:
                meal_id = json_data['meal_id']
                user_id = json_data['user_id']
                # Get the nutrition_id of the meal
                sql = 'SELECT * FROM production.ingredient WHERE meal_id = %d' % meal_id
                status, err, ret = self.db_session.query(sql)
                nutrition_id = [str(record['nutrition_id']) for record in ret]
                nutrition_abstract_nutrition_id = {}
                for record in ret:
                    id = record['nutrition_id']
                    subtract_amount = record['amount_g']
                    nutrition_abstract_nutrition_id[id] = subtract_amount

                # Get the grocery id based on the nutrition_id and user_id
                sql = 'SELECT * FROM production.grocery ' \
                      'WHERE nutrition_id REGEXP "%s" AND user_id = %d;' % ("|".join(nutrition_id), user_id)
                status, err, ret = self.db_session.query(sql)
                # Create a hashmap store the grocery id to be subtracted and subtract amount
                nutrition_abstract_grocery_id = {}
                for record in ret:
                    id = record['id']
                    nutrition_id = record['nutrition_id']
                    subtract_amount = nutrition_abstract_nutrition_id[nutrition_id]
                    nutrition_abstract_grocery_id[id] = subtract_amount
                # Update the grocery amount
                ans = []
                for id, subtract_amount in nutrition_abstract_grocery_id.items():
                    # Get the original amount
                    sql = 'SELECT * FROM production.grocery WHERE id = %d LIMIT 1' % id
                    status, err, ret = self.db_session.query(sql)
                    original_amount_g = ret[0]['amount_g']
                    new_amount_g = original_amount_g - subtract_amount
                    if new_amount_g < 0:  # Check if amount drops below 0
                        return {"status": -1, "msg": "Invalid amount, might be subtracted too much"}
                    sql = 'UPDATE production.grocery SET amount_g = %f WHERE id = %d LIMIT 1' % (new_amount_g, id)
                    status, err, ret = self.db_session.query(sql)
                    # Fetch the last modified
                    sql = 'SELECT * FROM production.grocery WHERE id = %d LIMIT 1' % id
                    status, err, ret = self.db_session.query(sql)
                    ans.append(ret)

                return {"status": 0, "ret": ans}

            else:
                return {"status": -1, "msg": "Invalid meal_id"}

        finally:
            self.db_session.close()

    def get(self):
        """
        This function takes user id and get the daily consumption from user database
        1. Get the user id
        2. Use meal api to get all meals
        3. Meals to join the daily entry

        :return: DailyConsumption
        """
        self.db_session.init_connection()
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('user_id', type=int, required=False, help="Invalid user_id, should be int")
            parser.add_argument('start_date', type=str, required=False, help="Invalid user_id, shoule be in YYYY-MM-DD")
            parser.add_argument('end_date', type=str, required=False, help="Invalid user_id, shoule be in YYYY-MM-DD")
            args = parser.parse_args()
            user_id = args['user_id']
            start_date = args['start_date']
            end_date = args['end_date']
            # Check if user id is existed
            sql = "SELECT id FROM production.user WHERE id = %d" % user_id
            status, err, ret = self.db_session.query(sql)
            if not ret:
                return {"status": -1, "msg": "User id does not exist"}
            # Check if user id is existed
            sql = "SELECT id FROM production.user WHERE id = %d" % user_id
            status, err, ret = self.db_session.query(sql)
            if not ret:
                return {"status": -1, "msg": "User id does not exist"}
            # Get all meals the user have eatern
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

    def subtract(self, user_id, nutrition_id, amount):
        self.db_session.init_connection()
        try:
            # Check if user id is existed
            sql = "SELECT id FROM production.user WHERE id = %d" % user_id
            status, err, ret = self.db_session.query(sql)
            if not ret:
                return {"status": -1, "msg": "User id does not exist"}
            # Get the original grocery amount
            sql = 'SELECT id, nutrition_id, amount_g ' \
                  'FROM production.grocery ' \
                  'WHERE nutrition_id = %d ' \
                  'LIMIT 1' % nutrition_id
            status, err, ret = self.db_session.query(sql)
            # Subtract
            id = ret[0]['id']
            original_amount = ret[0]['amount_g']
            sql = 'UPDATE production.grocery t SET t.amount_g = %d WHERE t.id = %d' % (original_amount - amount, id)
            status, err, ret = self.db_session.query(sql)
            # Fetch back the result
            sql = 'SELECT * FROM production.grocery WHERE id = %d LIMIT 1' % id
            status, err, ret = self.db_session.query(sql)
            return {"status": 0, "msg": ret}

        finally:
            self.db_session.close()


if __name__ == '__main__':
    test = Comsumption()
    test.subtract(1, 1108, 10)
