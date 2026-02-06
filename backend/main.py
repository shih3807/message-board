from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import FileResponse
import os

from database import engine
from models.table_model import Base
from config import PHOTO_DIR

from controllers.message_controller import MessageController
from models.message_model import MessageModel

Base.metadata.creat_all(bind=engine)

app = FastAPI()

os.makedirs(PHOTO_DIR, exist_ok=True)


@app.get("/", include_in_schema=False)
async def index(request: Request):
    return FileResponse("../fontend/templates/index.html", media_type="text/html")



@app.post("/message")
async def post_message(
    request: Request,
    username: str = Form(None),
    content: str = Form(None),
    image: UploadFile = File(None),
):
    return await MessageController.create_message(request, username, content, image)

@app.get("/message")
async def get_message(request: Request):
    return await MessageModel.get_messages()