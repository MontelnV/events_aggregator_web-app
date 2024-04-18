from fastapi import Request, status, HTTPException
from fastapi.responses import RedirectResponse



def check_authentication(request: Request):
    session_token = request.cookies.get("session_token")
    if session_token is None or session_token != "Dy8HcAVc05afGsbP4wOF6fRJsoghkju1b49rljExFoQh0f0f8qZ75lw2ymXPKhux":
        return False
    return True

async def get_user(request: Request) -> str:
    if not check_authentication(request):
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            headers={'location': '/events/login'})
        # return RedirectResponse(url="/events/login", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return request.cookies.get("session_token")