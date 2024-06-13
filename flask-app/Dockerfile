# Use an official Python runtime as a parent image
FROM python:3.11-alpine
# Update and install required packages
RUN apk update --no-cache && \
    apk add python3-dev build-base linux-headers pcre-dev
# Create a new user
RUN adduser -D uwsgiuser

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Copy the current directory contents into the container at /app
ADD . /app
# Switch to the created user
USER uwsgiuser