# [BBQ World](https://bbq-world.herokuapp.com)

<img src="https://github.com/GitNorthWay/3rd-milestone-project/blob/master/docs/mock_bbq_world.png?raw=true" alt="BBQ World" width="800">

BBQ World is a web application, part of my Full Stack Developer study at Code Institute, that allows users to store and easily access BBQ cooking recipes. Recipes would include fields such as ingredients, preparation steps and categories such as meat, seafood and vegetarian. The backend code and frontend form(s) allow users to add new recipes to the site, edit them and delete them (CRUD: Create, Read, Update and Delete). In the implementation of the web application I went one step further than the original assignment and implemented a login and registration method for users as well. To locate recipes I made a search functionality based on title, description, category and total cooking time (including preparation).

A live demo can be found [here](https://bbq-world.herokuapp.com).

### Project purpose

Build a full-stack site that allows your users to manage a common dataset about a particular domain.

### Project values

Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members.
The site owner advances their own goals by providing this functionality, potentially by being a regular user themselves. The site owner might also benefit from the collection of the dataset as a whole.

## UX

While creating this web application I had user stories in mind, choose a framework to work with and made a wireframe.

### User stories

For an optimal user experience I created the following user stories, based on the sentence ‘As a user I want to’:

- Browse for recipes
- Search for specific recipes based on text, category and/or cooking time
- Filter recipes based on text, category and/or cooking time
- Add my favorite recipes
- Edit my recipes
- Delete my recipes
- View my recipes
- View other user’s recipes
- Register to be able to add my recipe(s)
- Login to manage my recipes

### Frameworks

#### Bootstrap 4.7.0

I've chosen to work with Bootstrap because it a widely used framework for developing mobile first applications. It's helping in development by its great grid system and list of components ready to use.
I made use of the [Simplex theme of Bootswatch](https://bootswatch.com/simplex/). The reason for this is that I wanted to have a simple and ‘clean’ design. The second reason is that I wanted to make use of red and blue as the main colors, which are represented in this theme.

#### jQuery 3.5.1

jQuery is a lightweight, "write less, do more", JavaScript library. Therefore I’ve used jQuery in the application

#### Font Awesome 4.7.0

Font Awesome is a widely used framework for icons with a simple implementation. Therefore I’ve chosen this framework over others.

#### Flask 1.1.2

Flask is used as a microframework for this web application to render html from its routes/views.

#### Colors

In the web application you see two main colors: red and blue.
Red stands for passion, love, adventure and fire. Things I associate with BBQ and with me other people in my environment.
Blue is often associated with depth and stability. It symbolizes trust, loyalty, wisdom and confidence. Therefore I thought it would be a great color to compensate the negative associations of red: danger, dominant etc.
My main colors are:

![#D9230F](https://placehold.it/15/D9230F/D9230F) `#D9230F`
![#029ACF](https://placehold.it/15/029ACF/029ACF) `#029ACF`
![#469408](https://placehold.it/15/469408/469408) `#469408`
![#9B479F](https://placehold.it/15/9B479F/9B479F) `#9B479F`

#### Typography

I’ve used Open Sans as font in the application with a fallback to Roboto, Helvetica Neue, Arial and sans-serif. I used these fonts due to its nice and simple layout and because they are widely used. I have chosen the recipe to stand out instead of the fonts I choose.

#### Wireframes

## Features

I have added the following features to the web application:

- Browse through all the recipes by making use of pagination
- Search and filter for recipes based on a text query (title and description), the preferred category and the total time for making the meal
- User registration
- User login
- Add recipe (when logged in)
- Edit own recipe (when logged in)
- Delete own recipe (when logged in)
- View recipe when logged in in account page accordion
- View recipe for all visitors
- Statistics on amount of recipes and recipes by category or user
- Statistics for admin: total number of users & recipes, average recipes per user and top 3 users with most recipes
- Admin view of all recipes

### Features left to implement

- Create, Update and Delete recipes for admin
- CRUD functionality for admin to manage users
- Email functionality for managing accounts (registration and lost password)
- Add ingredients and directions as an array to add and remove

## Technologies used

### Tools

- Virtual Studio Code as IDE for coding
- GitHub for version control
- [ExtendsClass](https://extendsclass.com/python-tester.html) for validating Python
- [Markup Validation Service](https://validator.w3.org/) for validating HTML
- [CSS Validation Service](http://jigsaw.w3.org/css-validator/) for validating CSS
- [JSHint](https://jshint.com/) for validating jQuery
- [Favicon generator](https://realfavicongenerator.net)

### Frontend technologies

- HTML
- CSS
- Bootstrap 4.7.0
- Font Awesome 4.7.0
- jQuery 3.5.1

### Backend technologies

- Python 3.8.3 backend coding language
- Flask 1.1.2 as microframework
- Jinja 2.11.1 for making templates
- Pillow 7.2.0 as Python Image Library
- WTForms 2.3.1 for making forms
- Flask-Login 0.5.0 to make user login
- Werkzeug 1.0.1 for hashing passwords
- Flask-mongoengine 0.9.5 as a object document mapper for MongoDB
- Heroku for hosting the web application
- MongoDB Compass as DB while developing
- MongoDB Atlas as DB in production

## Testing

Via the tools [ExtendsClass](https://extendsclass.com/python-tester.html), [Markup Validation Service](https://validator.w3.org/), [CSS Validation Service](http://jigsaw.w3.org/css-validator/), [JSHint](https://jshint.com/) I checked my code. All code is valid. In the HTML files I ignored the warning that not all sections have headers. It is intended this way.

Further I tested the website on Chrome, Firefox and Edge and for the devices: iPad (Pro), iPhone 5 & higher, iPhone 6Plus & higher and Galaxy S5 and higher.

While developing and filling the database I did several manual tests in order to make sure the website works and being able to add users and add recipes.

## Deployment

Before trying to run this web application locally, please make sure you meet the following requirements:

- [Python3](https://www.python.org/downloads) to run the application
- [PIP](https://pip.pypa.io/en/stable/installing) to install needed packages
- [Visual Studio Code](https://code.visualstudio.com) or any other IDE of your choice
- [GIT](https://www.atlassian.com/git) for cloning my repo and version control
- [MongoDB](https://www.mongodb.com) to develop your own database either locally (Mongo DB Compass) or remotely on MongoDB Atlas
- Create in MongoDB Compass or Atlas a database with the name db_recipe and the collection user or recipe (while adding users and recipes missing collections will be added)

**Local Deployment**
In case of a local deployment with MongoDB Compass, please make sure you add a ‘SECRET_KEY’ in ‘**init**.py’ as well as the ‘MONGODB_SETTINGS’: { 'db' : 'db_recipe' }.

**Deployment on Heroku**
When you want to deploy on Heroku with MongoDB Atlas, please make use of the code in ‘**init**.py’ and add the configurable variables (Config Vars) ‘SECRET_KEY’ and ‘MONGODB_HOST’ in Heroku settings, eg:

- SECRET_KEY: MySuperSecretKey (or something more secure)
- MONGODB_HOST: mongodb+srv://<user>:<password>@cluster0-hxzg5.mongodb.net/db_recipe?retryWrites=true&w=majority
- PORT: 5000

Make sure you have the **Procfile** in your files as well as the **runtime.txt** that declares the exact Python version number to use. You also can deploy locally with MongoDB Atlas. In that case you could add the above variables hard code in your code (please note that you don’t commit it to a public Github with your credentials).

After making sure you meet the requirements go ahead and enjoy:

- Clone this repository by clicking the green ‘Clone or download’ button and download the project by entering the following into Git Bash or make use of the terminal in your IDE:
  - `git clone https://github.com/GitNorthWay/3rd-milestone-project.git`
- Install all requirements from the [requirements.txt](https://github.com/GitNorthWay/3rd-milestone-project/blob/master/requirements.txt) file using this command:
  - `pip install -r requirements.txt`
- Make sure you add one user with the e-mail 'bbq@world.com' in order to make use of the admin account

## Credits & acknowledgements

### Github

- [Python gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore)

### Flask

- [Explore Flask](https://exploreflask.com/en/latest/organizing.html) for package structure
- [Flask login documentation](https://flask-login.readthedocs.io/en/latest/)
- [Basic User Authentication/Login for Flask using MongoEngine and WTForms](https://medium.com/@dmitryrastorguev/basic-user-authentication-login-for-flask-using-mongoengine-and-wtforms-922e64ef87fe)

### Python

- [Common Python 3 Error Messages (and How to Eliminate Them!)](https://www2.cs.arizona.edu/people/mccann/errors-python#Three)

### MongoEngine

- [MongoEngine Docs](https://docs.mongoengine.org/)
- [Flask MongoEngine Docs](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)
- [MongoEngine and pagination](https://stackoverflow.com/questions/15822818/flask-mongoengine-pagination)

### HTML, Bootstrap and CSS

- [Bootstrap documentation](https://getbootstrap.com/)
- [Bootstrap 4 JS Collapse](https://www.w3schools.com/bootstrap4/bootstrap_ref_js_collapse.asp)
- [W3Schools custom forms (file upload)](https://www.w3schools.com/bootstrap4/bootstrap_forms_custom.asp)
- [Bootswatch simplex theme](https://bootswatch.com/simplex/)
- [Footer at bottom page](https://stackoverflow.com/questions/643879/css-to-make-html-page-footer-stay-at-bottom-of-the-page-with-a-minimum-height-b)
- [Favicon generator](https://realfavicongenerator.net)

### Heroku deployment

[Deploying simple flask app on heroku](http://p-s.co.nz/wordpress/deploying-simple-flask-app-on-heroku/)

### Photos

In the recipe website I made use of several photos of Pixabay users. Credits and appreciation are going to:

- [Skitterphoto](https://pixabay.com/users/skitterphoto-324082/)
- [Clker-Free-Vector-Images](https://pixabay.com/nl/vectors/barbecue-grill-houtskool-brand-309842/)
- [RitaE](https://pixabay.com/nl/photos/vlees-fruit-gemuesepiess-1440105/)
- [Werasak](https://pixabay.com/nl/photos/gegrilde-inktvis-squid-grill-eten-1446233/)
- [ReinhardThrainer](https://pixabay.com/nl/photos/biefstuk-tomahawk-steak-grillen-4342500/)
- [Einladung_zum_Essen](https://pixabay.com/nl/photos/spit-antipasti-tomaten-olijven-2397041/)
- [moerschy-127417](https://pixabay.com/nl/photos/shish-kebab-vlees-spies-417994/)

### Recipes

- [All recipes](https://www.allrecipes.com/)

## Learnings

Some lessons learned besides practising Flask and Python were:

- Choose where necessary different names in code, classes and database so that its clear where the application is referencing to (commit 2afa9fd)
- Choose the layer on top of PyMongo wisely. MongoClient is relatively lightweight where MongoEngine is a Document-Object Mapper (commit 2afa9fd) which is helpful in working with models.
- Use another branch than master when testing or when things go wrong. During deployment to Heroku and being under time pressure I messed up Git. In future I would make another branch or take the project to another repo for testing purposes.

**This repo is for educational purposes only.**
