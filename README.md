# [BBQ World](https://bbq-world.herokuapp.com)

<img src="https://github.com/GitNorthWay/3rd-milestone-project/blob/master/docs/mock_bbq_world.png?raw=true" alt="BBQ World" width="800">

BBQ World is a web application, part of my Full Stack Developer study at Code Institute, that allows users to store and easily access BBQ cooking recipes. Recipes would include fields such as ingredients, preparation steps and categories such as meat, seafood and vegetarian. The backend code and frontend form(s) allow users to add new recipes to the site, edit them and delete them (CRUD: Create, Read, Update and Delete). In the implementation of the web application I went one step further than the original assignment and implemented a login and registration method for users as well. To locate recipes I made a search functionality based on title, description, category and total cooking time (including preparation).

A live demo can be found [here](https://bbq-world.herokuapp.com).

### Project purpose

Build a full-stack site that allows your users to manage a common dataset about a particular domain.

### Project values

Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members.
The site owner advances their own goals by providing this functionality, potentially by being a regular user themselves. The site owner might also benefit from the collection of the dataset as a whole.

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
