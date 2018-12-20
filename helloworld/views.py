#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 22:27
# @Author  : raojingpeng
# @File    : views.py

from flask import flash, redirect, url_for, render_template
from helloworld import app, db
from helloworld.forms import HelloWorld
from helloworld.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloWorld()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
