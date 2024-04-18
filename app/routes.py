from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from app.schemas import EventAdd
from app.repositories import EventRepository
from fastapi.responses import RedirectResponse
from fastapi import FastAPI, Request, Depends, Form, status
from typing import Optional
from datetime import datetime


router = APIRouter(
    tags=["Events"]  # добавляем тег для отображения в Swagger UI
)


@router.post("/api/events")
async def create_event(request: Request, title: str = Form(...),
                       tag: str = Form(None), organizer: str = Form(None),
                       event_date: datetime = Form(...), registration_close_datetime: datetime = Form(None),
                       location: str = Form(None), registration_link: str = Form(None), description: str = Form(None)):
    event = EventAdd(title=title, tag=tag, organizer=organizer, event_date=event_date,
                     registration_close_datetime=registration_close_datetime, location=location,
                     registration_link=registration_link, description=description)

    await EventRepository.add_event(event)
    return RedirectResponse(url="/events/admin?showAll=True", status_code=status.HTTP_303_SEE_OTHER)

@router.post("/api/events/{event_id}")
async def update_event(request: Request, event_id: int, title: str = Form(...),
                       tag: str = Form(None), organizer: str = Form(None),
                       event_date: datetime = Form(...), registration_close_datetime: datetime = Form(None),
                       location: str = Form(None), registration_link: str = Form(None), description: str = Form(None)):

    event = EventAdd(title=title, tag=tag, organizer=organizer, event_date=event_date,
                     registration_close_datetime=registration_close_datetime, location=location,
                     registration_link=registration_link, description=description)
    await EventRepository.update_event(event_id, event)
    return RedirectResponse(url="/events/admin?showAll=True", status_code=status.HTTP_303_SEE_OTHER)

@router.delete("/api/events/{event_id}")
async def delete_event(event_id: int):
    result = await EventRepository.delete_event(event_id)
    return {"message": result}

@router.get("/api/events")
async def get_events(showAll: bool = False):
    events = await EventRepository.get_events(showAll)
    return {"events": events}

@router.get("/api/events/{event_id}")
async def get_events_by_id(event_id: int):
    event = await EventRepository.get_event_by_id(event_id)
    return {"event": event}