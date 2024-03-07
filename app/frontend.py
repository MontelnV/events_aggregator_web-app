from __future__ import annotations as _annotations
from fastapi import APIRouter, Depends
from typing import Annotated
import json
from fastapi.responses import HTMLResponse
from app.database import EventsORM
from app.schemas import Event, EventAdd, Auth
from app.repositories import EventRepository
from fastapi import APIRouter
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from fastui.components.display import DisplayLookup, DisplayMode
from fastui.events import GoToEvent, BackEvent
from app.database import new_session
from sqlalchemy import select
from contextlib import asynccontextmanager
from datetime import datetime

router = APIRouter(
    tags=["Frontend"],
)
#FAST UI
@router.get('/api/', response_model=FastUI, response_model_exclude_none=True)
async def main_page() -> list[AnyComponent]:
    async with new_session() as session:
        query = select(EventsORM)
        result = await session.execute(query)
        data = result.scalars().all()
        event_dicts = [{column.name: getattr(event, column.name) for column in EventsORM.__table__.columns}
                       for event in data]
        events = [EventAdd(**event_dict) for event_dict in event_dicts]

    return [
        c.Page(
            components=[
                c.Button(text="Личный кабинет администратора", on_click=GoToEvent(url='/admin')),
                c.PageTitle(text="Главная страница"),
                c.Heading(text="Агрегатор мероприятий", level=1),
                c.Table(
                    data=events,
                    columns=[
                        DisplayLookup(title='Название', field="title", table_width_percent=5),
                        DisplayLookup(title='Описание', field="description", table_width_percent=50),
                        DisplayLookup(title='Организатор', field="organizer"),
                        DisplayLookup(title='Дата события', field="event_date", table_width_percent=5),
                        DisplayLookup(title='Время закрытия регистрации', field="registration_close_datetime"),
                        DisplayLookup(title='Место проведения', field="location"),
                        DisplayLookup(title='Ссылка на регистрацию', field="registration_link", table_width_percent=10),
                    ]
                ),
            ]
        )
    ]

@router.get('/api/admin', response_model=FastUI, response_model_exclude_none=True)
async def main_page() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                c.Button(text="Вернуться назад", on_click=BackEvent()),
                c.PageTitle(text="ЛК"),
                c.Heading(text="Вход в личный кабинет", level=1),
                c.ModelForm(
                    model=Auth,
                    submit_url="/api/user"
                )

            ]
        )
    ]
#без следующей функции ничего не билдится, важная оч
@router.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    return HTMLResponse(prebuilt_html())