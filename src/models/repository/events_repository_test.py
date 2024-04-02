from .events_repository import EventsRepository
from src.models.settings.connection import db_connection_handler
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_events():
    
    event = {
        "uuid":  "meu_uuid2",
        "title": "meu title",
        "slug": "meu_slug2",
        "maximum_attendees": 20
    }

    event_repository = EventsRepository()
    response = event_repository.insert_event(event)
    print(response)

def test_get_event_by_id():
    event_id = "meu_uuid2"
    event_repository = EventsRepository()
    response = event_repository.get_event_by_id(event_id=event_id)

    print(response)
    