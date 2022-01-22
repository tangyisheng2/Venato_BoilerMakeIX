#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :__init__.py
# @Time      :1/21/22
# @Author    :Eason Tang
from flask import Blueprint
from flask_restful import Api

from .meal import Meal

meal_bp = Blueprint('meal', __name__)
api = Api(meal_bp)
api.add_resource(Meal, '/meal')
