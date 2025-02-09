# Use official Python base image
FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libnss3 \
    libgconf-2-4 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxrandr2 \
    libasound2 \
    libatk1.0-0 \
    libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download and install Chromium
RUN wget -q -O /tmp/chrome-linux.zip https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.112/linux64/chrome-linux.zip \
    && unzip /tmp/chrome-linux.zip -d /usr/local/ \
    && rm /tmp/chrome-linux.zip

# Set environment variable for Chrome binary location
ENV CHROME_BIN="/usr/local/chrome-linux/chrome"

# Expose the application port
EXPOSE 10000

# Run the app using Gunicorn
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:10000"]
