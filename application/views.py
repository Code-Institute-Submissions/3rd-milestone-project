from flask import render_template, url_for, redirect, flash, request, abort, send_file
from application import app, db
from application.forms import LoginForm, RegistrationForm, AddRecipeForm, searchForm
from application.models import Recipe, User, RecipeID
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
import datetime
from flask_paginate import Pagination, get_page_parameter
from mongoengine.queryset.visitor import Q

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def home():
    form = searchForm()

    # Set per page for pagination
    per_page = 6

    # Set default page parameter to 1 for pagination
    page = request.args.get('page', 1, type = int)

    # Get recipes and order descending so that newest recipes come first
    recipes = Recipe.objects.order_by('-recipe_id').paginate(page = page, per_page = per_page)
    

    if form.validate_on_submit():
        search_text         = form.search_text.data
        category_name       = form.category_name.data
        max_total_time      = form.max_total_time.data

        # If a category choice is not made
        if category_name == "":
            
            # Search query on title and description (case insensitive) and max cooking time
            if max_total_time != None:
                # Pagination of filtered recipes 
                filtered_recipes    = Recipe.objects.order_by('-recipe_id')((Q(title__icontains = search_text) | Q(description__icontains = search_text)) & Q(total_cooking_time__lte = max_total_time)).paginate(page = page, per_page = per_page)
                # Count number of filtered recipes
                total_recipes       = Recipe.objects.order_by('-recipe_id')((Q(title__icontains = search_text) | Q(description__icontains = search_text)) & Q(total_cooking_time__lte = max_total_time)).count()
            # Search query on title and description (case insensitive)
            else:
                # Pagination of filtered recipes 
                filtered_recipes    = Recipe.objects.order_by('-recipe_id')(Q(title__icontains = search_text) | Q(description__icontains = search_text)).paginate(page = page, per_page = per_page)
                # Count number of filtered recipes
                total_recipes       = Recipe.objects.order_by('-recipe_id')(Q(title__icontains = search_text) | Q(description__icontains = search_text)).count()
        # When a category choice is made
        else:
           
            # Search query on title and description (case insensitive), category and max cooking time
            if max_total_time != None:
                # Pagination of filtered recipes 
                filtered_recipes    = Recipe.objects.order_by('-recipe_id')((Q(title__icontains = search_text) | Q(description__icontains = search_text)) & Q(category_name = category_name) & Q(total_cooking_time__lte = max_total_time)).paginate(page = page, per_page = per_page)
                # Count number of filtered recipes
                total_recipes       = Recipe.objects.order_by('-recipe_id')((Q(title__icontains = search_text) | Q(description__icontains = search_text)) & Q(category_name = category_name) & Q(total_cooking_time__lte = max_total_time)).count()
            # Search query on title and description (case insensitive) and category 
            else:
                # Pagination of filtered recipes 
                filtered_recipes    = Recipe.objects.order_by('-recipe_id')((Q(title__icontains = search_text) | Q(description__icontains = search_text)) & Q(category_name = category_name)).paginate(page = page, per_page = per_page)
                # Count number of filtered recipes
                total_recipes       = Recipe.objects.order_by('-recipe_id')((Q(title__icontains = search_text) | Q(description__icontains = search_text)) & Q(category_name = category_name)).count()

        return render_template('recipes.html', title = 'Filter results recipes', form = form, recipes = filtered_recipes, total_recipes = total_recipes, category_name = category_name)

    total_meat_recipes          = Recipe.objects(category_name = "Meat").count()
    total_seafood_recipes       = Recipe.objects(category_name = "Seafood").count()
    total_vegetarian_recipes    = Recipe.objects(category_name = "Vegetarian").count()
    total_recipes               = Recipe.objects.count()

    # Getting latest 5 recipes for footer
    footer_recipes              = Recipe.objects[:5].order_by('-recipe_id')

    # Render html, recipes count (by category), search form and footer recipes
    return render_template('index.html', total_meat_recipes = total_meat_recipes, total_seafood_recipes = total_seafood_recipes, total_vegetarian_recipes = total_vegetarian_recipes, form = form, total_recipes = total_recipes, footer_recipes = footer_recipes)

