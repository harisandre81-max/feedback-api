from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.report import ReportCreate
from app.database.deps import get_db
from app.services.report_service import create_report
from app.core.api_key import get_project_by_api_key
from app.models.project import Project

router = APIRouter(prefix="/reports", tags=["reports"])

@router.post("/")
async def create_report_route(
    data: ReportCreate,
    db: Session = Depends(get_db),
    project: Project = Depends(get_project_by_api_key)
):
    return create_report(db, data, project)