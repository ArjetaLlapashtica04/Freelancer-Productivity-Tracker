from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from . import models, schemas, reports
from .database import SessionLocal, engine
import datetime


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint for the root path
@app.get("/")
def read_root():
    return {"message": "Welcome to the Productivity Tracker API!"}

# Endpoint to create a new project
@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# Endpoint to create a new task
@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Endpoint to create a new time entry
@app.post("/time-entries/", response_model=schemas.TimeEntry)
def create_time_entry(entry: schemas.TimeEntryCreate, db: Session = Depends(get_db)):
    # You could add logic here to calculate hours_worked before adding to DB
    # For now, we'll use the value from the Pydantic schema
    db_entry = models.TimeEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


# Endpoint to get the CSV report
@app.get("/reports/csv", response_class=Response)
def get_monthly_report(year: int, month: int, db: Session = Depends(get_db)):
    report_content = reports.generate_csv_report(db, year, month)
    
    if report_content == "No data found for this month.":
        raise HTTPException(status_code=404, detail=report_content)
    
    # Return the CSV content with the correct media type
    return Response(
        content=report_content, 
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=report_{year}_{month}.csv"
        }
    )
