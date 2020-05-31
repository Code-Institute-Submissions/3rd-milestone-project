import flask
from datetime import datetime
from application import db

class Recipe(db.Document):
    title                   = db.StringField(max_length=50)
    description             = db.StringField(max_length=50)
    user                    = db.StringField(max_length=50)

class User(db.Document):
    username                = db.StringField(max_length=50)
    email                   = db.StringField(max_length=50)
    first_name              = db.StringField(max_length=50)
    last_name               = db.StringField(max_length=50)
    password                = db.StringField(max_length=50)
    gdpr_check              = db.BooleanField()
    date_time_gdpr_check    = db.DateTimeField(default=datetime.now)
