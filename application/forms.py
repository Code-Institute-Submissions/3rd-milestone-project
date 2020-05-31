from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from application.models import User

class LoginForm(FlaskForm):
    email                   = StringField('E-mail', validators=[DataRequired(), Email()])
    password                = PasswordField('Password', validators=[DataRequired()])
    remember                = BooleanField('Keep me signed in')
    submit                  = SubmitField('Sign in')

class RegistrationForm(FlaskForm):
    username                = StringField('Username', validators=[DataRequired(), Length(min=5, max=15)])
    first_name              = StringField('First name', validators=[DataRequired()])
    last_name               = StringField('Last name', validators=[DataRequired()])
    email                   = StringField('E-mail', validators=[DataRequired(), Email()])
    password                = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    #confirm_password       = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    gdpr_check              = BooleanField('Confirm you\'ve read our terms and conditions', validators=[DataRequired()])
    submit                  = SubmitField('Register')



