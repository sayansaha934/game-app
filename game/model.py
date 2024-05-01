
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from db import Base

class Game(Base):
    __tablename__ = "game"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    status = Column(String, default="published")
    name = Column(String)
    url = Column(String)
    author= Column(String)
    published_date = Column(DateTime, default=datetime.utcnow)
