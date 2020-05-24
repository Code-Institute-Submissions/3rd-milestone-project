from flask import Flask

# instantiated flask application
app = Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return "<h1>Welcome to BBQ World</h1>"


@app.route("/bbq-recipes")
def recipes():
    return "<h1>The best BBQ recipes in the world</h1>"


if __name__ == "__main__":
    app.run(debug=True)