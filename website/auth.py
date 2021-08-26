from flask import Blueprint, render_template, redirect

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/log-out")
def log_out():
    return redirect(url_for("views.home"))

@auth.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")

