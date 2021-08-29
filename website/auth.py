import re
from flask import Blueprint, render_template, redirect, redirect, request, flash, url_for
from . import db
from .models import User
import sys
sys.dont_write_bytecode = True
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)




@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in!', category='Success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else: 
                flash('Password is incorrect', category='error')
        else:
            flash('Email does not exist', category='error')
                
    return render_template("login.html")


@auth.route("/log-out")
@login_required
def log_out():
    logout_user()
    return redirect(url_for("views.home"))

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        verify_password = request.form.get("verify_password")
        
        # Check the database if the end user is trying to register a email and username that already exists
        # Check if the leng
        email_exists = User.query.filter_by(email=email).first()
        username_exists  = User.query.filter_by(username=username).first()
        
        if email_exists:
            flash('Email is already in use', category='error')
        elif username_exists:
            flash('Username is already in use', category='error')
        elif password != verify_password:
            flash('Passowords do not match!', category='error')
        elif len(username) < 3: 
            flash('Username is too short', category='error')
        elif len(password) < 5:
            flash('Password is too short', category='error')
        elif len(email) < 4:
            flash('Email is invalid', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!')
            return redirect(url_for('views.home'))
        
        
    return render_template("sign_up.html")

