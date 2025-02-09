from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

def get_driver():
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Required for Render
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources
    options.add_argument("--disable-gpu")  # Disable GPU for headless mode

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
