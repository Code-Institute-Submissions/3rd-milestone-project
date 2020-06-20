import flask
from datetime import datetime
from application import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from mongoengine import *

# User loader function to load a user given an id
@login_manager.user_loader
def load_user(id):
    return User.objects(pk = id).first()

# ------ RECIPE MODEL ------ #
class Recipe(db.Document):
    recipe_id               = db.IntField()
    title                   = db.StringField(max_length = 50)    
    description             = db.StringField(max_length = 50)
    category_name           = db.StringField(max_length = 50)
    ingredients             = db.StringField(max_length = 50)
    directions              = db.StringField(max_length = 50)
    preparation_time        = db.IntField()
    cooking_time            = db.IntField()
    calories                = db.DecimalField()
    protein                 = db.DecimalField()
    carbohydrates           = db.DecimalField()
    cholesterol             = db.DecimalField()     
    author_id               = db.ReferenceField('User')
    author                  = db.StringField(max_length = 50)
    recipe_image            = db.ImageField()
    recipe_image_name       = db.StringField(max_length = 150)

# ------ USER MODEL ------ #
class User(db.Document, UserMixin):
    username                = db.StringField(min_length = 5, max_length=15)
    email                   = db.StringField(max_length = 50)
    first_name              = db.StringField(max_length = 50)
    last_name               = db.StringField(max_length = 50)
    password                = db.StringField(min_length = 8)
    gdpr_check              = db.BooleanField(default = False)
    date_time_gdpr_check    = db.DateTimeField(default = datetime.now)

    # Hash password to store password secure in DB
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Unhash password to check against password filled in form
    def get_password(self, password):
        return check_password_hash(self.password, password)