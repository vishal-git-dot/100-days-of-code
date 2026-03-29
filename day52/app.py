from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask App Structure!"

@app.route("/about")
def about():
    return "This is the About Page"

if __name__ == "__main__":
    app.run(debug=True)
