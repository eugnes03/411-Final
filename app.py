from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

