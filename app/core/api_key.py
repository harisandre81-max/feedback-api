from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.deps import get_db
from app.models.project import Project

def get_project_by_api_key(
    api_key: str = Header(..., alias="x-api-key"),
    db: Session = Depends(get_db)
):
    if not api_key:
        raise HTTPException(401, "API key missing")

    project = db.query(Project).filter_by(api_key=api_key).first()

    if not project:
        raise HTTPException(401, "Invalid API key")

    return project