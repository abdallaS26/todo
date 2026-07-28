from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/todos")
def todos():
    return render_template("todo_list.html")


@app.route("/todo/<int:id>")
def todo_details(id):
    return render_template("todo_details.html")


if __name__ == "__main__":
    app.run(debug=True)