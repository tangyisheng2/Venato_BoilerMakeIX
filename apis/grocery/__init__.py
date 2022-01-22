#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :__init__.py
# @Time      :1/21/22
# @Author    :Eason Tang
from flask import Blueprint
from flask_restful import Api

from .grocery import Grocery

grocery_bp = Blueprint('grocery', __name__)
api = Api(grocery_bp)
api.add_resource(Grocery, '/grocery')
