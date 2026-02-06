from fastapi import FastAPI, UploadFile, File, Form
from sqlalchemy.orm import Session
import os
import shutil

from database import SessionLocal, engine
from models import Base, Message

Base.metadata.creat_all(bind=engine)

app = FastAPI()

PHOTO = "photo"
os.makedirs(PHOTO, exist_ok = True)

@app.post("/message")
async def create_message(
    username:str = Form(None),
    content:str=Form(None),
    image: UploadFile=File(None)
):
    if not username and content and image:
        return {"error":True, "msg":"content is empty"}
    
    db:Session = SessionLocal()

    if image :
        try:
            file_path = f"{PHOTO}/{image.filename}"
            with open(file_path,"wb") as pic:
                shutil.copyfileobj(image.file, pic)

                msg = Message(
                    username=username,
                    content= content,
                    image_url=file_path
                )
                db.add(msg)
                db.commit()
                db.close()

                return{"success":True, "msg":"message created"}
        except Exception as e :
            return {"error":True, "msg":e}