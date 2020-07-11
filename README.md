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
- Email functionality for managing accounts (registration and lost password
- Add ingredients and directions as an array to add and remove

## Credits

gitignore python https://github.com/github/gitignore/blob/master/Python.gitignore
Local MongoDB connection https://stackoverflow.com/questions/22139173/how-to-connect-to-mongo-database-locally-using-python
Bootstrap documentation
Package structure: https://exploreflask.com/en/latest/organizing.html
flask_login: https://flask-login.readthedocs.io/en/latest/ / https://medium.com/@dmitryrastorguev/basic-user-authentication-login-for-flask-using-mongoengine-and-wtforms-922e64ef87fe

Error messages: https://www2.cs.arizona.edu/people/mccann/errors-python#Three
Bootstrap 4 JS Collapse: https://www.w3schools.com/bootstrap4/bootstrap_ref_js_collapse.asp
MongoEngine Docs: https://docs.mongoengine.org/
W3Schools custom forms (file upload): https://www.w3schools.com/bootstrap4/bootstrap_forms_custom.asp
Pagination https://stackoverflow.com/questions/15822818/flask-mongoengine-pagination
color schema: https://bootswatch.com/simplex/
Heroku deployment: http://p-s.co.nz/wordpress/deploying-simple-flask-app-on-heroku/ / http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
Footer solution: https://stackoverflow.com/questions/643879/css-to-make-html-page-footer-stay-at-bottom-of-the-page-with-a-minimum-height-b
Favicon generator: https://realfavicongenerator.net

### Photos

Rudy and Peter Skitterians (UN Skitterphoto) https://pixabay.com/users/skitterphoto-324082/
Pixbay user: Clker-Free-Vector-Images / https://pixabay.com/nl/vectors/barbecue-grill-houtskool-brand-309842/
Pixabay user: RitaE / https://pixabay.com/nl/photos/vlees-fruit-gemuesepiess-1440105/

Pixabay user: Werasak / https://pixabay.com/nl/photos/gegrilde-inktvis-squid-grill-eten-1446233/
Pixabay user: ReinhardThrainer / https://pixabay.com/nl/photos/biefstuk-tomahawk-steak-grillen-4342500/
Pixabay user: Einladung_zum_Essen / https://pixabay.com/nl/photos/spit-antipasti-tomaten-olijven-2397041/
Pixabay user: moerschy-127417 / https://pixabay.com/nl/photos/shish-kebab-vlees-spies-417994/

## Learnings

Choose where necessary different names in code, classes and database so that its clear where the application is referencing to (commit 2afa9fd
).
Choose the layer on top of PyMongo wisely. MongoClient is relatively lightweight where MongoEngine is a Document-Object Mapper (commit 2afa9fd).
