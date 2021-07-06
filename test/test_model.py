import datetime

from src.data_model.model import Event
from src.data_model.orm_mapper import EventTable, BeerTable
from test.set_up import test_db


def test_event(test_db):
    test_date = datetime.date(2021, 6, 21)
    test_event = EventTable('test_name', 'test_host', test_date)
    test_event.add_beer(BeerTable('beer1', 'brew1', 'ch'))
    test_event.add_beer(BeerTable('beer2', 'brew2', 'ch'))
    test_event.add_beer(BeerTable('beer3', 'brew2', 'ch'))
    test_event.create_or_update()

    event_load_again = Event(None, 'test_name')
    assert event_load_again.host == 'test_host'
    assert event_load_again.get_beer_by_name('beer3').brewery == 'brew2'

    event_load_again.name = 'new_test_name'
    event_load_again.update()

    event_load_second_time = Event(None, 'new_test_name')
    assert event_load_second_time.id == event_load_again.id
    updated_beer = event_load_second_time.get_beer_by_name('beer3')
