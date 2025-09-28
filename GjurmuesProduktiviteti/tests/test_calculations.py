import datetime
import pytest

# We need to import the calculation functions from our reports module
from app.reports import calculate_total_hours, calculate_payment

# Since our tests don't connect to a real database, we'll create simple
# mock objects that mimic the structure of our SQLAlchemy models.
class MockTimeEntry:
    def __init__(self, start_time, end_time, hourly_rate):
        self.start_time = start_time
        self.end_time = end_time
        
        self.task = MockTask(hourly_rate)

class MockTask:
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate


def test_calculate_total_hours():
    """Tests the duration calculation function with a known time span."""
    start = datetime.datetime(2025, 9, 20, 10, 0, 0)
    end = datetime.datetime(2025, 9, 20, 12, 30, 0)
    mock_entry = MockTimeEntry(start, end, 20.0)
    
    # We expect 2.5 hours
    expected_hours = 2.5
    assert calculate_total_hours(mock_entry) == expected_hours


def test_calculate_payment():
    """Tests the payment calculation function with a known duration and rate."""
    start = datetime.datetime(2025, 9, 20, 10, 0, 0)
    end = datetime.datetime(2025, 9, 20, 12, 30, 0)
    mock_entry = MockTimeEntry(start, end, 20.0)
    
    # Calculation: 2.5 hours * 20.0 per hour = 50.0
    expected_payment = 50.0
    assert calculate_payment(mock_entry) == expected_payment


def test_zero_duration_payment():
    """Tests the payment calculation when the duration is zero."""
    start = datetime.datetime(2025, 9, 20, 10, 0, 0)
    end = datetime.datetime(2025, 9, 20, 10, 0, 0)
    mock_entry = MockTimeEntry(start, end, 20.0)

    assert calculate_payment(mock_entry) == 0.0
