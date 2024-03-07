from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class EventAdd(BaseModel):

    title: str
    description: Optional[str] = None
    organizer: str
    event_date: str
    registration_close_datetime: str
    location: str
    registration_link: Optional[str] = None

class Event(EventAdd):

    id: int
    model_config = ConfigDict(from_attributes=True)