
import os

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_ckeditor import CKEditor




# use app.app_context().push() when creating database

app=Flask(__name__)

extension=['.jpg','jpeg','png']
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/levitproject'
app.config['SECRET_KEY']='levitsecretkey'
app.config['UPLOADED_PHOTOS_DEST']='New_levit\static\post_images'


bcrypt=Bcrypt(app)
db=SQLAlchemy(app)
ckeditor=CKEditor(app)
login_manager=LoginManager(app)
from New_levit import routes

