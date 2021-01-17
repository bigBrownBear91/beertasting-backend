#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_cors import CORS

from src.database import Session
from src.entities.entity import Selector
from src.entities.event import Event, EventSchema

app = Flask(__name__)
CORS(app)

session = Session()


@app.route('/events')
def get_events():
    event = Selector(Event)
    event.select_all(session)

    schema = EventSchema(many=True)
    jsonevent = schema.dump(event.result)

    return jsonify(jsonevent)


@app.route('/event/<event_id>')
def get_event(event_id):
    event = Selector(Event)
    event.select_by_id(session, event_id)

    schema = EventSchema()
    json_event = schema.dump(event.result)

    return jsonify(json_event)


@app.route('/event', methods=['POST'])
def add_event():
    posted_event = EventSchema(only=('name', 'host', 'date')).load(request.get_json())

    event = Event(**posted_event)
    event.create(session)

    new_event = EventSchema().dump(event)
    return jsonify(new_event), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
