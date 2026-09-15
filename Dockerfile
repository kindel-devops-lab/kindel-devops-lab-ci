# Lightweight version of python is enough
FROM python:3.10-slim

WORKDIR /app

# Prevent python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Install flake8, pytest and flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Port used by flask
EXPOSE 5000

CMD ["python3", "app.py"]
