from __future__ import annotations as _annotations
from fastapi import APIRouter, Depends
from typing import Annotated
import json
from fastapi.responses import HTMLResponse
from app.database import EventsORM
from app.schemas import Event, EventAdd
from app.repositories import EventRepository
from fastapi import APIRouter
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from fastui.components.display import DisplayLookup, DisplayMode
from app.database import new_session
from sqlalchemy import select
from contextlib import asynccontextmanager

router = APIRouter(
    tags=["Events"]  # добавляем тег для отображения в Swagger UI
)

@router.post("/api/v1/events")
async def create_task(event: EventAdd):
    event = await EventRepository.add_event(event)
    return {"task_id": "Event created successfully"}

@router.get("/api/v1/events")
async def get_tasks():
    events = await EventRepository.get_events()
    return {"events": events}

@router.get("/api/v1/events/{event_id}")
async def get_task(event_id: int):
    event = await EventRepository.get_event_by_id(event_id)
    return {"event": event}


@router.get('/api/', response_model=FastUI, response_model_exclude_none=True)
async def main_page() -> list[AnyComponent]:
    async with new_session() as session:

        query = select(EventsORM)
        result = await session.execute(query)
        users = result.scalars().all()
    return [
        c.Page(
            components=[
                c.Button(text="Личный кабинет администратора"),
                c.PageTitle(text="Главная страница"),
                c.Heading(text="Агрегатор мероприятий", level=1),
                c.Table(
                    data=users,
                    columns=[
                        DisplayLookup(title='Название', field="title"),
                        DisplayLookup(title='Описание', field="description"),
                        DisplayLookup(title='Организатор', field="organizer"),
                        DisplayLookup(title='Дата события', field="event_date"),
                        DisplayLookup(title='Время закрытия регистрации', field="registration_close_datetime"),
                        DisplayLookup(title='Место проведения', field="location"),
                        DisplayLookup(title='Ссылка на регистрацию', field="registration_link"),
                    ]
                ),
            ]
        )
    ]

#без следующей функции ничего не билдится, важная оч
@router.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    return HTMLResponse(prebuilt_html())
