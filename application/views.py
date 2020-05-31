from flask import render_template, url_for, redirect, flash
from application import app, db
from application.forms import LoginForm, RegistrationForm
from application.models import Recipe, User

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('index.html')


@app.route("/recipes")
def recipes():
    return render_template('recipes.html', title = 'All recipes', recipe_list = Recipe.objects.all())

@app.route("/account")
def account():
    return render_template('account.html', title = 'User account')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email               = form.email.data
        password            = form.password.data   
        user                = User.objects(email = email).first()     
        
        if user and user.get_password(password):
            flash('You are succesfully logged in!', 'success')
            return redirect(url_for('account'))
        else:
            flash('Login failed. Please make sure you used the correct username (= e-mail) and password!', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        username    = form.username.data
        email       = form.email.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data
        password    = form.password.data
        gdpr_check  = form.gdpr_check.data

        user = User(email = email, first_name = first_name, last_name = last_name, gdpr_check = gdpr_check)
        user.set_password(password)
        user.save()
        flash(f'Welcome, we\'re glad to have you here {form.first_name.data}! Please login with your e-mail and password.', 'success')
        return redirect("/login")
    return render_template("register.html", title="Register", form=form)