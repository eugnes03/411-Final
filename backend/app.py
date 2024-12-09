from flask import Flask, request, jsonify
from plaid_routes import plaid_blueprint

app = Flask(__name__)

# Register Plaid routes
app.register_blueprint(plaid_blueprint, url_prefix='/api/plaid')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
