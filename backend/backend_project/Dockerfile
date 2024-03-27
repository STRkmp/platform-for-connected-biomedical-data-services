# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code/

# Copy common_dto to backend_project
#COPY common_dto/ /code/backend_project/common_dto/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install qmanager-1.0.tar.gz

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
