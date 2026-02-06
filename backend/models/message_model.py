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

