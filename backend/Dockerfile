# Use Python 3.13.5 image based on Debian Bullseye in its slim variant as the base image
FROM python:3.13.5-slim-bullseye AS builder

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Set the working directory within the container to /app for any subsequent commands
WORKDIR /app

# Copy the entire current directory contents into the container at /app
COPY . /app/


# Upgrade pip to ensure we have the latest version for installing dependencies
RUN pip install --upgrade pip

# Install dependencies from the requirements.txt file to ensure our Python environment is ready
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production stage
FROM python:3.13.5-slim

RUN useradd -m -r appuser && mkdir /app && chown -R appuser /app

# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Set the working directory
WORKDIR /app

# Copy application code
COPY --chown=appuser:appuser . .

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Switch to non-root user
USER appuser

# Expose the application port
EXPOSE 8000 

# Set the command to run our web service using Gunicorn, binding it to 0.0.0.0 and the PORT environment variable
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "config.wsgi:application"]