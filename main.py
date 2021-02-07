import datetime

from src.database import Session, Base, engine
from src.entities.event import Event
from src.entities.entity import Selector

session = Session()
Base.metadata.create_all(bind=engine)

name = 'me'
host = 'you'
date = datetime.date(2021, 6, 21)
new_event = Event(name, host, date)
new_event.create(session)


selected_event = Selector.select_by_id(session, 1, Event)
selected_event.name = 'him'

same_event_again_selected = Selector.select_by_id(session, 1, Event)
