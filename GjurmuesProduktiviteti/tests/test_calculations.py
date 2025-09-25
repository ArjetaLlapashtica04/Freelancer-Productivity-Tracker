import sys
import os

# Kjo ndihmon Python të gjejë modulet tona në file 'app'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models import Task

def test_payment_calculation():
    """Teston llogaritjen e pagesës për një detyrë me kohëzgjatje 2.5 orë."""
    task = Task(
        id=1,
        description="Test task",
        start_time="2025-09-20T10:00:00",
        end_time="2025-09-20T12:30:00",
        hourly_rate=20.0
    )
    expected_payment = 50.0
    assert task.calculate_payment() == expected_payment

def test_zero_duration_payment():
    """Teston rastin kur pagesa duhet të jetë zero (kohëzgjatje zero)."""
    task = Task(
        id=1,
        description="Test task",
        start_time="2025-09-20T10:00:00",
        end_time="2025-09-20T10:00:00",
        hourly_rate=20.0
    )
    assert task.calculate_payment() == 0.0