import csv
from . import database
from .models import Task

def generate_csv_report(year, month, filename="report.csv"):
    """Gjeneron një raport CSV me detyrat e një muaji."""
    tasks_data = database.get_tasks_for_month(year, month)
    if not tasks_data:
        print("Nuk ka të dhëna për këtë muaj.")
        return

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Shkruajmë header-in
        writer.writerow(['Përshkrimi', 'Kohëzgjatja (orë)', 'Pagesa për Orë (€)', 'Pagesa Totale (€)'])
        
        total_payment = 0
        for row in tasks_data:
            task = Task(**dict(row))
            duration = task.calculate_duration_hours()
            payment = task.calculate_payment()
            total_payment += payment
            writer.writerow([task.description, f"{duration:.2f}", task.hourly_rate, f"{payment:.2f}"])
        
        # Shkruajmë rreshtin e totalit
        writer.writerow(['', '', 'TOTALI', f"{total_payment:.2f}"])
    print(f"Raporti CSV u ruajt si '{filename}'")