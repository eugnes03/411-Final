from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash
from sqlalchemy.orm import sessionmaker
from initialize_db import engine, User
import hashlib, os

Session = sessionmaker(bind=engine)
session = Session()

# Define the Blueprint
routes = Blueprint("routes", __name__)

def flash_and_render(template, message, category="info"):
    flash(message, category)
    return render_template(template)

@routes.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@routes.route('/create-account', methods=['GET', 'POST'])
def create_account():
    '''
    Create a new account

    - Check if all fields are filled
    - Check if passwords match
    - Check if username and email are unique
    - Hash the password and save the user
    '''
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

    '''
    Update the password of an existing user

    - Check if all fields are filled
    - Check if user exists
    - Update the password
    '''
    if request.method == "POST":
        # Get form data
        username = request.form.get("username")
        email = request.form.get("email")
        new_password = request.form.get("password")

        if not username or not email or not new_password:
            return flash_and_render('update-password.html', "All fields are required.", "error")

        # Check if user exists
        existing_user = session.query(User).filter_by(username=username, email=email).first()
        if not existing_user:
            return flash_and_render('update-password.html', "User not found. Please check the username or email.", "error")


        # Update password
        try:
            hashed_password = hashlib.sha256((new_password + existing_user.salt).encode()).hexdigest()
            existing_user.hashed_password = hashed_password
            session.commit()
            return redirect(url_for('routes.login'))
        except Exception as e:
            session.rollback()
            flash("An error occurred while updating the password.", "error")
            print(f"Error: {e}")
            return render_template('update-password.html')

    return render_template("update-password.html")


@routes.route("/login", methods=["GET", "POST"])
def login():
    '''
    Login a user

    - Check if all fields are filled
    - Check if user exists
    - Check if password is correct
    '''

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return flash_and_render('login.html', "All fields are required.", "error")

        user = session.query(User).filter_by(username=username).first()

        if not user:
            return flash_and_render('login.html', "Invalid username or password.", "error")

        hashed_input_password = hashlib.sha256((password + user.salt).encode()).hexdigest()
        if hashed_input_password != user.hashed_password:
            return flash_and_render('login.html', "Invalid username or password.", "error")

        flash(f"Welcome back, {username}!", "success")
        return redirect(url_for('routes.index'))

    return render_template("login.html")