# ------ GET ALL RECIPES ------ #
@app.route("/recipes", methods=['GET', 'POST'])
def recipes():
    form = searchForm()

    # Set per page for pagination
    per_page = 2

    # Set default page parameter to 1 for pagination
    page = request.args.get('page', 1, type = int)

    # Get recipes and order descending so that newest recipes come first
    recipes = Recipe.objects.order_by('-recipe_id').paginate(page = page, per_page = per_page)
    

    if form.validate_on_submit():
        search_text         = form.search_text.data
        category_name       = form.category_name.data
        max_total_time      = form.max_total_time.data
        # Redefine page nummer. Otherwise page number will cause 404 while using pagination
        page                = 1

        # If a category choice is not made
        if category_name == "":
            
            # Search query on title and description (case insensitive) and max cooking time
            if max_total_time != None:
                # Pagination of filtered recipes 
                filtered_recipes    = Recipe.objects.order_by('-recipe_id')((Q(title__icontains = search_text) | Q(description__icontains = search_text)) & Q(total_cooking_time__lte = max_total_time)).paginate(page = page, per_page = per_page)
                # Count number of filtered recipes
                total_recipes       = Recipe.objects.order_by('-recipe_id')((Q(title__icontains = search_text) | Q(description__icontains = search_text)) & Q(total_cooking_time__lte = max_total_time)).count()
            # Search query on title and description (case insensitive)
            else:
                # Pagination of filtered recipes 
                filtered_recipes    = Recipe.objects.order_by('-recipe_id')(Q(title__icontains = search_text) | Q(description__icontains = search_text)).paginate(page = page, per_page = per_page)
                # Count number of filtered recipes
                total_recipes       = Recipe.objects.order_by('-recipe_id')(Q(title__icontains = search_text) | Q(description__icontains = search_text)).count()
        # When a category choice is made
        else:
           
            # Search query on title and description (case insensitive), category and max cooking time
            if max_total_time != None:
                # Pagination of filtered recipes 
                filtered_recipes    = Recipe.objects.order_by('-recipe_id')((Q(title__icontains = search_text) | Q(description__icontains = search_text)) & Q(category_name = category_name) & Q(total_cooking_time__lte = max_total_time)).paginate(page = page, per_page = per_page)
                # Count number of filtered recipes
                total_recipes       = Recipe.objects.order_by('-recipe_id')((Q(title__icontains = search_text) | Q(description__icontains = search_text)) & Q(category_name = category_name) & Q(total_cooking_time__lte = max_total_time)).count()
            # Search query on title and description (case insensitive) and category 
            else:
                # Pagination of filtered recipes 
                filtered_recipes    = Recipe.objects.order_by('-recipe_id')((Q(title__icontains = search_text) | Q(description__icontains = search_text)) & Q(category_name = category_name)).paginate(page = page, per_page = per_page)
                # Count number of filtered recipes
                total_recipes       = Recipe.objects.order_by('-recipe_id')((Q(title__icontains = search_text) | Q(description__icontains = search_text)) & Q(category_name = category_name)).count()

        footer_recipes              = Recipe.objects[:5].order_by('-recipe_id')
        return render_template('recipes.html', title = 'Filtered results recipes', form = form, recipes = filtered_recipes, total_recipes = total_recipes, category_name = category_name, footer_recipes = footer_recipes)
    
    total_recipes = Recipe.objects.count()

    # Getting latest 5 recipes for footer
    footer_recipes              = Recipe.objects[:5].order_by('-recipe_id')

    # Render html, giving its title and passing in recipes, recipes count, search form and footer recipes
    return render_template('recipes.html', title = 'All recipes', recipes = recipes, total_recipes = total_recipes, form = form, footer_recipes = footer_recipes)

# ------ GET ALL RECIPES BY USER ------ #
@app.route('/user/<author>')
def user_recipes(author):
    # Set per page for pagination
    per_page = 6

    # Set default page parameter to 1 for pagination
    page = request.args.get('page', 1, type = int)

    # Get recipe and order descending so that newest recipes come first
    user_recipes = Recipe.objects(author = author).order_by('-recipe_id').paginate(page = page, per_page = per_page)

    # Count user's recipes
    total_user_recipes = Recipe.objects(author = author).count()

    # Getting latest 5 recipes for footer
    footer_recipes              = Recipe.objects[:5].order_by('-recipe_id')
    
    # Render html, giving its title and passing in the user's recipe object and recipes for footer
    return render_template('user_recipes.html', title = 'User recipes', user_recipes = user_recipes, total_user_recipes = total_user_recipes, author = author, footer_recipes = footer_recipes)

# ------ GET ALL MEAT RECIPES ------ #
@app.route("/meat-recipes")
def meat_recipes():
    # Set per page for pagination
    per_page = 6

    # Set default page parameter to 1 for pagination
    page = request.args.get('page', 1, type = int)

    # Get recipe and order descending so that newest recipes come first
    recipes = Recipe.objects(category_name = "Meat").order_by('-recipe_id').paginate(page = page, per_page = per_page)

    # Count number of recipes
    total_recipes = Recipe.objects(category_name = "Meat").count()

    # Getting latest 5 recipes for footer
    footer_recipes              = Recipe.objects[:5].order_by('-recipe_id')
        
    # Render html, giving its title, recipes by category, count of category recipes and footer recipes
    return render_template('meat_recipes.html', title = 'All meat recipes', recipes = recipes, total_recipes = total_recipes, footer_recipes = footer_recipes)

