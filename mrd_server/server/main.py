# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from util import serverconfig



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

	
@app.route('/')
def index():
	return 'Index Page'


if __name__ == '__main__':
	app.debug = True
	app.run(host=serverconfig.HOST, port=serverconfig.PORT)