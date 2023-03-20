#!/usr/bin/python3
"""starts a Flask web application that listens on 0.0.0.0, port 5000,
and has only 2 routes:
- "/" displays "Hello HBNB!"
- "/hbnb" displays "HBNB"
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return("HBNB")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
