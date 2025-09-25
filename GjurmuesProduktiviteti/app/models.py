import datetime

class Task:
    def __init__(self, id, description, start_time, end_time, hourly_rate):
        self.id = id
        self.description = description
        self.start_time = datetime.datetime.fromisoformat(start_time)
        self.end_time = datetime.datetime.fromisoformat(end_time)
        self.hourly_rate = hourly_rate

    def calculate_duration_hours(self):
        """Llogarit kohëzgjatjen e detyrës në orë."""
        if self.end_time and self.start_time:
            duration = self.end_time - self.start_time
            return duration.total_seconds() / 3600
        return 0

    def calculate_payment(self):
        """Llogarit pagesën totale bazuar në kohëzgjatjen dhe tarifën për orë."""
        return self.calculate_duration_hours() * self.hourly_rate