from flask import Flask, render_template, url_for
from pymongo import MongoClient

# instantiated flask application
app = Flask(__name__)

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
    return render_template('recipes.html', recipe_list = collection.find())


if __name__ == "__main__":
    app.run(debug=True)