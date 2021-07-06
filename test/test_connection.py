import pytest
import datetime

from src.data_model.orm_mapper import EventTable
from test.set_up import test_db


def test_connection_and_creating_and_querying_by_name(test_db):
    retrieved_value = EventTable.get_by_name('test_name')

    assert 'test_name' == retrieved_value.name
    assert 'test_host' == retrieved_value.host
    assert datetime.date(2021, 6, 21) == retrieved_value.date


def test_update(test_db):
    corrected_date = datetime.date(2021, 7, 1)
    retrieved_value = EventTable.get_by_name('test_name')
    retrieved_value.host = 'corrected_host'
    retrieved_value.date = corrected_date
    retrieved_value.create_or_update()

    expected_value = EventTable.get_by_name('test_name')
    assert 'corrected_host' == expected_value.host
    assert corrected_date == expected_value.date
