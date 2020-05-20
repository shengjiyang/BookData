  # web_app/routes/home_routes.py

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def home_page():
    return render_template("home_page.html")

# @home_routes.route("/about")
# def about():
#     return "About me"