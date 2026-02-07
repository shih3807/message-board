from sqlalchemy.orm import Session
from models.table_model import Message

from database import SessionLocal


class MessageModel:
    # 創建訊息
    @staticmethod
    def create_message(
        username: str | None = None,
        content: str | None = None,
        image_url: str | None = None,
    ):
        db: Session = SessionLocal()
        try:
            msg = Message(username=username, content=content, image_url=image_url)

            db.add(msg)
            db.commit()
            db.refresh(msg)

            return {"success": True}
        except Exception as e:
            return {"error": True, "msg": str(e)}
        finally:
            db.close()

    # 取得所有訊息
    @staticmethod
    async def get_messages():
        db: Session = SessionLocal()
        try:
            msgs = db.query(Message).order_by(Message.created_at.desc()).all()

            result = [
                {"username": m.username, "content": m.content, "image_url": m.image_url}
                for m in msgs
            ]
            return result
        except Exception as e:
            return {"error": True, "msg": str(e)}
        finally:
            db.close()
