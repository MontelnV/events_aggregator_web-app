from fastapi import APIRouter, Request, status, Depends
from typing import Annotated
from fastapi.templating import Jinja2Templates
from app.repositories import EventRepository
from fastapi.responses import RedirectResponse
from app.deps import get_user

router = APIRouter(
    prefix="/events",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def login_page(request: Request, showAll: bool = False):
    events = await EventRepository.get_events(showAll)
    return templates.TemplateResponse("index.html", {"request": request, "events": events})

@router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/admin")
async def home(request: Request, admin: Annotated[str, Depends(get_user)], showAll: bool = False):
    events = await EventRepository.get_events(showAll)
    return templates.TemplateResponse("admin.html", {"request": request, "events": events})

@router.get("/admin/addnew")
async def addnew(request: Request, admin: Annotated[str, Depends(get_user)]):
    return templates.TemplateResponse("addnew.html", {"request": request})

@router.get("/admin/edit/{event_id}")
async def edit(request: Request, admin: Annotated[str, Depends(get_user)], event_id: int):
    event = await EventRepository.get_event_by_id(event_id)
    return templates.TemplateResponse("edit.html", {"request": request, "event": event})

@router.get("/admin/delete/{event_id}")
async def delete(request: Request, admin: Annotated[str, Depends(get_user)], event_id: int):
    await EventRepository.delete_event(event_id)
    return RedirectResponse(url="/events/admin?showAll=True", status_code=status.HTTP_303_SEE_OTHER)