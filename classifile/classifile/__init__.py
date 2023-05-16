from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail, Message
import json
from .app import app



app = Flask(__name__)
mail = Mail(app)
app.config['SECRET_KEY'] = '3dce62013b890416bcb508b1210ad0a1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOADED_IMAGES_DEST'] = 'static/media_dest'
app.config['UPLOADED_FILES_ALLOW'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from classifile import routes