from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    error = ""
    name = ""

    if request.method == "POST":
        name = request.form.get("name")

        if not name:
            error = "Name is required!"
        else:
            return render_template("form.html", name=name)

    return render_template("form.html", error=error, name=name)

if __name__ == "__main__":
    app.run(debug=True)
