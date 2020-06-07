from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User, Recipe

# ------ LOGIN FORM ------ #
class LoginForm(FlaskForm):
    email                   = StringField('E-mail', validators=[DataRequired(message="Please enter your e-mail.")])
    password                = PasswordField('Password', validators=[DataRequired(message="Please enter your password.")])
    remember                = BooleanField('Keep me signed in')
    submit                  = SubmitField('Sign in')

# ------ REGISTRATION FORM ------ #
class RegistrationForm(FlaskForm):
    username                = StringField('Username', validators=[DataRequired(message="Please enter the username of your choice."), Length(min=5, max=15, message="Your username should be between 5 and 15 characters long.")])
    first_name              = StringField('First name', validators=[DataRequired(message="Please enter your firstname.")])
    last_name               = StringField('Last name', validators=[DataRequired(message="Please enter your lastname.")])
    email                   = StringField('E-mail', validators=[DataRequired(message="Please enter your e-mail."), Email(message="Please enter a valid e-mail.")])
    password                = PasswordField('Password', validators=[DataRequired(message="Please enter your password."), Length(min=8, message="Your password should be at least 8 characters long.")])
    confirm_password        = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password', message="Password and confirm password fields should match. Please enter the password of your choice.")])
    gdpr_check              = BooleanField('Confirm you\'ve read our terms and conditions', validators=[DataRequired(message="Please confirm that you\'ve read our terms and conditions.")])
    submit                  = SubmitField('Register')

    # Validation on username: username should be unique.
    def validate_username(self, username):
        user = User.objects(username = username.data).first()
        if user:
            raise ValidationError("This username is unfortunately taken. Please register with another username.")
    
    # Validation on e-mail: e-mail should be unique.
    def validate_email(self, email):
        user = User.objects(email = email.data).first()
        if user:
            raise ValidationError("You already registered with this email. Please login with this email.")

# ------ ADD RECIPE FORM ------ #
class AddRecipeForm(FlaskForm):
    title                   = StringField('Title', validators=[DataRequired(message="Please enter a title for your recipe.")])
    description             = StringField('Description', validators=[DataRequired(message="Please enter a description for your recipe.")])
    submit                  = SubmitField('Submit')



