from flask import Flask
from pymongo import MongoClient

# instantiated flask application
app = Flask(__name__)

app.config.from_pyfile('instance/config.py')

# local MongoDB
client = MongoClient('localhost', 27017)
db = client.recipe
collection = db.recipe

from recipeapp import views