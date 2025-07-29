# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim-buster

# Set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
# We copy our requirements file first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY ./app /app/app

# The command to run the application
# Uvicorn will be running on http://0.0.0.0:$PORT
# The PORT environment variable is automatically set by Cloud Run.
CMD exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080} 