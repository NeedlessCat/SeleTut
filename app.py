from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

def scrape_website(url):
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(url)
    data = driver.title  # Example: Get page title
    driver.quit()
    
    return {"title": data}

@app.route("/scrape", methods=["POST"])
def scrape():
    url = request.json.get("https://en.wikipedia.org/wiki/British_Raj")
    if not url:
        return jsonify({"error": "URL is required"}), 400
    return jsonify(scrape_website(url))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
