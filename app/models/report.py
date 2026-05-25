from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database.base import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)

    type = Column(String)

    # generales
    device = Column(String)
    android_version = Column(String)

    # opinion
    rating = Column(Integer, nullable=True)
    improvement = Column(String, nullable=True)
    easy_to_use = Column(Boolean, nullable=True)

    # bug
    screen = Column(String, nullable=True)
    problem = Column(String, nullable=True)
    steps = Column(String, nullable=True)

    # proyecto
    project_id = Column(Integer, ForeignKey("projects.id"))