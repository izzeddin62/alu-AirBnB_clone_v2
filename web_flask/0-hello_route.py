#!/usr/bin/python3
"""starts a Flask web application that listens on 0.0.0.0, port 5000,
and has a single route that displays "Hello HBNB!" when accessed.
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return("Hello HBNB!")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
