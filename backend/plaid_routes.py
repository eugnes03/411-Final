from flask import Blueprint, request, jsonify
from plaid import Client
import os
from dotenv import load_dotenv
from loan_logic import simulate_credit_score  # Assuming loan_logic.py contains simulation logic

# Load environment variables from .env
load_dotenv()

# Initialize Flask Blueprint
plaid_blueprint = Blueprint('plaid', __name__)

# Initialize Plaid client
client = Client(
    client_id=os.getenv('PLAID_CLIENT_ID'),
    secret=os.getenv('PLAID_SECRET'),
    environment=os.getenv('PLAID_ENV', 'sandbox')  # Default to sandbox
)

# Route to generate a link token
@plaid_blueprint.route('/create_link_token', methods=['POST'])
def create_link_token():
    try:
        user_id = 'unique_user_id'  # Replace with your unique user ID logic
        response = client.LinkToken.create({
            'user': {
                'client_user_id': user_id
            },
            'client_name': 'Your App Name',
            'products': ['auth', 'transactions', 'income'],
            'country_codes': ['US'],
            'language': 'en',
        })
        return jsonify({'link_token': response['link_token']})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

# Route to exchange public token for access token
@plaid_blueprint.route('/exchange_public_token', methods=['POST'])
def exchange_public_token():
    data = request.json
    public_token = data.get('public_token')

    try:
        response = client.Item.public_token.exchange(public_token)
        access_token = response['access_token']
        return jsonify({'access_token': access_token})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

# Route to fetch transactions
@plaid_blueprint.route('/transactions', methods=['GET'])
def get_transactions():
    access_token = request.args.get('access_token')  # Replace with secure token storage

    try:
        start_date = '2023-01-01'
        end_date = '2023-12-31'
        response = client.Transactions.get(access_token, start_date, end_date)
        transactions = response['transactions']
        return jsonify({'transactions': transactions})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

# Route to fetch income
@plaid_blueprint.route('/fetch_income', methods=['GET'])
def fetch_income():
    access_token = request.args.get('access_token')
    try:
        income_response = client.Income.get(access_token)
        return jsonify(income_response['income'])
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

# Route to fetch liabilities
@plaid_blueprint.route('/fetch_liabilities', methods=['GET'])
def fetch_liabilities():
    access_token = request.args.get('access_token')
    try:
        liabilities_response = client.Liabilities.get(access_token)
        return jsonify(liabilities_response['liabilities'])
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

# Route to simulate credit score
@plaid_blueprint.route('/simulate_credit_score', methods=['GET'])
def simulate_credit_score_endpoint():
    access_token = request.args.get('access_token')
    try:
        # Fetch income and liabilities
        income = client.Income.get(access_token)['income']
        liabilities = client.Liabilities.get(access_token)['liabilities']

        # Simulate credit score
        score = simulate_credit_score(income, liabilities)

        return jsonify({'credit_score': score})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
