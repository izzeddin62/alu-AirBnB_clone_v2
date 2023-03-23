#!/usr/bin/python3
"""simple flask routes"""
from flask import Flask, abort, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """return message with paramns"""
    states = storage.all(State).values()
    sorted_list = sorted(states, key=lambda x: x['name'])
    return render_template('9-states.html',
                           states=sorted_list)


@app.route('/states/<state_id>', strict_slashes=False)
def cities(state_id):
    """return message with paramns"""
    cities = storage.all(City).values()
    sorted_list = sorted(cities, key=lambda x: x['name'])
    filtered_list = [d for d in sorted_list if d['state_id'] == state_id]
    if len(filtered_list) > 0:
        states = storage.all(State).values()
        state = [d for d in states if d['id'] == state_id][0]

        return render_template('9-cities.html',
                               state=state, cities=filtered_list)
    else:
        abort(404)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
