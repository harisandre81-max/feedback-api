from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.core.api_key import get_project_by_api_key
from app.services.admin_service import get_reports

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/reports")
def get_project_reports(
    db: Session = Depends(get_db),
    project = Depends(get_project_by_api_key)
):
    reports = get_reports(db, project.id)

    return {
        "project": project.name,
        "reports": reports
    }