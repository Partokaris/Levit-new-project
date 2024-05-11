from New_levit import app
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed, FileField 
from flask_admin.actions import action,request, redirect
from wtforms import SubmitField,StringField, TextAreaField,PasswordField,IntegerField,SelectField,DecimalField
from wtforms.validators import DataRequired,Email,Length,EqualTo,email
from datetime import datetime
from flask_login import UserMixin,current_user,LoginManager,login_user,logout_user

from flask_admin.form import BaseForm
from flask_admin.form.upload import FileUploadField, secure_filename
from flask_admin.contrib.sqla import ModelView
from New_levit.models import post,products,User
from flask_admin.contrib.fileadmin import FileAdmin
from flask_ckeditor import CKEditorField

from New_levit import db
from flask_uploads import UploadSet, IMAGES,configure_uploads

photos=UploadSet('photos',IMAGES)
configure_uploads(app,photos)


class LoginForm(FlaskForm):
    email=StringField(label="Email", validators=[DataRequired(),Length(min=6),Email()])
    password=PasswordField(label="Password", validators=[DataRequired(),Length(min=6)])
    submit=SubmitField(label="Login")


class RegistrationForm(FlaskForm):
    first_name=StringField(label="First Name", validators=[DataRequired()])
    second_name=StringField(label="Second Name", validators=[DataRequired()])
    sur_name=StringField(label="Sur Name", validators=[DataRequired()])
    email=StringField(label="Email", validators=[DataRequired(),Email()])
    password=PasswordField(label="Password", validators=[DataRequired(),Length(min=6)])
    confirm_password=PasswordField(label="Confirm Password", validators=[DataRequired(),EqualTo('password')] )
    submit=SubmitField(label="Register")

class blogpost(FlaskForm):
    title=StringField(label="title",validators=[DataRequired()])
    subtitle=StringField(label="subtitle",validators=[DataRequired()])
    # content=TextAreaField(label="content",validators=[DataRequired()])
    content = CKEditorField('content',validators=[DataRequired()])
    author=StringField(label="author",validators=[DataRequired()])
    date_posted=StringField(label="Date",validators=[DataRequired()])
    slug=StringField(label="slug",validators=[DataRequired()] )
    picture=FileField(label="Upload", validators=[FileAllowed(photos,'only images allowed')])

    submit=SubmitField(label="upload")

class add_product(FlaskForm):
    product_name=StringField(label="product_name",validators=[DataRequired()],render_kw={"placeholder": " Product Name "})
    description=TextAreaField(label="Description",validators=[DataRequired()],render_kw={"placeholder": " Description "})
    category=SelectField(u"Product Category",choices=[('Laptop','Laptops'),('Printers','Printers'),('Antivirus','Antivirus')], validators=[DataRequired()],render_kw={"placeholder": "Category"})
    price=DecimalField(label="Price",validators=[DataRequired()],render_kw={"placeholder": " Price Ksh "})
    discount=IntegerField(label="Discount",validators=[DataRequired()],render_kw={"placeholder": " Discount "})
    product_image=FileField(label="Upload",validators=[FileAllowed(photos,'only images allowed')])
    Model_number=StringField(label="Model_number",validators=[DataRequired()],render_kw={"placeholder": " Model Number "})

    submit=SubmitField(label="upload")
# class MyForm(BaseForm):
#     image=FileUploadField('file', namegen=prefix_name)


    
# admin.add_view(ModelView(post, db.session))
# admin.add_view(FileAdmin(path,'/static/', name='static files'))
