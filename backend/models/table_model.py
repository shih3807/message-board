from sqlalchemy import Column, String, Integer, DateTime, func
from datetime import datetime, timezone
from backend.database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True)
    content = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())