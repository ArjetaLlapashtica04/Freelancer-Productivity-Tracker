from sqlalchemy.orm import Session
from . import models
import datetime
import csv
from io import StringIO

def calculate_total_hours(time_entry: models.TimeEntry) -> float:
    """Calculates the duration of a single time entry in hours."""
    if time_entry.start_time and time_entry.end_time:
        duration = time_entry.end_time - time_entry.start_time
        return duration.total_seconds() / 3600
    return 0.0

def calculate_payment(time_entry: models.TimeEntry) -> float:
    """Calculates the total payment for a time entry."""
    hours_worked = calculate_total_hours(time_entry)
    if time_entry.task:
        return hours_worked * time_entry.task.hourly_rate
    return 0.0

def generate_csv_report(db: Session, year: int, month: int):
    """
    Generates a CSV report with monthly time entries, payments, and totals.

    Args:
        db (Session): The database session.
        year (int): The year for the report.
        month (int): The month for the report.
    """
    # Define the start and end dates for the month
    start_date = datetime.datetime(year, month, 1)
    end_date = (start_date.replace(day=28) + datetime.timedelta(days=4)).replace(day=1) - datetime.timedelta(days=1)
    
    # Query all TimeEntry records for the specified month
    time_entries = db.query(models.TimeEntry).filter(
        models.TimeEntry.start_time >= start_date,
        models.TimeEntry.start_time <= end_date
    ).all()
    
    if not time_entries:
        return "No data found for this month."

    # Use StringIO to create an in-memory file for the CSV
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Project', 'Task Description', 'Hours Worked', 'Hourly Rate (€)', 'Total Payment (€)'])
    
    total_payment = 0.0
    for entry in time_entries:
        # Check if the task relationship is loaded
        if entry.task and entry.task.project:
            hours_worked = calculate_total_hours(entry)
            payment = calculate_payment(entry)
            total_payment += payment
            
            writer.writerow([
                entry.task.project.name,
                entry.task.title,
                f"{hours_worked:.2f}",
                f"{entry.task.hourly_rate:.2f}",
                f"{payment:.2f}"
            ])
    
    
    writer.writerow(['', '', '', 'TOTAL', f"{total_payment:.2f}"])
    
    # Return the string value of the CSV file
    return output.getvalue()
