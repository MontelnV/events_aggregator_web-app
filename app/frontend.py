from fastapi import APIRouter, FastAPI, Request, status
from typing import Optional
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.repositories import EventRepository
from app.schemas import EventAdd
from app.database import EventsORM, new_session
from sqlalchemy import select
from fastapi.responses import RedirectResponse


router = APIRouter(
    prefix="/events",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")

def check_authentication(request: Request):
    session_token = request.cookies.get("session_token")
    if session_token is None or session_token != "Dy8HcAVc05afGsbP4wOF6fRJsWR0Wju1b49rljExFoQh0f0f8qZ75lw2ymXPKhux":
        return False
    return True

@router.get("/")
async def login_page(request: Request, showAll: bool = False):
    events = await EventRepository.get_events(showAll)
    return templates.TemplateResponse("index.html", {"request": request, "events": events})

@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/admin")
async def home(request: Request, showAll: bool = False):
    if not check_authentication(request):
        return RedirectResponse(url="/events/login", status_code=status.HTTP_303_SEE_OTHER)

    events = await EventRepository.get_events(showAll)
    return templates.TemplateResponse("index.html", {"request": request, "events": events})

@router.get("/admin/addnew")
async def addnew(request: Request):
    if not check_authentication(request):
        return RedirectResponse(url="/events/login", status_code=status.HTTP_303_SEE_OTHER)

    return templates.TemplateResponse("addnew.html", {"request": request})

@router.get("/admin/edit/{event_id}")
async def edit(request: Request, event_id: int):
    if not check_authentication(request):
        return RedirectResponse(url="/events/login", status_code=status.HTTP_303_SEE_OTHER)

    event = await EventRepository.get_event_by_id(event_id)
    return templates.TemplateResponse("edit.html", {"request": request, "event": event})

@router.get("/admin/delete/{event_id}")
async def delete(request: Request, event_id: int):
    if not check_authentication(request):
        return RedirectResponse(url="/events/login", status_code=status.HTTP_303_SEE_OTHER)

    await EventRepository.delete_event(event_id)
    return RedirectResponse(url="/events/admin?showAll=True", status_code=status.HTTP_303_SEE_OTHER)