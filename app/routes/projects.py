from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.deps import get_db
from app.schemas.project import ProjectCreate
from app.services.project_service import create_project_service, get_projects_service
from app.core.auth import get_current_user
from app.schemas.project import ProjectResponse
router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("/", response_model=list[ProjectResponse])
def get_projects(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return get_projects_service(db, user)

@router.post("/")
def create_project(
    data: ProjectCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return create_project_service(db, data, user)