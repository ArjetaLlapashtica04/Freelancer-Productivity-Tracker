Gjurmues Produktiviteti (Productivity Tracker)
This project is a modular, professional API built using Python's FastAPI framework and SQLAlchemy for data management. It allows users to track time spent on projects and tasks and generate financial reports.

🚀 Key Features
API Endpoints: Full CRUD (Create, Read, Update, Delete) functionality for Projects, Tasks, and Time Entries.

Data Persistence: Uses a lightweight SQLite database (produktiviteti.db) managed by SQLAlchemy.

Data Validation: Implements Pydantic schemas to ensure all incoming and outgoing data is correctly formatted.

Reporting: Generates a detailed CSV report of billable hours and earnings for a given month and year.

🛠️ Setup and Installation
Prerequisites
You need Python 3.8+ installed on your system.

1. Install Dependencies
Open your terminal in the project root directory and run the following commands to install the required libraries:

pip install fastapi
pip install "uvicorn[standard]"
pip install sqlalchemy
pip install pydantic
pip install pytest  # For running tests

2. Run the Application
The application is run using the Uvicorn ASGI server. The --reload flag is recommended during development to automatically restart the server when code changes are saved.

python -m uvicorn app.main:app --reload

💻 Usage (Interacting with the API)
Once the server is running, the API documentation is automatically generated. This documentation allows you to test every endpoint directly from your browser.

Access Docs: Open your web browser to:
http://127.0.0.1:8000/docs

Basic Workflow: To use the system, you must create data in the correct order:

POST /projects/: Create a new project (e.g., id: 1).

POST /tasks/: Create a task and link it using the project's ID (e.g., project_id: 1).

POST /time-entries/: Log work and link it using the task's ID (e.g., task_id: 1).

Generate Report:

GET /reports/csv: Download a CSV report by providing the year and month parameters.

🧪 Running Tests
Unit tests are implemented using the Pytest framework to ensure the payment and hour calculations are correct.

Make sure you have pytest installed (pip install pytest).

Run the tests from the root directory:

pytest
