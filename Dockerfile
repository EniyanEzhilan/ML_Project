# Use a Python base image
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3.11

# Install dependencies
RUN apt-get update && apt-get install -y \
    python-pip

RUN apt-get install python-pip
# RUN python3 ./get-pip.py
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN python -m pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Set the environment variable for Flask app
ENV FLASK_APP app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]