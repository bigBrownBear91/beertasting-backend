import pytest
from datetime import date

from src.data_model.orm_mapper import EventTable, BeerTable
from test.set_up import test_db


def test_adding_beer_to_event():
    event = EventTable('name', 'host', date(2021, 6, 21))
    beer = BeerTable('beername', 'brewery', 'ch')

    assert len(event.beers) == 0
    event.add_beer(beer)
    assert len(event.beers) == 1
    assert event.beers[0] == beer


def test_get_beers_by_event(test_db):
    event = EventTable('name', 'host', date(2021, 6, 21))
    event.add_beer(BeerTable('beer1', 'brew1', 'ch'))
    event.add_beer(BeerTable('beer2', 'brew2', 'ch'))
    event.add_beer(BeerTable('beer3', 'brew2', 'ch'))
    event.create_or_update()

    event_got_again = event.get_by_name('name')
    beers = BeerTable.get_beer_by_event(event_got_again.id)
    assert len(beers) == 3
    assert 'beer1' in [beer.name for beer in beers]
    assert 'beer3' in [beer.name for beer in beers]
    assert 'beer4' not in [beer.name for beer in beers]
    assert isinstance(beers[0], BeerTable)
    assert isinstance(beers[1], BeerTable)
    assert isinstance(beers[2], BeerTable)