# ------ GET ALL SEAFOOD RECIPES ------ #
@app.route("/seafood-recipes")
def seafood_recipes():
    # Set per page for pagination
    per_page = 6

    # Set default page parameter to 1 for pagination
    page = request.args.get('page', 1, type = int)


    # Get recipe and order descending so that newest recipes come first
    recipes = Recipe.objects(category_name = "Seafood").order_by('-recipe_id').paginate(page = page, per_page = per_page)

    # Count number of recipes
    total_recipes = Recipe.objects(category_name = "Seafood").count()

    # Getting latest 5 recipes for footer
    footer_recipes              = Recipe.objects[:5].order_by('-recipe_id')
        
    # Render html, giving its title, recipes by category, count of category recipes and footer recipes
    return render_template('seafood_recipes.html', title = 'All seafood recipes', recipes = recipes, total_recipes = total_recipes, footer_recipes = footer_recipes)

# ------ GET ALL VEGETARIAN RECIPES ------ #
@app.route("/vegetarian-recipes")
def vegetarian_recipes():
    # Set per page for pagination
    per_page = 6

    # Set default page parameter to 1 for pagination
    page = request.args.get('page', 1, type = int)

    # Get recipe and order descending so that newest recipes come first
    recipes = Recipe.objects(category_name = "Vegetarian").order_by('-recipe_id').paginate(page = page, per_page = per_page)

    # Count number of recipes
    total_recipes = Recipe.objects(category_name = "Vegetarian").count()

    # Getting latest 5 recipes for footer
    footer_recipes              = Recipe.objects[:5].order_by('-recipe_id')
        
    # Render html, giving its title, recipes by category, count of category recipes and footer recipes
    return render_template('vegetarian_recipes.html', title = 'All vegetarian recipes', recipes = recipes, total_recipes = total_recipes, footer_recipes = footer_recipes)

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

        # Count total cooking time
        total_cooking_time  = preparation_time + cooking_time   

        # Create new instance of recipe
        new_recipe_id   = RecipeID(recipe_id = recipe_id)
        new_recipe      = Recipe(recipe_id = recipe_id, title = title, description = description, category_name = category_name, ingredients = ingredients,\
                            directions = directions, preparation_time = preparation_time, cooking_time = cooking_time, total_cooking_time = total_cooking_time, \
                            calories = calories, protein = protein, carbohydrates = carbohydrates, cholesterol = cholesterol, author_id = author_id, author = author,\
                            recipe_image = recipe_image, recipe_image_name = recipe_image_name)
        # Insert record to the DB
        new_recipe_id.save()
        new_recipe.save()
        flash('Your awesome recipe has been added!', 'success')
        # Go to all account page after submitting a recipe
        return redirect(url_for('account'))

    # Getting latest 5 recipes for footer
    footer_recipes              = Recipe.objects[:5].order_by('-recipe_id')

    # Render html, giving its title, passing in the form and footer recipes
    return render_template('add_recipe.html', title = 'Add recipe', form = form, footer_recipes = footer_recipes)

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
        recipe.title               = form.title.data
        recipe.description         = form.description.data
        recipe.category_name       = form.category_name.data
        recipe.ingredients         = form.ingredients.data
        recipe.directions          = form.directions.data    
        recipe.preparation_time    = form.preparation_time.data 
        recipe.cooking_time        = form.cooking_time.data        
        recipe.calories            = form.calories.data              
        recipe.protein             = form.protein.data               
        recipe.carbohydrates       = form.carbohydrates.data           
        recipe.cholesterol         = form.cholesterol.data  

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

        # Count total cooking time
        total_cooking_time  = recipe.preparation_time + recipe.cooking_time   

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

    # Getting latest 5 recipes for footer
    footer_recipes = Recipe.objects[:5].order_by('-recipe_id')

    # Render html, giving its title, passing in the form and footer recipes
    return render_template('add_recipe.html', title = 'Edit recipe', form = form, footer_recipes = footer_recipes)  

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

    # Getting latest 5 recipes for footer
    footer_recipes              = Recipe.objects[:5].order_by('-recipe_id')

    # Render html, giving its title, recipe and footer recipes
    return render_template('recipe.html', title = title, recipe = recipe, footer_recipes = footer_recipes)

# ------ USER ACCOUNT ------ #
@app.route("/account", methods=['GET', 'POST'])
# Login is required for account page
@login_required
def account():
    author              = current_user.username
    user_first_name     = current_user.first_name 
   
    # Make recipe list by author
    recipe_list = Recipe.objects(author = author)
    
    # Getting latest 5 recipes for footer
    footer_recipes              = Recipe.objects[:5].order_by('-recipe_id') 

    # Render html, giving its title, recipe list by author, user's first name and footer recipes
    return render_template('account.html', title = 'User account', recipe_list = recipe_list, user_first_name = user_first_name, footer_recipes = footer_recipes)

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

    # Getting latest 5 recipes for footer
    footer_recipes              = Recipe.objects[:5].order_by('-recipe_id')

    # Render html, giving its title, passing in the form and footer recipes
    return render_template('login.html', title = 'Login', form = form, footer_recipes = footer_recipes)

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

    # Getting latest 5 recipes for footer
    footer_recipes = Recipe.objects[:5].order_by('-recipe_id')

    # Render html, giving its title, passing in the form and footer recipes
    return render_template("register.html", title = "Register", form = form, footer_recipes = footer_recipes)