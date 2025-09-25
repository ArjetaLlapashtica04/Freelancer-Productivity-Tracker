import sqlite3

DATABASE_FILE = "produktiviteti.db"

def get_db_connection():
    """Krijon dhe kthen një lidhje me bazën e të dhënave."""
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row  # Kthen rreshtat si dictionarë
    return conn

def create_tables():
    """Krijon tabelën 'tasks' nëse nuk ekziston."""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            hourly_rate REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_task(description, start_time, end_time, hourly_rate):
    """Shton një detyrë të re në bazën e të dhënave."""
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO tasks (description, start_time, end_time, hourly_rate) VALUES (?, ?, ?, ?)",
        (description, start_time, end_time, hourly_rate)
    )
    conn.commit()
    conn.close()

def get_tasks_for_month(year, month):
    """Merr të gjitha detyrat për një muaj specifik."""
    conn = get_db_connection()
    month_pattern = f"{year}-{month:02d}-%"
    cursor = conn.execute(
        "SELECT * FROM tasks WHERE start_time LIKE ?", (month_pattern,)
    )
    tasks = cursor.fetchall()
    conn.close()
    return tasks