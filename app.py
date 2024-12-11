from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify
from routes import routes
import os

# Initialize Flask app
app = Flask(__name__)

app.secret_key = os.urandom(24).hex()

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loan_qualification_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Register routes
app.register_blueprint(routes)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/check-eligibility', methods=['POST'])
def check_eligibility():
    data = request.json
    username = data.get('username')
    credit_score = int(data.get('creditScore', 0))
    annual_income = float(data.get('annualIncome', 0))
    loan_amount = float(data.get('loanAmount', 0))

    # Dummy logic for eligibility
    qualified = credit_score > 650 and annual_income > loan_amount * 1.5

    return jsonify({'qualified': qualified})

if __name__ == '__main__':
    app.run(debug=True)
