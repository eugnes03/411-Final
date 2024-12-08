from flask import Flask, render_template, Blueprint, request, redirect, url_for

# Define the Blueprint
routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return "<p>Add home page if there's time</p>"

@routes.route("/create-account", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        # Get form data
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        # Debugging: Print form data
        print(f"Username: {username}, Email: {email}, Password: {password}, Confirm: {confirm_password}")

    return render_template("create-account.html")


@routes.route("/update-password", methods=["GET", "POST"])
def update_password():
    if request.method == "POST":
        # Get form data
        username = request.form.get("username")
        email = request.form.get("email")
        new_password = request.form.get("password")

        # Debugging: Print form data
        print(f"Username: {username}, Email: {email}, Password: {new_password}")

    return render_template("update-password.html")

@routes.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")
