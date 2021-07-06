import pytest
from pathlib import Path
import os
import datetime

from src.data_model.orm_mapper import EventTable, BeerTable


@pytest.fixture(scope='function')
def test_db():
    Path('testDb.db').touch()

    test_date = datetime.date(2021, 6, 21)
    test_event = EventTable('test_name', 'test_host', test_date)
    test_event.add_beer(BeerTable('beer1', 'brew1', 'ch'))
    test_event.add_beer(BeerTable('beer2', 'brew2', 'ch'))
    test_event.add_beer(BeerTable('beer3', 'brew2', 'ch'))
    test_event.create_or_update()

    yield 'testDb.db'
    os.remove('testDb.db')
