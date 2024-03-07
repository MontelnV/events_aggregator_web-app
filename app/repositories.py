from app.database import new_session, EventsORM
from app.schemas import EventAdd
from sqlalchemy import select
from fastapi import HTTPException


class EventRepository:

    @classmethod
    async def add_event(cls, data: EventAdd):
        async with new_session() as session:
            event_dict = data.model_dump()
            event = EventsORM(**event_dict)
            session.add(event)
            await session.commit()

    @classmethod
    async def get_events(cls):
        async with new_session() as session:
            query = select(EventsORM)
            result = await session.execute(query)
            event_models = result.scalars().all()
            if event_models is None:
                return "Event not found"
            return event_models

    @classmethod
    async def get_event_by_id(cls, event_id):
        async with new_session() as session:
            query = select(EventsORM).where(EventsORM.id == event_id)
            result = await session.execute(query)
            event = result.scalars().first()
            if event is None:
                return "Event not found"
            return event