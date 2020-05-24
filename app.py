from flask import Flask, render_template, url_for

# instantiated flask application
app = Flask(__name__)

recipe_list = [
    {
        "user" : "BBQ fan",
        "title" : "The best BBQ burger",
        "description" : "We like our burgers piled sky-high. This version comes with our secret sauce (made from four very simple ingredients), sweet and sour onions, emmental cheese, gherkins, frilly lettuce, and more."
    },
        {
        "user" : "Another BBQ fan",
        "title" : "BBQ pulled pork",
        "description" : "Pulled pork is a great recipe to feed a crowd at a summer BBQ. Ours are served up in soft buns with crunchy coleslaw – plus we've included extra instructions on how to make this recipe in a slow cooker."
    }
]

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('index.html')


@app.route("/recipes")
def recipes():
    return render_template('recipes.html', recipe_list = recipe_list)


if __name__ == "__main__":
    app.run(debug=True)