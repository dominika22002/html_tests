from flask import Flask
from flask_cors import CORS

import json
import flask.json
import geog

app = Flask('Aplikacja')
CORS(app)

locations = [
        None,
        (51.1013665, 17.0266555),
        (51.1013665,17.0266555)
]

course = 0

def update_positions():
    global locations
    global course
    print('updating positions')

    a, b = geog.propagate(locations[1][::-1], course, 5)
    c, d = geog.propagate(locations[2][::-1], -course, 3)

    locations[1] = (b, a)
    locations[2] = (d, c)

    course += 20

@app.route('/beka')
def beka():
    return 'Beka'

@app.route('/drone/<int:drone_id>')
def get_drone(drone_id):
        global locations
        global course
        if drone_id not in range(1,3):
            return flask.json.jsonify({'status': 'error', 'message': 'no such drone'})

        names = [
            'none',
            'Nabuchodonozor',
            'Ozyrys'
        ]

        drone = {
            'id': drone_id,
            'name': names[drone_id],
            'position': locations[drone_id]
        }

        update_positions()

        return flask.json.jsonify(drone)


app.run()