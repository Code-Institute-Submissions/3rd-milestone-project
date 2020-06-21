from flask import render_template, url_for, redirect, flash, request, abort, send_file
from application import app, db
from application.forms import LoginForm, RegistrationForm, AddRecipeForm
from application.models import Recipe, User, RecipeID
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
import datetime
from flask_paginate import Pagination, get_page_parameter

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():

    total_meat_recipes          = Recipe.objects(category_name = "Meat").count()
    total_seafood_recipes       = Recipe.objects(category_name = "Seafood").count()
    total_vegetarian_recipes    = Recipe.objects(category_name = "Vegetarian").count()
    return render_template('index.html', total_meat_recipes = total_meat_recipes, total_seafood_recipes = total_seafood_recipes, total_vegetarian_recipes = total_vegetarian_recipes)

# ------ GET ALL RECIPES ------ #
@app.route("/recipes")
def recipes():
    # Set default page parameter to 1
    page = request.args.get(get_page_parameter(), type = int, default = 1)

    # Get recipes and order descending so that newest recipes come first
    recipes = Recipe.objects.order_by('-recipe_id')
    # Count number of recipes
    total_recipes = recipes.count()

    # Configure pagination setting
    pagination = Pagination(page = page, total = total_recipes, record_name = 'recipes', per_page = 3, css_framework = 'bootstrap4')

    # Render html, giving its title and passing in recipes
    return render_template('recipes.html', title = 'All recipes', recipes = recipes, pagination = pagination, total_recipes = total_recipes)

# ------ GET ALL RECIPES BY USER ------ #
@app.route('/user/<author>')
def user_recipes(author):
    user_recipes        = Recipe.objects(author = author)
    total_user_recipes  = user_recipes.count()
    
    # Render html, giving its title and passing in the recipe object
    return render_template('user_recipes.html', title = 'test', user_recipes = user_recipes, total_user_recipes = total_user_recipes, author = author)

# ------ GET ALL MEAT RECIPES ------ #
@app.route("/meat-recipes")
def meat_recipes():
    # Get recipe and order descending so that newest recipes come first
    recipes = Recipe.objects(category_name = "Meat").order_by('-recipe_id')
    # Count number of recipes
    total_recipes = Recipe.objects(category_name = "Meat").count()
        
    # Render html, giving its title and passing in recipes
    return render_template('meat_recipes.html', title = 'All meat recipes', recipes = recipes, total_recipes = total_recipes)

# ------ GET ALL SEAFOOD RECIPES ------ #
@app.route("/seafood-recipes")
def seafood_recipes():
    # Get recipe and order descending so that newest recipes come first
    recipes = Recipe.objects(category_name = "Seafood").order_by('-recipe_id')
    # Count number of recipes
    total_recipes = Recipe.objects(category_name = "Seafood").count()
        
    # Render html, giving its title and passing in recipes
    return render_template('seafood_recipes.html', title = 'All seafood recipes', recipes = recipes, total_recipes = total_recipes)

# ------ GET ALL VEGETARIAN RECIPES ------ #
@app.route("/vegetarian-recipes")
def vegetarian_recipes():
    # Get recipe and order descending so that newest recipes come first
    recipes = Recipe.objects(category_name = "Vegetarian").order_by('-recipe_id')
    # Count number of recipes
    total_recipes = Recipe.objects(category_name = "Vegetarian").count()
        
    # Render html, giving its title and passing in recipes
    return render_template('vegetarian_recipes.html', title = 'All vegetarian recipes', recipes = recipes, total_recipes = total_recipes)

# ------ HELPER ROUTE TO SHOW IMAGES ------ #
@app.route('/images/<image_name>')
def get_image(image_name):
    image = Recipe.objects(recipe_image_name = image_name).first()
    return send_file(image.recipe_image, mimetype='image')

# ------ ADD RECIPE ------ #
@app.route("/recipe/add", methods=['GET', 'POST'])
# Login is required for add recipe page
@login_required
def add_recipe():
    form    = AddRecipeForm()
    # Access the underlying object User that is proxied for making the ReferenceField author work
    author_id  = current_user._get_current_object()
    author     = current_user.username 
   
    # Check if a request is both a POST request and a valid request
    if form.validate_on_submit():
        # Count recipe ID's in separate collection so that numbers stay unique
        recipe_id           = RecipeID.objects.count() + 1
        title               = form.title.data
        description         = form.description.data
        category_name       = form.category_name.data
        ingredients         = form.ingredients.data
        directions          = form.directions.data    
        preparation_time    = form.preparation_time.data 
        cooking_time        = form.cooking_time.data        
        calories            = form.calories.data              
        protein             = form.protein.data               
        carbohydrates       = form.carbohydrates.data           
        cholesterol         = form.cholesterol.data               

        # Check if recipe image is selected by user
        if 'recipe_image' in request.files:
            recipe_image = request.files[ 'recipe_image'] 
            # Check if image name is secure by usering Werkzeug's secure_filename function
            secure_image_name = secure_filename(recipe_image.filename)

            # Creating prefix for making image name unique
            prefix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
            recipe_image_name = "_".join([prefix, secure_image_name])  

        # Create new instance of recipe
        new_recipe_id   = RecipeID(recipe_id = recipe_id)
        new_recipe      = Recipe(recipe_id = recipe_id, title = title, description = description, category_name = category_name, ingredients = ingredients,\
                            directions = directions, preparation_time = preparation_time, cooking_time = cooking_time, calories = calories, protein = protein,\
                            carbohydrates = carbohydrates, cholesterol = cholesterol, author_id = author_id, author = author, recipe_image = recipe_image,\
                            recipe_image_name = recipe_image_name)
        # Insert record to the DB
        new_recipe_id.save()
        new_recipe.save()
        flash('Your awesome recipe has been added!', 'success')
        # Go to all account page after submitting a recipe
        return redirect(url_for('account'))
    return render_template('add_recipe.html', title = 'Add recipe', form = form)

