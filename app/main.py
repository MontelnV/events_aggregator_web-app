from fastapi import FastAPI
from app.database import create_tables, drop_tables
from contextlib import asynccontextmanager

from app.routes import router as event_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    #await drop_tables()
    print("tables dropped")
    #await create_tables()
    #print("tables created")
    yield
    print("App OFF")

app = FastAPI(lifespan=lifespan)
app.include_router(event_router)