#!/usr/bin/env python
import os


DEBUG = True
SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWD = 'fantuan'
HOST = '193.193.193.2'
PORT = '3306'
DATABASE = 'myblog'


SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,
                                              DRIVER, USERNAME, PASSWD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False