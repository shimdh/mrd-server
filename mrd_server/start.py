# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from server.util import serverconfig
import server

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

server.db = db

from server.model import user
	
@app.route('/')
def index():
	return 'Index Page'


if __name__ == '__main__':
	app.debug = True
	app.run(host=serverconfig.HOST, port=serverconfig.PORT)