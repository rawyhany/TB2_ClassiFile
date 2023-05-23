# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy project files to the working directory
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app is running on
EXPOSE 5000

# Set the entry point command to start your Flask app
CMD ["gunicorn", "classifile:app", "--bind=0.0.0.0:$PORT"]
