from flask import Flask
from routes import routes

# initializing Flask app
app = Flask(__name__)

# routes Blueprint
app.register_blueprint(routes)

# reload when changes are made
if __name__ == "__main__":
    app.run(debug=True)