from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        return redirect(url_for("success", username=name))

    return render_template("form.html")


@app.route("/success/<username>")
def success(username):
    return render_template("success.html", name=username)


if __name__ == "__main__":
    app.run(debug=True)
