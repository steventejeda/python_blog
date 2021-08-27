from flask import Blueprint, render_template, redirect, redirect, request

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template("login.html")

@auth.route("/log-out")
def log_out():
    return redirect(url_for("views.home"))

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    verify_password = request.form.get("verify_password")
    return render_template("sign_up.html")

