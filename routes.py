from flask import Flask, render_template, Blueprint

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return "<p>Add home page if theres time</p>"

@routes.route("/login")
def login():
    return render_template("login.html")