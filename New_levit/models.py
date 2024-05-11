from New_levit import db
from flask_login import UserMixin,current_user,LoginManager,login_user,logout_user
from datetime import datetime
from New_levit import login_manager
from flask import redirect, url_for
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('loginpage'))
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(255))
    second_name=db.Column(db.String(255))
    sur_name=db.Column(db.String(255))
    email=db.Column(db.String(255), unique=True )
    password=db.Column(db.String(255))
    image_blog=db.Column(db.String(255),default='default.jpg')
    def __repr__(self):
        return f"{self.first_name}:{self.second_name}:{self.sur_name}:{self.email}:{self.password}"

class post(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    subtitle=db.Column(db.String(255))
    content=db.Column(db.Text)
    author=db.Column(db.String(255))
    date_posted=db.Column(db.DateTime,default=datetime.utcnow)
    image_blog=db.Column(db.String(255),default='default.jpg')
    slug=db.Column(db.String(255), unique=True )
    
    def __repr__(self):
        return f"{self.title}:{self.subtitle}:{self.content}:{self.author}:{self.date_posted.strftime('%d/%m/%Y, %M:%M:%S')}:{self.image_blog}:{self.slug}"

class products(db.Model,UserMixin):
   id=db.Column(db.Integer,primary_key=True)
   product_name=db.Column(db.String(255))
   description=db.Column(db.String(255))
   category=db.Column(db.String(255))
   price=db.Column(db.Float)
   discount=db.Column(db.Float)
   product_image=db.Column(db.String(255),default='default.jpg')
   Model_number=db.Column(db.String(255), unique=True )


   def __repr__(self):
        return f"{self.product_name}:{self.description}:{self.category}:{self.price}:{self.discount}:{self.product_image}:{self.Model_number}"
