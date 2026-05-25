import secrets
from app.models.project import Project

def generate_key():
    return secrets.token_hex(32)

def create_project_service(db, data, user):
    project = Project(
        name=data.name,
        user_id=user.id,
        api_key=generate_key()
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project

def get_projects_service(db, user):
    return db.query(Project).filter(
        Project.user_id == user.id
    ).all()