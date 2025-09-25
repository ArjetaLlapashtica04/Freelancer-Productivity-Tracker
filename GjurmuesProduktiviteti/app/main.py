import datetime
from . import database, reports
from .models import Task

def show_menu():
    """Paraqet menunë e opsioneve."""
    print("\n--- Gjurmuesi i Produktivitetit ---")
    print("1. Shto detyrë të re")
    print("2. Shiko detyrat për një muaj")
    print("3. Gjenero raport mujor (CSV)")
    print("4. Dil")
    return input("Zgjidhni një opsion: ")

def add_new_task_flow():
    """Procesi i shtimit të një detyre të re."""
    print("\n--- Shto Detyrë të Re ---")
    desc = input("Përshkrimi: ")
    start_str = input("Koha e fillimit (YYYY-MM-DD HH:MM): ")
    end_str = input("Koha e mbarimit (YYYY-MM-DD HH:MM): ")
    rate = float(input("Pagesa për orë (€): "))
    
    # Krijon një format datë-ore që SQLite e ruan si string
    start_iso = datetime.datetime.strptime(start_str, "%Y-%m-%d %H:%M").isoformat()
    end_iso = datetime.datetime.strptime(end_str, "%Y-%m-%d %H:%M").isoformat()
    
    database.add_task(desc, start_iso, end_iso, rate)
    print("Detyra u shtua me sukses!")

def view_tasks_flow():
    """Paraqet detyrat për një muaj specifik."""
    print("\n--- Detyrat për një muaj ---")
    try:
        year = int(input("Jepni vitin (p.sh., 2025): "))
        month = int(input("Jepni muajin (1-12): "))
    except ValueError:
        print("Viti ose muaji i pavlefshëm.")
        return

    tasks_data = database.get_tasks_for_month(year, month)
    if not tasks_data:
        print("Nuk u gjetën detyra për këtë muaj.")
        return

    print(f"\n--- Detyrat për {month:02d}/{year} ---")
    total_payment = 0
    for row in tasks_data:
        task = Task(**dict(row))
        duration = task.calculate_duration_hours()
        payment = task.calculate_payment()
        total_payment += payment
        
        print(f"Përshkrimi: {task.description}")
        print(f"  > Kohëzgjatja: {duration:.2f} orë")
        print(f"  > Pagesa Totale: {payment:.2f} €")
        print("-" * 20)
    
    print(f"Pagesa totale për muajin: {total_payment:.2f} €")
    
def generate_report_flow():
    """Gjeneron raportin CSV."""
    print("\n--- Gjenero Raport ---")
    try:
        year = int(input("Jepni vitin (p.sh., 2025): "))
        month = int(input("Jepni muajin (1-12): "))
    except ValueError:
        print("Viti ose muaji i pavlefshëm.")
        return
        
    reports.generate_csv_report(year, month)


def main():
    """Funksioni kryesor që ekzekuton programin."""
    database.create_tables() # Sigurohet që tabela e databazës ekziston
    while True:
        choice = show_menu()
        if choice == '1':
            add_new_task_flow()
        elif choice == '2':
            view_tasks_flow()
        elif choice == '3':
            generate_report_flow()
        elif choice == '4':
            print("Mirupafshim!")
            break
        else:
            print("Opsion i pavlefshëm, provo përsëri.")

if __name__ == "__main__":
    main()