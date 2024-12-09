from flask import Flask
from routes import routes
import os

# initializing Flask app
app = Flask(__name__)

app.secret_key = os.urandom(24).hex()

# routes Blueprint
app.register_blueprint(routes)

# reload when changes are made
if __name__ == "__main__":
    app.run(debug=True)