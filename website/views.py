from flask import Blueprint, render_template
import sys
sys.dont_write_bytecode = True

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html", name="Steven") 