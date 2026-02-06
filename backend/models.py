from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from database import Base

class Message(Base):
    _tablename_ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    content = Column(String)
    image_url = Column(String)
    created_at = Column(DateTime, default=datetime.now)