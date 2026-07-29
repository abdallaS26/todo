from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select, insert

from database import engine
from models import users, todos

app = Flask(__name__)
app.secret_key = "change_this_secret"

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/todos")
def todo_list():
    with engine.connect() as conn:
        result = conn.execute(select(todos).limit(20))
        todo_rows = result.mappings().all()
    return render_template("todo_list.html", todos=todo_rows)

@app.route("/todo/<int:id>")
def todo_details(id):
    with engine.connect() as conn:
        result = conn.execute(select(todos).where(todos.c.id == id))
        todo_row = result.mappings().first()
    if not todo_row:
        return redirect(url_for("todo_list"))
    return render_template("todo_details.html", todo=todo_row)

@app.route("/auth/login", methods=["POST"])
def auth_login():
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")

    with engine.connect() as conn:
        result = conn.execute(select(users).where(users.c.email == email))
        user_row = result.mappings().first()

    if not user_row or not check_password_hash(user_row["password"], password):
        flash("Invalid email or password", "error")
        return redirect(url_for("login_page"))

    session["user_id"] = user_row["id"]
    return redirect(url_for("todos"))

@app.route("/auth/register", methods=["POST"])
def auth_register():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")

    if not name or not email or not password:
        flash("All fields are required", "error")
        return redirect(url_for("register_page"))

    hashed_password = generate_password_hash(password)
    with engine.begin() as conn:
        conn.execute(insert(users).values(name=name, email=email, password=hashed_password))

    flash("Account created successfully. Please log in.", "success")
    return redirect(url_for("login_page"))

if __name__ == "__main__":
    app.run(debug=True)
