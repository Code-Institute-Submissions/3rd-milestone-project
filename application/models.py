import flask
from datetime import datetime
from application import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# ------ RECIPE MODEL ------ #
class Recipe(db.DynamicDocument):
    title                   = db.StringField(max_length = 50)
    description             = db.StringField(max_length = 50)
    author_id               = db.ReferenceField('User')
    author                  = db.StringField(max_length = 50)


# User loader function to load a user given an id
@login_manager.user_loader
def load_user(id):
    return User.objects(pk = id).first()

# ------ USER MODEL ------ #
class User(db.Document, UserMixin):
    username                = db.StringField(min_length = 5, max_length=15)
    email                   = db.StringField(max_length = 50)
    first_name              = db.StringField(max_length = 50)
    last_name               = db.StringField(max_length = 50)
    password                = db.StringField(min_length = 8)
    gdpr_check              = db.BooleanField(default = False)
    date_time_gdpr_check    = db.DateTimeField(default = datetime.now)

    @property
    def author(self):
        return author.objects(user = self).get()

    # Hash password to store password secure in DB
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Unhash password to check against password filled in form
    def get_password(self, password):
        return check_password_hash(self.password, password)  
