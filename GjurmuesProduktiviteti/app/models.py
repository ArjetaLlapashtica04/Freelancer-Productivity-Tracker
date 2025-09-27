from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    
    # This relationship links Project to Task
    tasks = relationship("Task", back_populates="project")

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    hourly_rate = Column(Float, default=0.0)
    project_id = Column(Integer, ForeignKey("projects.id"))
    
    # These relationships link Task to Project and TimeEntry
    project = relationship("Project", back_populates="tasks")
    time_entries = relationship("TimeEntry", back_populates="task")

class TimeEntry(Base):
    __tablename__ = "time_entries"
    
    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(DateTime, default=datetime.datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    hours_worked = Column(Float, default=0.0)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    
    # This relationship links TimeEntry to Task
    task = relationship("Task", back_populates="time_entries")
