# -*- coding: utf-8 -*-

from ..mrd_server.mrd_server import db
import datetime


class User(db.Model):
    """docstring for User"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), unique=True)
    gender = db.Column(db.String(1), default='M')
    character = db.Column(db.Text())
    slots = db.Column(db.Text())
    clothes = db.Column(db.Text())
    friendship_point = db.Column(db.Integer, default=0)
    inventories = db.Column(db.Text())
    cash = db.Column(db.Integer, default=0)
    session_id = db.Column(db.String(100))
    session_date = db.Column(db.DateTime())
    registered_date = db.Column(db.DateTime(), default=datetime.datetime.now())
    login_date = db.Column(db.DateTime())

    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password

    def __repr__(self):
        return '<User %s>' % (self.name)
    