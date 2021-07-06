from orm_mapper import EventTable, BeerTable

class Event:
    def __init__(self, event_id):
        _event = EventTable.get_by_id(event_id)
