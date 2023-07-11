# Use the official Python base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code to the working directory
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port the Flask app will be running on
EXPOSE 5000

# Initialize the SQLite database
#RUN flask init-db

# Start the Flask application
CMD ["flask", "run"]
