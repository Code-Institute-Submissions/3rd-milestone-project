from flask import render_template, url_for, redirect, flash, request
from application import app, db
from application.forms import LoginForm, RegistrationForm
from application.models import Recipe, User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('index.html')

# ------ GET ALL RECIPES ------ #
@app.route("/recipes")
def recipes():
    return render_template('recipes.html', title = 'All recipes', recipe_list = Recipe.objects.all())

# ------ USER ACCOUNT ------ #
@app.route("/account")
# Login is required for account page
@login_required
def account():
    return render_template('account.html', title = 'User account')

# ------ LOGIN ------ #
@app.route("/login", methods=['GET', 'POST'])
def login():
    # Check if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = LoginForm()
    # Validate form
    if form.validate_on_submit():
        email         = form.email.data
        password      = form.password.data   
        remember      = form.remember.data
        user          = User.objects(email = email).first()     
        
        # Check if user exist and verify password against DB
        if user and user.get_password(password):
            # Login user
            login_user(user, remember = remember)
            flash('You are succesfully logged in!', 'success')
            # Go to page user intented to visit before logging in
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('account'))
        else:
            flash('Login failed. Please make sure you used the correct username (= e-mail) and password!', 'danger')
    # Render html, giving its title and passing in the form
    return render_template('login.html', title='Login', form=form)

# ------ LOGOUT ------ #
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

# ------ USER REGISTRATION ------ #
@app.route("/register", methods=['GET','POST'])
def register():
    # Check if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = RegistrationForm()
    # Validate form
    if form.validate_on_submit():
        username    = form.username.data
        email       = form.email.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data
        password    = form.password.data
        gdpr_check  = form.gdpr_check.data

        # Create new instance of user
        user = User(username = username, email = email, first_name = first_name, last_name = last_name, gdpr_check = gdpr_check)
        # Hash password
        user.set_password(password)
        # Insert record to the DB
        user.save()
        flash(f'Welcome, we\'re glad to have you here {form.first_name.data}! Please login with your e-mail and password.', 'success')
        return redirect("/login")
    # Render html, giving its title and passing in the form
    return render_template("register.html", title="Register", form=form)