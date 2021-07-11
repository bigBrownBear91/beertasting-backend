from src.data_model.orm_mapper import EventTable, BeerTable
from src.data_model.schemas import EventSchema, BeerSchema


class Event:
    def __init__(self, event_id=None, event_name=None):
        assert event_id is None and event_name is not None or event_id is not None and event_name is None

        self._event = EventTable.get_by_id(event_id) if event_id is not None else EventTable.get_by_name(event_name)
        self._beers = BeerTable.get_beer_by_event(self._event.id)

        self.id = self._event.id
        self.name = self._event.name
        self.host = self._event.host
        self.date = self._event.date
        self.beers = self._beers

    def get_beer_by_name(self, name):
        beer = [beer for beer in self.beers if beer.name == name]
        if len(beer) == 0:
            raise BeerNotExisting(name)
        if len(beer) > 1:
            raise IndexError(f"More than one beer with the name {name} exists for this event")
        return beer[0]

    def serialize(self):
        schema = EventSchema(many=False)
        return schema.dump(self)

    def update(self):
        self._event.name = self.name
        self._event.host = self.host
        self._event.date = self.date
        self._event.create_or_update()

        for beer in self.beers:
            beer.create_or_update()


class BeerNotExisting(Exception):
    def __init__(self, name):
        message = f"{name} doesn't exist for this event"
        super().__init__(message)
