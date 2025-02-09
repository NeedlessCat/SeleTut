#!/bin/bash

# Download Chromium if not exists
if [ ! -f "./chrome-linux/chrome" ]; then
    echo "Downloading Chromium..."
    mkdir -p chrome-linux
    wget -qO- https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.112/linux64/chrome-linux.zip | busybox unzip - -d chrome-linux
    chmod +x chrome-linux/chrome
fi

# Start the application
gunicorn main:app --bind 0.0.0.0:10000
