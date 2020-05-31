import flask
from datetime import datetime
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class Recipe(db.Document):
    title                   = db.StringField(max_length=50)
    description             = db.StringField(max_length=50)
    user                    = db.StringField(max_length=50)

class User(db.Document):
    username                = db.StringField(min_length = 5, max_length=15)
    email                   = db.StringField(max_length=50)
    first_name              = db.StringField(max_length=50)
    last_name               = db.StringField(max_length=50)
    password                = db.StringField(min_length=8)
    gdpr_check              = db.BooleanField(default = False)
    date_time_gdpr_check    = db.DateTimeField(default = datetime.now)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)  
