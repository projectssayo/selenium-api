from fastapi import FastAPI
import undetected_chromedriver as uc

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Use /title?url=YOUR_URL to get the page title"}

@app.get("/title")
def get_title(url: str):
    options = uc.ChromeOptions()
    options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = uc.Chrome(options=options)
    driver.get(url)
    title = driver.title
    driver.quit()
    return {"url": url, "title": title}
