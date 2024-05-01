# Dockerfile.worker

FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code/

RUN apt-get update && apt-get install -y python3-opencv


# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install qmanager-1.0.tar.gz
