import json
from flask import jsonify, Blueprint, request
from flask_cors import cross_origin

from src.data_model.model import Event
from src.data_model.orm_mapper import EventTable, BeerTable
from src.data_model.schemas import EventSchema, BeerSchema

event_bp = Blueprint('event', __name__)
beer_bp = Blueprint('beer', __name__)


@event_bp.route('/')
@event_bp.route('/events', methods=['GET', 'OPTIONS'])
@cross_origin()
def get_events():
    events = EventTable.get_all()
    schema = EventSchema(many=True)
    events_as_json = schema.dump(events)
    return jsonify(events_as_json), 200


@event_bp.route('/event/<event_id>', methods=['GET'])
@cross_origin()
def get_event_by_id(event_id):
    event = Event(event_id)
    event_as_json = event.serialize()
    return jsonify(event_as_json), 200


@event_bp.route('/event', methods=['OPTIONS'])
def allow_preflight_request():
    return jsonify({'status_code': 200})


@event_bp.route('/event', methods=['POST'])
def add_event():
    data = json.loads(json.dumps(request.get_json()))
    posted_event = EventSchema(only=('name', 'host', 'date')).load(data)
    event = EventTable(**posted_event)
    event.create_or_update()

    new_event = EventSchema().dump(event)
    return jsonify(new_event), 201


@event_bp.route('/event/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = EventTable.get_by_id(event_id)
    event.delete()

    return jsonify({"result": "deleted"}), 200


@event_bp.route('/event', methods=['PUT', 'OPTIONS'])
def update_event():
    data = json.loads(json.dumps(request.get_json()))
    event_from_request = EventSchema().load(data)
    event = EventTable.get_by_id(event_from_request.get('id'))
    event.name = event_from_request.get('name')
    event.host = event_from_request.get('host')
    event.date = event_from_request.get('date')
    event.create_or_update()

    schema = EventSchema()
    event = schema.dump(event)
    return jsonify(event), 200


@beer_bp.route('/beer', methods=['OPTIONS'])
def allow_preflight_request():
    return jsonify({'status_code': 200})


@beer_bp.route('/beer', methods=['POST'])
def add_beers():
    data = json.loads(json.dumps(request.get_json()))
    posted_beer = BeerSchema(only=('name')).load(data)
    beer = BeerTable(**posted_beer)
    beer.create_or_update()

    new_beer = BeerSchema().dump(beer)
    return jsonify(new_beer), 201
