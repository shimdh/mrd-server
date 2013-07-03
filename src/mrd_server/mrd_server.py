# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from util import serverconfig

import view.user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# class User(db.Model):
# 	"""docstring for User"""
# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String(80), unique=True)
# 	email = db.Column(db.String(120), unique=True)

# 	def __init__(self, username, email):
# 		self.username = username
# 		self.email = email

# 	def __repr__(self):
# 		return '<User %r>' % self.username
		
@app.route('/')
def index():
	return 'Index Page'


app.add_url_rule(
    '/register', 'register', view.user.register)


if __name__ == '__main__':
	app.debug = True
	app.run(host=serverconfig.HOST, port=serverconfig.PORT)