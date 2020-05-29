from flask import Flask
from application.instance.config import Config
from flask_mongoengine import MongoEngine

# instantiated flask application
app = Flask(__name__)

app.config.from_object(Config)

# local MongoDB
db = MongoEngine()
db.init_app(app)

from application import views