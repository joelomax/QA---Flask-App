from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import os

app = Flask(__name__)

bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes

