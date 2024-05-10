#!/usr/bin/python3
"""
View functions
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    states = storage.all('State')
    state_list = [v for v in states.values()]
    return render_template('7-states_list.html', states=state_list)


@app.teardown_appcontext
def teardown(value):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
