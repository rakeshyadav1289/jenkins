# Use a lightweight Python 2025-compatible base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the Flask default port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
