from flask import render_template, url_for, redirect, flash
from recipeapp import app, collection
from recipeapp.forms import LoginForm, RegistrationForm

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('index.html')


@app.route("/recipes")
def recipes():
    return render_template('recipes.html', title = 'All recipes', recipe_list = collection.find())

@app.route("/account")
def account():
    return render_template('account.html', title = 'User account')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'user@bbq.com' and form.password.data == 'password':
            flash('You are succesfully logged in!', 'success')
            return redirect(url_for('account'))
        else:
            flash('Login failed. Please make sure you used the correct username (= e-mail) and password!', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Welcome, we\'re glad to have you here {form.first_name.data}!', 'success')
        return redirect(url_for('account'))
    return render_template('register.html', title='Register', form=form)