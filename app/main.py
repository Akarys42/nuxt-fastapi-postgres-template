from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.constants import DATABASE_URL

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)  # Remember to tailor the CORS policies to your use case!

engine = create_async_engine(DATABASE_URL)
Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


@app.get("/")
async def root() -> list:
    """Placeholder root endpoint."""
    async with Session() as session:
        database_version = next(await session.execute(text("SELECT VERSION();")))[0]

    return [
        {"id": 1, "content": "Post 1"},
        {"id": 2, "content": "Post 2"},
        {"id": 3, "content": f"Using {database_version}"},
    ]
