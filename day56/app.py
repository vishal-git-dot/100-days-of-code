from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    name = ""

    if request.method == "POST":
        name = request.form.get("name")

    return render_template("form.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
