from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = FastAPI()

@app.get("/title")
def get_title(url: str):
    options = Options()
    options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)  # make sure chromedriver is available
    driver.get(url)
    title = driver.title
    driver.quit()
    return {"url": url, "title": title}
