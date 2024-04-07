from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import create_tables, drop_tables
from contextlib import asynccontextmanager
from app.routes import router as event_router
from app.frontend import router as frontend_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    #await drop_tables()
    #await create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.mount("/static/", StaticFiles(directory="static"), name="static")
app.include_router(event_router)
app.include_router(frontend_router)