import flask
from application import db
 

class Recipe(db.Document):
    title = db.StringField( max_length=50 )
    description = db.StringField( max_length=50 )
    user = db.StringField( max_length=50 )
