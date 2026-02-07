from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from backend.database import engine
from backend.models.table_model import Base

from backend.controllers.message_controller import MessageController
from backend.models.message_model import MessageModel

Base.metadata.create_all(bind=engine)


app = FastAPI()

BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR.parent / "frontend" / "static"
TEMPLATE_DIR = BASE_DIR.parent / "frontend" / "templates"

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", include_in_schema=False)
async def index(request: Request):
    return FileResponse(TEMPLATE_DIR / "index.html", media_type="text/html")


@app.post("/messages")
async def post_message(
    request: Request,
    username: str = Form(None),
    content: str = Form(None),
    image: UploadFile = File(None),
):
    return await MessageController.create_message(request, username, content, image)


@app.get("/messages")
async def get_message(request: Request):
    return await MessageModel.get_messages()


import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    dbname=os.getenv("POSTGRES_DB"),
)
print("Connected!", conn)
