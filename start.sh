#!/bin/bash
# Install Chrome
apt-get update && apt-get install -y wget unzip
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb || apt-get -fy install

# Start your app
gunicorn main:app --bind 0.0.0.0:10000
