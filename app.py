from flask import Flask, render_template, request, jsonify
from routes import routes
import os
from plaid_routes import plaid_blueprint
# initializing Flask app
app = Flask(__name__)

app.secret_key = os.urandom(24).hex()

# routes Blueprint
app.register_blueprint(routes)
app.register_blueprint(plaid_blueprint, url_prefix='/api/plaid')
@app.route('/')
def home():
    '''
    Home route
    '''
    return render_template('home.html')

@app.route('/check-eligibility', methods=['POST'])
def check_eligibility():
    '''
    Check eligibility route

    Returns:

    qualified (bool): True if the user is eligible for the loan, False otherwise
    '''
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

