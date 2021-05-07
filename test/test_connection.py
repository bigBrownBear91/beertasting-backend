import pytest
import os
import datetime
from pathlib import Path

from src.data_model.model import Event


@pytest.fixture(scope='module')
def test_db():
    Path('testDb.db').touch()
    yield 'testDb.db'
    os.remove('testDb.db')


def test_connection(test_db):
    test_date = datetime.date(2021, 6, 21)
    test_event = Event('test_name', 'test_host', test_date)
    test_event.create_or_update()
    retrieved_value = Event.get_by_name('test_name')

    assert 'test_name' == retrieved_value.name
    assert 'test_host' == retrieved_value.host
    assert test_date == retrieved_value.date
