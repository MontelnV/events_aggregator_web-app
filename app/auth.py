from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi import Request, Form, status

router = APIRouter(
    tags=["Auth"]
)

@router.post("/events/login")
async def admin_login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "admin":
        response = RedirectResponse(url="/events/admin", status_code=status.HTTP_302_FOUND)
        response.set_cookie(key="session_token", value="Dy8HcAVc05afGsbP4wOF6fRJsoghkju1b49rljExFoQh0f0f8qZ75lw2ymXPKhux")
        return response
    else:
        return RedirectResponse(url="/events/login", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/events/admin/logout")
async def admin_logout(request: Request):
    response = RedirectResponse(url="/events/login", status_code=status.HTTP_302_FOUND)
    response.delete_cookie("session_token")  # Удаление сессионного токена из cookies
    return response