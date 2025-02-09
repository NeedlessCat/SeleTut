from flask import Flask

app = Flask(__name__)

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Set binary location to downloaded Chromium
    options.binary_location = os.path.abspath("./chrome-linux/chrome")

    # Start WebDriver
    service = Service(ChromeDriverManager().install())
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
