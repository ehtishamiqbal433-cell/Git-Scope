# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies if required
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project requirements or files
COPY . /app/

# Expose any necessary application ports (change if needed, e.g., 80, 5000)
EXPOSE 8080

# Default command to run your application
CMD ["python3", "-m", "http.server", "8080"]
