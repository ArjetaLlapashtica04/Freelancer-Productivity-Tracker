# app/schemas.py
from pydantic import BaseModel
from typing import Optional
import datetime

# Schema for creating a Project
# It doesn't need an 'id' since the database will generate it.
class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None

# Schema for reading a Project
# It includes the 'id' and a way to read from SQLAlchemy models.
class Project(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True # Enables Pydantic to work with SQLAlchemy models

# Schema for creating a Task
class TaskCreate(BaseModel):
    title: str
    hourly_rate: float
    project_id: int

# Schema for reading a Task
class Task(BaseModel):
    id: int
    title: str
    hourly_rate: float
    project_id: int
    
    class Config:
        orm_mode = True

# Schema for creating a TimeEntry
class TimeEntryCreate(BaseModel):
    start_time: datetime.datetime
    end_time: Optional[datetime.datetime] = None
    task_id: int
    hours_worked: Optional[float] = 0.0

# Schema for reading a TimeEntry
class TimeEntry(BaseModel):
    id: int
    start_time: datetime.datetime
    end_time: Optional[datetime.datetime] = None
    hours_worked: float
    task_id: int

    class Config:
        orm_mode = True