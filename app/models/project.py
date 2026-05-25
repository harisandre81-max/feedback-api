from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.database.base import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    api_key = Column(String, unique=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))  

    created_at = Column(DateTime, default=datetime.utcnow)    