# ------ EDIT/UPDATE SPECIFIC RECIPE ------ #
@app.route("/recipe/edit/<int:recipe_id>", methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    # Search in DB for recipe ID. If not, return 404 page
    recipe = Recipe.objects.get_or_404(recipe_id = recipe_id)
    # Check if author ID is same as OnjectId of current user. If not, return 403 Forbidden page
    if recipe.author_id != current_user._get_current_object():
        abort(403)
    form = AddRecipeForm()
    if form.validate_on_submit():
        title               = form.title.data
        description         = form.description.data
        category_name       = form.category_name.data
        ingredients         = form.ingredients.data
        directions          = form.directions.data    
        preparation_time    = form.preparation_time.data 
        cooking_time        = form.cooking_time.data        
        calories            = form.calories.data              
        protein             = form.protein.data               
        carbohydrates       = form.carbohydrates.data           
        cholesterol         = form.cholesterol.data  

        # Check if recipe image is selected by user
        if 'recipe_image' in request.files:
            recipe_image = request.files[ 'recipe_image'] 

            # Check if image name is secure by usering Werkzeug's secure_filename function
            secure_image_name = secure_filename(recipe_image.filename)

            # Creating prefix for making image name unique
            prefix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
            recipe_image_name = "_".join([prefix, secure_image_name])  

            # Adding image object and name in case an image is selected
            recipe.recipe_image         = recipe_image
            recipe.recipe_image_name    = recipe_image_name

        # MongoEngine tracks changes to documents to provide efficient saving. When document exists changes will be updated atomically. 
        # Reference: https://docs.mongoengine.org/guide/document-instances.html#saving-and-deleting-documents
        recipe.save()
        flash('Your recipe has been changed. Thank you for keeping our website up to date with your latest taste sensations ;)', 'success')
        return redirect(url_for('account'))
    # Show existing data in form through GET request    
    elif request.method == 'GET':
        form.title.data             = recipe.title
        form.description.data       = recipe.description
        form.category_name.data     = recipe.category_name
        form.ingredients.data       = recipe.ingredients
        form.directions.data        = recipe.directions
        form.preparation_time.data  = recipe.preparation_time
        form.cooking_time.data      = recipe.cooking_time
        form.calories.data          = recipe.calories
        form.protein.data           = recipe.protein       
        form.carbohydrates.data     = recipe.carbohydrates
        form.cholesterol.data       = recipe.cholesterol     
    # Render html, giving its title and passing in the form
    return render_template('add_recipe.html', title = 'Edit recipe', form = form)  

    # ------ DELETE SPECIFIC RECIPE ------ #
@app.route("/recipe/delete/<int:recipe_id>")
@login_required
def delete_recipe(recipe_id):
    # Search in DB for recipe ID. If not, return 404 page
    recipe = Recipe.objects.get_or_404(recipe_id = recipe_id)
    # Check if author ID is same as OnjectId of current user. If not, return 403 Forbidden page
    if recipe.author_id != current_user._get_current_object():
        abort(403)
    recipe.delete()
    flash('Your recipe has been deleted. We hope to see you adding a new recipe soon ;)', 'success')
    return redirect(url_for('account')) 

# ------ VIEW RECIPE BY RECIPE ID ------ #
@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe  = Recipe.objects.get_or_404(recipe_id = recipe_id)
    title   = recipe.title
    total_cooking_time = recipe.preparation_time + recipe.cooking_time
    # Render html, giving its title and passing in the recipe object
    return render_template('recipe.html', title = title, recipe = recipe, total_cooking_time = total_cooking_time)

# ------ USER ACCOUNT ------ #
@app.route("/account", methods=['GET', 'POST'])
# Login is required for account page
@login_required
def account():
    author              = current_user.username
    user_first_name     = current_user.first_name 
   
    # Make recipe list by author
    recipe_list = Recipe.objects(author = author)
     
    return render_template('account.html', title = 'User account', recipe_list = recipe_list, user_first_name = user_first_name)

# ------ LOGIN ------ #
@app.route("/login", methods=['GET', 'POST'])
def login():
    # Check if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = LoginForm()
    # Check if a request is both a POST request and a valid request
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
            flash('Login failed. Please make sure you use the correct username (= e-mail) and password!', 'danger')
    # Render html, giving its title and passing in the form
    return render_template('login.html', title = 'Login', form = form)

# ------ LOGOUT ------ #
@app.route("/logout")
def logout():
    logout_user()
    flash('You have successfully logged out.', 'success')
    return redirect(url_for('home'))

# ------ USER REGISTRATION ------ #
@app.route("/register", methods=['GET','POST'])
def register():
    # Check if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = RegistrationForm()
    # Check if a request is both a POST request and a valid request
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
    return render_template("register.html", title = "Register", form = form)