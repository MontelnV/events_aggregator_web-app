from app.database import new_session, EventsORM
from app.schemas import EventAdd
from sqlalchemy import select
from fastapi import HTTPException
from datetime import datetime

class EventRepository:

    @classmethod
    async def add_event(cls, data: EventAdd):
        async with new_session() as session:
            event_dict = data.model_dump()
            event = EventsORM(**event_dict)
            session.add(event)
            await session.flush()
            await session.commit()
            return event.id

    @classmethod
    async def get_events(cls, show_all: bool = False):
        async with new_session() as session:
            query = select(EventsORM)
            if not show_all:
                query = query.where(EventsORM.event_date >= datetime.now())  # Проверка на актуальность по дате
            result = await session.execute(query)
            events = result.scalars().all()
            if not events:
                return "Events not found"
            return events

    @classmethod
    async def get_event_by_id(cls, event_id):
        async with new_session() as session:
            query = select(EventsORM).where(EventsORM.id == event_id)
            result = await session.execute(query)
            event = result.scalars().first()
            if event is None:
                return "Event not found"
            return event

    @classmethod
    async def update_event(cls, event_id, data: EventAdd):
        async with new_session() as session:
            query = select(EventsORM).where(EventsORM.id == event_id)
            result = await session.execute(query)
            event = result.scalars().first()
            if event is None:
                raise HTTPException(status_code=404, detail="Event not found")
            event_data = data.model_dump()
            for key, value in event_data.items():
                setattr(event, key, value)
            await session.commit()

    @classmethod
    async def delete_event(cls, event_id):
        async with new_session() as session:
            query = select(EventsORM).where(EventsORM.id == event_id)
            result = await session.execute(query)
            event = result.scalars().first()
            if event is None:
                raise HTTPException(status_code=404, detail="Event not found")
            await session.delete(event)
            await session.commit()