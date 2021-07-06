import datetime

from src.data_model.model import Event
from test.set_up import test_db


def test_event(test_db):
    event_load_again = Event(None, 'test_name')
    assert event_load_again.host == 'test_host'
    assert event_load_again.get_beer_by_name('beer3').brewery == 'brew2'

    event_load_again.name = 'new_test_name'
    event_load_again.update()

    event_load_second_time = Event(None, 'new_test_name')
    assert event_load_second_time.id == event_load_again.id
