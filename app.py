from flask import Flask, render_template, request, jsonify
from routes import routes
import os

# initializing Flask app
app = Flask(__name__)

app.secret_key = os.urandom(24).hex()

# routes Blueprint
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
    monthly_debt = float(data.get('monthlyDebt', 0))
    asset_value = float(data.get('assetValue', 0))

    # Calculate debt-to-income ratio (DTI)
    monthly_income = annual_income / 12
    dti = (monthly_debt / monthly_income) * 100 if monthly_income > 0 else 100

    # Calculate loan-to-value ratio (LTV)
    ltv = (loan_amount / asset_value) * 100 if asset_value > 0 else 0

    # Eligibility checks
    qualified = (
        credit_score >= 650 and
        dti <= 40 and
        ltv <= 80 and
        annual_income >= loan_amount * 1.5
    )

    return jsonify({
        'qualified': qualified,
        'criteria': {
            'creditScore': credit_score >= 650,
            'dti': dti <= 40,
            'ltv': ltv <= 80,
            'incomeToLoanRatio': annual_income >= loan_amount * 1.5
        }
    })


if __name__ == '__main__':
    app.run(debug=True)

