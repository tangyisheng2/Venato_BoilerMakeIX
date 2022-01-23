#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :grocery.py
# @Time      :1/21/22
# @Author    :Eason Tang
from flask import request
from flask_restful import Resource, reqparse
import db


class Grocery(Resource):
    def __init__(self):
        self.db_session = db.DB()

    def get(self):
        """
        This function takes user id and return all groceries the user have
        :return: Grocery.id[]
        """
        self.db_session.init_connection()
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('user_id', type=int, required=False, help="Invalid user_id")
            args = parser.parse_args()
            user_id = args['user_id']
            # Check if user id is existed
            sql = "SELECT id FROM production.user WHERE id = %d" % user_id
            status, err, ret = self.db_session.query(sql)
            if not ret:
                return {"status": -1, "msg": "User id does not exist"}
            # Get Grocery based on user id
            sql = 'SELECT g.*, n.name FROM production.grocery AS g ' \
                  'JOIN production.nutrition AS n ON g.nutrition_id = n.id ' \
                  'WHERE user_id = %d' % user_id
            status, err, ret = self.db_session.query(sql)
            if status == 0:
                if ret:
                    return {"status": 0, "msg": ret}
                else:
                    return {"status": -1, "msg": "The server returns nothing"}
            else:
                return {"status": -1, "msg": "Some error happened"}
        # else:
        # return {"status": -1, "msg": "UserID is not valid"}

        finally:
            self.db_session.close()

    def post(self):
        """
        This function Add groceries to the database
        :return: Grocery.id[]
        """
        self.db_session.init_connection()
        try:
            json_data = request.get_json()  # Where it takes json data
            # todo Now we put a random nutrition id change it back later
            ans = []
            if json_data['userid'] and json_data['groceries']:
                for grocery in json_data['groceries']:
                    if len(grocery) == 2 and grocery["nutrition_id"] and grocery["amount_g"]:
                        # Check if the ID  exist
                        sql = 'SELECT id, amount_g ' \
                              'FROM production.grocery ' \
                              'WHERE user_id = %d AND nutrition_id = %d ' \
                              'LIMIT 1' % (json_data['userid'], grocery["nutrition_id"])
                        status, err, ret = self.db_session.query(sql)
                        if ret:
                            id = ret[0]['id']
                            original_amount_g = ret[0]['amount_g']
                            new_amount_g = original_amount_g + grocery["amount_g"]
                            sql = 'UPDATE production.grocery SET amount_g = %f WHERE id = %d' % (new_amount_g, id)
                            status, err, ret = self.db_session.query(sql)
                            last_id = id
                        else:
                            # Add Grocery
                            sql = "INSERT INTO production.grocery (user_id, nutrition_id, amount_g) VALUES (%d, %d, %f)" % \
                                  (json_data['userid'], grocery['nutrition_id'], grocery['amount_g'])
                            self.db_session.query(sql)
                            # Get the last insert ID
                            sql = "SELECT last_insert_id()"
                            status, err, ret = self.db_session.query(sql)
                            last_id = ret[0]['last_insert_id()']
                        # Fetch data based on that id
                        sql = "SELECT * FROM production.grocery WHERE id = %d LIMIT 1" % last_id
                        status, err, ret = self.db_session.query(sql)
                        ans.append({
                            "grocery_id": ret[0]['id'],
                            "nutrition_id": ret[0]['nutrition_id'],
                            "amount_g": ret[0]['amount_g']
                        })
                    else:
                        return {"status": -1, "msg": "Not a valid grocery"}
                return {"status": 0, "msg": ans}
            else:
                return {"status": -1, "msg": "Not a valid userid or grocery"}
        finally:
            self.db_session.close()


class Search(Resource):
    def __init__(self):
        self.db_session = db.DB()

    def post(self):
        """
        This function takes user input and searches & return all nutrition
        :return: Grocery.id[]
        """
        self.db_session.init_connection()
        try:
            json_data = request.get_json()
            if len(json_data) >= 1 and "keyword" in json_data:
                reg_expression = "|".join(json_data['keyword'])
                # todo Remove the Limit 20
                sql = "SELECT id, name, category FROM production.nutrition WHERE name REGEXP '%s' LIMIT 20" % reg_expression
                status, err, ret = self.db_session.query(sql)
                return {"status": 0, "msg": ret}
            else:
                return {"status": -1, "msg": "Search Keyword is not valid"}
        finally:
            self.db_session.close()
