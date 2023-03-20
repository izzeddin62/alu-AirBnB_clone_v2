#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return("Hello HBNB!")
"""
    Display "Hello HBNB!" when the root route is accessed.
    Returns:
        str: The string "Hello HBNB!".
"""

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
