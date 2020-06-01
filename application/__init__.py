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
# Redirect user who is not logged in to login page when user visits a page for which a login is required 
login_manager.login_view = 'login'
# Custom message when user visits page for which a login in required wjen user is not logged in
login_manager.login_message = 'Please sign in. Afterwards you will be redirected to the requested page.'
# Bootstrap color for login messaga
login_manager.login_message_category = "warning"

from application import views