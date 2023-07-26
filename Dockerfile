# Use the official Python image as the base image
FROM python:3.9-slim

# Install required system dependencies
RUN apt-get update \
  && apt-get install -y --no-install-recommends libpq-dev gcc \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Copy the Python application files to the container
WORKDIR /app
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python application
CMD ["python", "main.py"]
