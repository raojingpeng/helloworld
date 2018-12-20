#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 22:28
# @Author  : raojingpeng
# @File    : __init__.py

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask('helloworld')
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


from helloworld import views, commands
