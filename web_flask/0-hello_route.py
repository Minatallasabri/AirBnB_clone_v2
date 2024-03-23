#!/usr/bin/python3
"""
web flask app
"""
from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

