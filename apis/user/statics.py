#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :statics.py
# @Time      :1/22/22
# @Author    :Eason Tang
from flask import request
from flask_restful import Resource
import db


class Statics(Resource):
    def __init__(self):
        self.db_session = db.DB()

    def get(self):
        """
        This function returns the summary of the nutrition data
        :return:
        """
        self.db_session.init_connection()
        try:
            # json_data = request.get_json()
            # if len(json_data) == 1 and "user_id" in json_data:
            #     user_id = json_data['user_id']
            # # Check if user id is existed
            # sql = "SELECT id FROM production.user WHERE id = %d" % user_id
            # status, err, ret = self.db_session.query(sql)
            # if not ret:
            #     return {"status": -1, "msg": "User id does not exist"}
            # Get the statics
            sql = "SELECT production.grocery.id, " \
                  "SUM(production.grocery.amount_g) AS 'amount_g', production.nutrition.category as category " \
                  "FROM production.grocery " \
                  "JOIN production.nutrition " \
                  "ON grocery.nutrition_id = nutrition.id " \
                  "GROUP BY category"
            status, err, ret = self.db_session.query(sql)
            return {"status": 0, "msg": ret}
        finally:
            self.db_session.close()
