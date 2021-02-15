import json
from flask import jsonify, Blueprint, request
from flask_cors import cross_origin

from src.database import Session
from src.entities.entity import Selector
from src.entities.event import Event, EventSchema

session = Session()
event_bp = Blueprint('event', __name__)


@event_bp.route('/')
@event_bp.route('/events', methods=['GET', 'OPTIONS'])
@cross_origin()
def get_events():
    events = Selector.select_all(session, Event)
    schema = EventSchema(many=True)
    events_as_json = schema.dump(events)
    return jsonify(events_as_json), 200


@event_bp.route('/event/<event_id>', methods=['GET'])
@cross_origin()
def get_event_by_id(event_id):
    event = Selector.select_by_id(session, event_id, Event)
    schema = EventSchema()
    event_as_json = schema.dump(event)
    return jsonify(event_as_json), 200


@event_bp.route('/event', methods=['OPTIONS'])
def allow_preflight_request():
    return jsonify({'status_code': 200})


@event_bp.route('/event', methods=['POST'])
def add_event():
    data = json.loads(json.dumps(request.get_json()))
    posted_event = EventSchema(only=('name', 'host', 'date')).load(data)
    event = Event(**posted_event)
    event.create(session)

    new_event = EventSchema().dump(event)
    return jsonify(new_event), 201


@event_bp.route('/event/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Selector.select_by_id(session, event_id, Event)
    event.delete(session)

    return jsonify({"result": "deleted"}), 200


@event_bp.route('/event', methods=['PUT', 'OPTIONS'])
def update_event():
    data = json.loads(json.dumps(request.get_json()))
    event_from_request = EventSchema().load(data)
    event = Selector.select_by_id(session, event_from_request.get('id'), Event)
    event.name = event_from_request.get('name')
    event.host = event_from_request.get('host')
    event.date = event_from_request.get('date')
    event.update(session)

    schema = EventSchema()
    event = schema.dump(event)
    return jsonify(event), 200
