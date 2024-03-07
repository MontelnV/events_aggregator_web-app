from pydantic import BaseModel, ConfigDict, HttpUrl
from typing import Optional
from datetime import datetime


class EventAdd(BaseModel):

    tag: Optional[str] = None
    title: str
    description: Optional[str] = None
    organizer: Optional[str] = None
    event_date: datetime
    registration_close_datetime: Optional[datetime] = None
    location: Optional[str] = None
    registration_link: Optional[str] = None

class Event(EventAdd):

    id: int
    model_config = ConfigDict(from_attributes=True)

class Auth(BaseModel):

    username: str
    password: str