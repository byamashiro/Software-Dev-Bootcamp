# Use an official Python runtime as a parent image (1) # python:3.12-slim-bookworm
FROM python:3.12-slim

# System deps for your stack:
# - libgl1/libglib2.0: OpenCV GUI/IO bits
# - libopenjp2-7: Glymur (OpenJPEG)
# - libkrb5-3: Kerberos runtime used by some clients
# - ffmpeg: video IO (moviepy, imageio-ffmpeg can also bundle its own)
# - build-essential: fallback builds if a wheel is missing
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
      git curl ca-certificates \
      libgl1 libglib2.0-0 \
      libopenjp2-7 \
      libkrb5-3 \
      ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container (2) # /app
WORKDIR /app

# Copy the requirements file first to leverage Docker's build cache (3) # requirements.txt .
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt (4) # RUN pip install -r requirements.txt
RUN python -m pip install --upgrade "pip==25.0.1" "setuptools==75.8.0" wheel \
 && pip install -r requirements.txt

# Copy your application code into the container (5) # COPY app.py .
# This copies 'app.py' from your current (host) directory into '/app' in the image
COPY hinode_paper.ipynb /app

# Command to run app.py when the container launches (6)
# CMD ["python", "app.py", "ls"]

# By default, run "python" so you can pass a script and args at 'docker run' time.
# Example: docker run --rm -v "$PWD":/app solar:py312 python my_script.py --flag
ENTRYPOINT ["python"]
CMD ["-V"]