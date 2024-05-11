# Dockerfile.worker

FROM base-opencv

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install qmanager-1.0.tar.gz
