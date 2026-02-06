from fastapi import FastAPI, UploadFile, File, Form, Request
from sqlalchemy.orm import Session
import os
import shutil

from database import SessionLocal, engine
from models.table_model import Base, Message
from config import PHOTO_DIR

from controllers.message_controller import MessageController

Base.metadata.creat_all(bind=engine)

app = FastAPI()

os.makedirs(PHOTO_DIR, exist_ok=True)


@app.post("/message")
async def post_message(
    request: Request,
    username: str = Form(None),
    content: str = Form(None),
    image: UploadFile = File(None),
):
    return await MessageController.create_message(request, username, content, image)
