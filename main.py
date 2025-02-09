from flask import Flask

app = Flask(__name__)

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Set Chromium binary location from Docker environment
    options.binary_location = os.getenv("CHROME_BIN", "/usr/local/chrome-linux/chrome")

    # Start WebDriver
    service = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    return driver


@app.route("/")
def scrape():
    driver = get_driver()
    driver.get("https://en.wikipedia.org/wiki/British_Raj")
    page_source = driver.page_source
    driver.quit()
    return f"Scraped Page Length: {len(page_source)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
