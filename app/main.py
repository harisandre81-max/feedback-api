from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import engine
from app.database.base import Base

# importar modelos
from app.models.user import User
from app.models.project import Project
from app.models.report import Report

# importar rutas
from app.routes import reports, admin, projects, auth

# crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FeedbackSDK API",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# rutas
app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(reports.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {
        "message": "FeedbackSDK API funcionando"
    }

@app.get("/healthz")
def health():
    return {"status": "ok"}    