from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=False)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/nisz/flask/wtfforms/wtfforms/site.db'
db = SQLAlchemy(app)

from wtfforms import routes
