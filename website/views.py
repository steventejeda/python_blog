from flask import Blueprint, render_template
from flask_login import login_required, current_user

import sys
sys.dont_write_bytecode = True

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("home.html", name="Steven") 