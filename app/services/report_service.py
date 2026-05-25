from app.models.report import Report

def create_report(db, data, project):
    report = Report(
        type=data.type,

        device=data.device,
        android_version=data.android_version,

        rating=data.rating,
        improvement=data.improvement,
        easy_to_use=data.easy_to_use,

        screen=data.screen,
        problem=data.problem,
        steps=data.steps,

        project_id=project.id
    )

    db.add(report)
    db.commit()
    db.refresh(report)

    return {
        "message": "Reporte guardado",
        "id": report.id,
        "project": project.name
    } 