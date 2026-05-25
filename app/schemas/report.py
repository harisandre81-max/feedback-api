from pydantic import BaseModel
from enum import Enum
from typing import Optional

class ReportType(str, Enum):
    opinion = "opinion"
    bug = "bug"
    suggestion = "suggestion"


# -------------------------
# CREAR REPORTE
# -------------------------
class ReportCreate(BaseModel):

    type: ReportType

    # generales
    device: str
    android_version: str

    # opinion
    rating: Optional[int] = None
    improvement: Optional[str] = None
    easy_to_use: Optional[bool] = None

    # bug
    screen: Optional[str] = None
    problem: Optional[str] = None
    steps: Optional[str] = None


# -------------------------
# RESPUESTA
# -------------------------
class ReportResponse(BaseModel):
    id: int
    type: ReportType
    message: str

    class Config:
        from_attributes = True #Pydantic v2