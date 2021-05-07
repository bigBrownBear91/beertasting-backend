import pytest
import os
import datetime
from pathlib import Path

from src.data_model.model import Event


@pytest.fixture(scope='function')
def test_db():
    Path('testDb.db').touch()
    yield 'testDb.db'
    os.remove('testDb.db')


def test_connection_and_creating_and_querying_by_name(test_db):
    test_date = datetime.date(2021, 6, 21)
    test_event = Event('test_name', 'test_host', test_date)
    test_event.create_or_update()
    retrieved_value = Event.get_by_name('test_name')

    assert 'test_name' == retrieved_value.name
    assert 'test_host' == retrieved_value.host
    assert test_date == retrieved_value.date


def test_update(test_db):
    test_date = datetime.date(2021, 6, 21)
    test_event = Event('test_name', 'test_host', test_date)
    test_event.create_or_update()

    corrected_date = datetime.date(2021, 7, 1)
    retrieved_value = Event.get_by_name('test_name')
    retrieved_value.host = 'corrected_host'
    retrieved_value.date = corrected_date
    retrieved_value.create_or_update()

    expected_value = Event.get_by_name('test_name')
    assert 'corrected_host' == expected_value.host
    assert corrected_date == expected_value.date
