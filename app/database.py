from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

engine = create_async_engine(
    "sqlite+aiosqlite:///events.db"
)
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class EventsORM(Base):
    __tablename__ = "events"


    id: Mapped[int] = mapped_column(primary_key=True)
    tag: Mapped[str | None]
    title: Mapped[str]
    description: Mapped[str | None]
    organizer: Mapped[str]
    event_date: Mapped[datetime]
    registration_close_datetime: Mapped[datetime]
    location: Mapped[str]
    registration_link: Mapped[str | None]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)