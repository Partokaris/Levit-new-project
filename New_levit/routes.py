from New_levit import app, db
from flask import Flask , render_template, url_for, flash,send_from_directory

import os.path as op
import os

import string
import random



import secrets
from flask_admin.form import SecureForm
from flask_admin.model.form import InlineFormAdmin
from flask_admin.actions import action

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.form import BaseForm
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed, FileField
from flask_admin.actions import action,request, redirect
from wtforms import SubmitField,StringField, TextAreaField,PasswordField,IntegerField,SelectField,DecimalField
from wtforms.validators import DataRequired,Email,Length
from datetime import datetime
from flask_admin.form.upload import FileUploadField, secure_filename
from flask_login import UserMixin,current_user,LoginManager,login_user,logout_user,login_required
from New_levit.forms import blogpost, LoginForm, add_product,photos, RegistrationForm
from New_levit.models import post,products,User
from New_levit import bcrypt


admin=Admin(app, name='LevitAdmin', template_mode='bootstrap3')
path=op.join(op.dirname(__file__),'static/post_images')
extension=['.jpg','.jpeg','.png']




def exists(file_path):
    return os.path.isfile(file_path)
    
def prefix_name(obj,file_data):
    parts=op.splitext(file_data.filename)
    return secure_filename('file-%s%s'% parts)

@app.route('/post_images/<filename>')
def get_file(filename):
    new_filename=filename +"super"
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],new_filename)


@app.route("/superuser", methods=['GET','POST'])
@login_required
def adminpage():
    form=blogpost()
    if form.validate_on_submit():
        filename = secure_filename(form.picture.data.filename)
        slug = form.slug.data
        file_ext = os.path.splitext(filename)[1]
        new_filename = f"{slug}{file_ext}"
        photos.save(form.picture.data, name=new_filename)
        file_url = url_for('get_file', filename=new_filename)
        flash(f'Your Blog has been posted successful for the title {form.title.data}',category='success')
        post.image_blog=new_filename
        blog=post(title=form.title.data,subtitle=form.subtitle.data, content=form.content.data, author=form.author.data, date_posted=form.date_posted.data,image_blog=new_filename,slug=form.slug.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('adminpage'))
    else:
        file_url=None
    # image_url=url_for('static', filename="post_images/"+ post.image_blog)
      
    return render_template("superuser.html", title="Admin Page", form=form,file_url=file_url)


@app.route("/blogging", methods=['POST','GET'])
def blogpage():
    paths=path
    posts=post.query.all()
    return render_template("blogging.html", title="Blog Page",posts=posts, paths=paths)

@app.route("/login", methods=['POST','GET'])
def loginpage():
    if current_user.is_authenticated:
        return  redirect(url_for('adminpage'))
    form=LoginForm()
    
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            flash(f'login successful',category='success')
            return redirect(url_for('adminpage'))
        else:
            flash(f'incorrect Email or password please check your details',category='danger')
            return redirect(url_for('loginpage'))
    return render_template("login.html",title="Admin Login",form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('loginpage'))

@app.route("/registration", methods=['GET','POST'])
def registration():
    """func that returns the address of the Registration page"""
    form=RegistrationForm()
    if form.validate_on_submit():
        encrypted_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(first_name=form.first_name.data, second_name=form.second_name.data, sur_name=form.sur_name.data, email=form.email.data,password=encrypted_password)
        db.session.add(user)
        db.session.commit()
        flash(f'{form.first_name.data} {form.second_name.data} is added successful',category='success')
        return redirect(url_for('loginpage'))
    return render_template("registration.html",title="Registration Page",form=form)
@app.route("/")
def Homepage():
    """func that returns the address of the home page"""
    return render_template("homepage.html",title="Home Page")

@app.route("/about")
def Aboutpage():
    """func that returns the address of the About page"""
    return render_template("about.html",title="About")


@app.route("/post1/<slug>",methods=['POST','GET'])
def post1(slug):
    posts=post.query.filter_by(slug=slug).one()
    file_url = url_for('get_file', filename=posts.image_blog)
    paths=path
    """func that returns the single post"""
    return render_template("post1.html",title="post",posts=posts,paths=paths,file_url=file_url)

@app.route("/services")
def servicespage():
    """func that returns the address of the blog page"""
    return render_template("services.html",title="Services")

@app.route("/contact")
def contactpage():
    """func that returns the address of the blog page"""
    return render_template("contact.html",title="Contact Us")

# section for services drill down
@app.route("/services/hardware-and-infrastructure")
def sercices_drill_down():
    """func that returns the address of the services drill down"""
    return render_template("service-hardware.html",title="Services")
# software solutions
@app.route("/services/software-solutions")
def software_solutions():
    """func that returns the address of the services drill down"""
    return render_template("software-solutions.html",title="Services")
# Security solutions
@app.route("/services/security-solutions")
def security_solutions():
    """func that returns the address of the services drill down"""
    return render_template("security-solutions.html",title="Services")
# Website Development
@app.route("/services/website-development")
def web_dev():
    """func that returns the address of the services drill down"""
    return render_template("website-development.html",title="Services")

@app.route("/services/graphic-design-and-digital-marketing")
def graphic_design():
    """func that returns the address of the services drill down"""
    return render_template("graphic-design.html",title="Services")

@app.route("/services/ict-consultancy")
def ict_consultancy():
    """func that returns the address of the services drill down"""
    return render_template("ict-consultancy.html",title="Services")
# @app.route("/post")
# def post():
#     """func that returns the address of the post page"""
#     return render_template("post.html", title="Post")

@app.route("/shop", methods=['GET','POST'])
def shop():
    """func that returns the address of the post page"""
    product_list = products.query.all()

    # Generate image URLs for products with valid extensions and existing files
    valid_products = []
    for product in product_list:
        for extension in ['.jpg', '.jpeg', '.png']:
            image_url = url_for('static', filename=f'post_images/{product.Model_number}{extension}')
            if exists(image_url):
                product.image_url = image_url
                valid_products.append(product)
                break  # Break out of the inner loop once a valid image is found

    return render_template("shop.html", title="Shop", products=valid_products,product_list=product_list)
@app.route("/shopcart")
def shopcart():
    """func that returns the address of the services drill down"""
    return render_template("shopcart.html",title="Shop Cart")

@app.route("/addstock", methods=['GET','POST'])
def addstock():
    """func that returns the address of the services drill down"""
    form=add_product()
    if form.validate_on_submit():
        filename = secure_filename(form.product_image.data.filename)
        model_number = form.Model_number.data
        file_ext = os.path.splitext(filename)[1]
        new_filename = f"{model_number}{file_ext}"
        photos.save(form.product_image.data, name=new_filename)
        products.product_image=new_filename
        file_url = url_for('get_file', filename=new_filename)
        flash(f'{form.product_name.data} has been stocked successful', category='success')
        stock=products(product_name=form.product_name.data,description=form.description.data, category=form.category.data, price=form.price.data, discount=form.discount.data,product_image=new_filename,Model_number=form.Model_number.data)
        products.product_image=new_filename
        db.session.add(stock)
        db.session.commit()
        return redirect(url_for('addstock'))
    else:
        file_url=None
    return render_template("addstock.html",title="Add Stock",form=form,file_url=file_url)