import datetime
from re import search
from unittest.mock import patch, MagicMock

from src.data_model.model import Event
from src.data_model.orm_mapper import BeerTable, EventTable
from test.set_up import test_db


def test_event(test_db):
    event_load_again = Event(None, 'test_name')
    assert event_load_again.host == 'test_host'
    assert event_load_again.get_beer_by_name('beer3').brewery == 'brew2'

    event_load_again.name = 'new_test_name'
    event_load_again.update()

    event_load_second_time = Event(None, 'new_test_name')
    assert event_load_second_time.id == event_load_again.id


@patch('src.data_model.orm_mapper.Base.get_by_id')
def test_serialize(mock_event):
    event_table = EventTable('test_name', 'test_host', datetime.date(2021, 6, 21))
    event_table.id = 1
    beer1 = BeerTable('beer1', 'brew1', 'ch')
    beer2 = BeerTable('beer2', 'brew2', 'd')
    event_table.add_beer(beer1)
    event_table.add_beer(beer2)

    mock_event.return_value = event_table
    with patch.object(BeerTable, 'get_beer_by_event', return_value=[beer1, beer2]):
        event = Event(1)

    dump = event.serialize()

    assert search("'name': 'test_name'", str(dump))
    assert search("'host': 'test_host'", str(dump))
    assert search("'date': '2021-06-21'", str(dump))
