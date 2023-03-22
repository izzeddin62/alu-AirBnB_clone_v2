#!/usr/bin/python3
"""simple flask routes"""
from flask import Flask, abort, render_template
from models import storage
from models.state import State;

app = Flask(__name__)


@app.route('/test', strict_slashes=False)
def number_odd_or_even():
    """return message with paramns"""
    states = storage.all(State)
    states_list = []
    for i in states.keys():
        states_list.append(states[i])
    return render_template('7-states_list.html',
                            states=states_list)

@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
