# Use an official Python runtime as a parent image (1) # python:3.12-slim-bookworm
FROM jupyter/minimal-notebook

# Set the working directory in the container (2) # /app
WORKDIR /app

# Copy the requirements file first to leverage Docker's build cache (3)
COPY requirements.txt .

# Install any needed packages specified in requirements.txt (4)
RUN pip install -r requirements.txt

# Copy your application code into the container (5)
# This copies 'app.py' from your current (host) directory into '/app' in the image
# COPY nasafetch.py .

# Command to run app.py when the container launches (6)
# CMD ["python", "nasafetch.py", "ls"]
