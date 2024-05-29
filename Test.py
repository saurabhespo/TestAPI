from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def hello():
    return "Hello"

