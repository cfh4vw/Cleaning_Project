FROM python:3.10-slim

# Create app directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src
COPY assets/ ./assets

EXPOSE 5000

# Set Flask environment variables
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Run the app
CMD ["flask", "run"]

