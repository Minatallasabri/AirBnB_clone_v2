#!/usr/bin/python3
"""
Main view functions
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def display_static():
    states = storage.all('State')
    cities = storage.all('City')
    amenities = storage.all('Amenity')

    state_list = [v for v in states.values()]
    city_list = [v for v in cities.values()]
    amenity_list = [v for v in amenities.values()]
    return render_template(
        '10-hbnb_filters.html',
        states=state_list,
        cities=city_list,
        amenities=amenity_list)


@app.teardown_appcontext
def teardown(value):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
