# Hapi 1: Fillo nga një imazh bazë zyrtar i Python
FROM python:3.9-slim

# Hapi 2: Përcakto direktoriumin e punës brenda kontejnerit
WORKDIR /app

# Hapi 3: Kopjo skedarin e varësive dhe instalo ato
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Hapi 4: Kopjo kodin e aplikacionit tënd brenda kontejnerit
COPY ./app .

# Hapi 5: Përcakto komandën që do të ekzekutohet kur kontejneri niset
CMD ["python", "-m", "app.main"]