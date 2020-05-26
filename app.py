from flask import Flask, render_template, url_for, redirect, flash
from pymongo import MongoClient
from forms import LoginForm, RegistrationForm

# instantiated flask application
app = Flask(__name__)

app.config['SECRET_KEY'] = '86f41a39c3a243fd22d96228eaeb23a60df36e76'

# local MongoDB
client = MongoClient('localhost', 27017)
db = client.recipe
collection = db.recipe

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

if __name__ == "__main__":
    app.run(debug=True)