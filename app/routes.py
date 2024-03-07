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
from datetime import datetime

router = APIRouter(
    tags=["Events"],
    prefix='/api/v1'# добавляем тег для отображения в Swagger UI
)

@router.post("/events")
async def create_task(event: EventAdd):
    event = await EventRepository.add_event(event)
    return {"task_id": event}

@router.get("/events")
async def get_tasks(showAll: bool = False):
    events = await EventRepository.get_events(showAll)
    return {"events": events}

@router.get("/events/{event_id}")
async def get_task(event_id: int):
    event = await EventRepository.get_event_by_id(event_id)
    return {"event": event}

@router.put("/events/{event_id}")
async def update_task(event_id: int, event: EventAdd):
    result = await EventRepository.update_event(event_id, event)
    return {"message": result}

@router.delete("/events/{event_id}")
async def delete_task(event_id: int):
    result = await EventRepository.delete_event(event_id)
    return {"message": result}
