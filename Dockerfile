FROM ubuntu:latest

WORKDIR /usr/app/src

ARG DEBIAN_FRONTEND=noninteractive

# Install necessary system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    locales \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set up locales
RUN locale-gen en_US.UTF-8

# Copy the requirements file into the container
COPY requirements.txt ./

# Create and activate a virtual environment
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application code
COPY ./ ./

# Use the virtual environment's Python for running the application
CMD ["venv/bin/streamlit", "run", "app.py", "--server.port", "8501"]
