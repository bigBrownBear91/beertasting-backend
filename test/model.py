import pytest
from datetime import date

from src.data_model.model import Event, Beer


def test_adding_beer_to_event():
    event = Event('name', 'host', date(2021, 6, 21))
    beer = Beer('beername', 'brewery', 'ch')

    assert len(event.beers) == 0
    event.add_beer(beer)
    assert len(event.beers) == 1
    assert event.beers[0] == beer
