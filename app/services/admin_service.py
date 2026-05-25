from app.models.report import Report

def get_reports(db, project_id):
    return db.query(Report).filter(
        Report.project_id == project_id
    ).all()