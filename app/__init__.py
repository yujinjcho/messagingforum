from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#import flask.ext.login as flask_login

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
#lm = flask_login.LoginManager()
#lm.init_app(app)

from app import views, models


