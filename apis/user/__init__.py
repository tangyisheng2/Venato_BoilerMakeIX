#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :__init__.py
# @Time      :1/21/22
# @Author    :Eason Tang
from flask import Blueprint
from flask_restful import Api

from .user import SignUp, LogIn
from .comsumption import Comsumption
from .statics import Statics

user_bp = Blueprint('user', __name__)
api = Api(user_bp)
api.add_resource(SignUp, '/user/signup')
api.add_resource(LogIn, '/user/login')
api.add_resource(Comsumption, "/user/consumption")
api.add_resource(Statics, "/user/statics")
