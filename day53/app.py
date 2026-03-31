from flask import Flask

app = Flask(__name__)

# Static Routes
@app.route("/")
def home():
    return "Welcome to Home Page"

@app.route("/about")
def about():
    return "This is About Page"

@app.route("/contact")
def contact():
    return "Contact Page"


# Dynamic Route
@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}!"


# Dynamic Route with Type
@app.route("/age/<int:age>")
def age(age):
    return f"Your age is {age}"


if __name__ == "__main__":
    app.run(debug=True)
