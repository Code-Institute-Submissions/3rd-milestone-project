import os
from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

# Instantiated flask application
app = Flask(__name__)

# Secret key in environment variables
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') 

# Setting up DB connection to MongoDB Atlas via environment variables in Heroku
MONGODB_HOST = os.environ.get('MONGODB_HOST') 

app.config['MONGODB_SETTINGS'] = {
    'db': 'db_recipe',
    'host': MONGODB_HOST 
}

# Initiating MongoEngine
db = MongoEngine()
db.init_app(app)

# Login manager for user authentication and sessions
login_manager = LoginManager(app)
# Redirect user who is not logged in to login page when user visits a page for which a login is required 
login_manager.login_view = 'login'
# Custom message when user visits page for which a login in required when user is not logged in
login_manager.login_message = 'Please sign in. Afterwards you will be redirected to the requested page.'
# Bootstrap color for login messaga
login_manager.login_message_category = "warning"

from application import views