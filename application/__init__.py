from flask import Flask
from application.instance.config import Config
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

# Instantiated flask application
app = Flask(__name__)

app.config.from_object(Config)

# Local MongoDB
db = MongoEngine()
db.init_app(app)

# Login manager for user authentication and sessions
login_manager = LoginManager(app)

from application import views