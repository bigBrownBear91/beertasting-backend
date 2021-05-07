from datetime import datetime

from entities.entity import Selector
from entities.tables import Event, EventSchema
from database import Session

session = Session()

event = Selector(Event)
event.select_all(session)

schema = EventSchema(many=True)
jsonevent = schema.dump(event.result)
print(jsonevent)
