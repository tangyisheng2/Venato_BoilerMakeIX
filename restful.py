#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :restful.py
# @Time      :1/21/22
# @Author    :Eason Tang
import os
import sys

# SSL
# from OpenSSL import SSL
from flask import Flask
from flask_restful import Resource, Api, reqparse

absPath = os.path.abspath(__file__)  # 返回代码段所在的位置，肯定是在某个.py文件中
temPath = os.path.dirname(absPath)  # 往上返回一级目录，得到文件所在的路径
temPath = os.path.dirname(temPath)  # 在往上返回一级，得到文件夹所在的路径
sys.path.append(temPath)  # 添加该路径到搜索路径中

# Import Blueprint
from apis.user import user_bp
from apis.grocery import grocery_bp
from apis.meal import meal_bp


# context = SSL.Context(SSL.TLSv1_2_METHOD)


# context.use_privatekey_file('cert/3118405_agv.tangyisheng2.com.key')
# context.use_certificate_file('cert/3118405_agv.tangyisheng2.com.crt')
# context.load_client_ca('cert/3118405_agv.tangyisheng2.com.crt',
#                        )


class Debug(Resource):
    def get(self):
        """
        :return: Self test the program
        """
        return {'status': '0'}


app = Flask(__name__)
api = Api(app)
# Add Resources
api.add_resource(Debug, '/')

# Add Blueprint
app.register_blueprint(user_bp)
app.register_blueprint(grocery_bp)
app.register_blueprint(meal_bp)

# Server config starts Here


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5001,
            debug=True)
