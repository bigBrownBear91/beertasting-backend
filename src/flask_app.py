#!/usr/bin/env python3
import json

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from src.database import Session
from src.entities.entity import Selector
from src.entities.event import Event, EventSchema

app = Flask(__name__)
CORS(app, support_credentials=True)


session = Session()


@app.route('/events')
def get_events():
    events = Selector.select_all(session, Event)
    schema = EventSchema(many=True)
    jsonevent = schema.dump(events)

    return jsonify(jsonevent), 200


@app.route('/event/<event_id>')
def get_event(event_id):
    event = Selector.select_by_id(session, event_id, Event)

    schema = EventSchema()
    json_event = schema.dump(event)

    return jsonify(json_event), 200


@app.route('/event', methods=['POST'])
def add_event():
    data = json.loads(json.dumps(request.get_json()))
    posted_event = EventSchema(only=('name', 'host', 'date')).load(data)
    event = Event(**posted_event)
    event.create(session)

    new_event = EventSchema().dump(event)
    return jsonify(new_event), 201


@app.route('/event/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Selector.select_by_id(session, event_id, Event)
    event.delete(session)

    return jsonify({"result": "deleted"}), 200


@app.route('/event', methods=['PATCH'])
@cross_origin(supports_credentials=True)
def update_event():
    data = json.loads(json.dumps(request.get_json()))
    put_event = EventSchema().load(data)
    event = Selector.select_by_id(session, put_event.id, Event)
    event.name = put_event.name
    event.host = put_event.host
    event.date = put_event.date

    return jsonify(update_event), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
