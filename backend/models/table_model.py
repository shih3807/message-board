from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from database import Base

class Message(Base):
    _tablename_ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True)
    content = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now)