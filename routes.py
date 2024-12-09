from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash
from sqlalchemy.orm import sessionmaker
from initialize_db import engine, User
import hashlib, os

Session = sessionmaker(bind=engine)
session = Session()

# Define the Blueprint
routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return "<p>Add home page if there's time</p>"


def flash_and_render(template, message, category="info"):
    flash(message, category)
    return render_template(template)

@routes.route('/create-account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        if not username or not email or not password:
            return flash_and_render('create-account.html', "All fields are required.", "error")

        if password != confirm_password:
            return flash_and_render('create-account.html', "Passwords do not match.", "error")

        # Check if user exists
        if session.query(User).filter_by(username=username).first():
            return flash_and_render('create-account.html', "Username already exists.", "error")

        if session.query(User).filter_by(email=email).first():
            return flash_and_render('create-account.html', "Email already exists.", "error")

        # Add user
        try:
            salt = os.urandom(16).hex()
            hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
            new_user = User(username=username, email=email, salt=salt, hashed_password=hashed_password)
            session.add(new_user)
            session.commit()
            return flash_and_render('create-account.html', f"Account created! Username: {username}, Email: {email}", "success")
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
            return flash_and_render('create-account.html', "An error occurred. Please try again.", "error")

    return render_template('create-account.html')


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
