from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DecimalField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from flask_wtf.file import FileField, FileRequired, FileAllowed
from application.models import User, Recipe

category_choices            = [("Meat", "Meat"), ("Seafood","Seafood"), ("Vegetarian","Vegetarian")]

# ------ LOGIN FORM ------ #
class LoginForm(FlaskForm):
    email                   = StringField('E-mail', validators=[DataRequired(message="Please enter your e-mail.")])
    password                = PasswordField('Password', validators=[DataRequired(message="Please enter your password.")])
    remember                = BooleanField('Keep me signed in')
    submit                  = SubmitField('Sign in')

# ------ REGISTRATION FORM ------ #
class RegistrationForm(FlaskForm):
    username                = StringField('Username', validators=[DataRequired(message="Please enter the username of your choice."), Length(min=5, max=15, message="Your username should be between 5 and 15 characters long.")])
    first_name              = StringField('First name', validators=[DataRequired(message="Please enter your firstname."), Length(max=50, message="Please keep your first name realistic (max 50 characters)!")])
    last_name               = StringField('Last name', validators=[DataRequired(message="Please enter your lastname."), Length(max=50, message="Please keep your last name realistic (max 50 characters)!")])
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
    title                   = StringField('Title', validators=[DataRequired(message="Please enter a title for your recipe."), Length(max=50, message="Please keep your title short (max 50 characters)!")])
    description             = TextAreaField('Description', validators=[DataRequired(message="Please enter a description for your recipe."), Length(min=50, message="Your awesome recipe deserves more text!")])
    category_name           = SelectField('Category', choices=category_choices)
    ingredients             = TextAreaField('Ingredients', validators=[DataRequired(message="Please enter ingredients for your recipe.")])
    directions              = TextAreaField('Directions', validators=[DataRequired(message="Please enter directions for your recipe.")])
    preparation_time        = IntegerField('Preparation time in minutes', validators=[DataRequired(message="Please enter the preparation time for your recipe.")])
    cooking_time            = IntegerField('Cooking time in minutes', validators=[DataRequired(message="Please enter the cooking time for your recipe.")])
    calories                = DecimalField('Calories', validators=[DataRequired(message="Please enter the calories for your recipe.")])
    protein                 = DecimalField('Protein (g)', validators=[DataRequired(message="Please enter the protein for your recipe.")])
    carbohydrates           = DecimalField('Carbohydrates (g)', validators=[DataRequired(message="Please enter the carbohydrates for your recipe.")])
    cholesterol             = DecimalField('Cholesterol (mg)', validators=[DataRequired(message="Please enter the cholesterol for your recipe.")])  
    recipe_image            = FileField('Upload recipe image', validators=[FileRequired(), FileAllowed(['jpg','jpeg', 'png', 'gif'], 'Images only please!')])
    submit                  = SubmitField('Submit')


class searchForm(FlaskForm):
    search_text             = StringField('Text search')
    category_name           = SelectField('Category', choices=[("", "---")] + category_choices)
    max_total_time          = IntegerField('Max. cooking time (minutes)', validators=[Optional()])       
    submit                  = SubmitField('Search')