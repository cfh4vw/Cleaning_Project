FROM python:3.10-slim

# Create app directory
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src
COPY assets/ ./assets

EXPOSE 5000

# Run the app
CMD ["python", "src/app.py"]

