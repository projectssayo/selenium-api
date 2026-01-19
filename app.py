from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/title")
def get_title(url: str):
    try:
        r = requests.get(url, timeout=10, headers={
            "User-Agent": "Mozilla/5.0"
        })
        r.raise_for_status()
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to fetch URL")

    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.title.string.strip() if soup.title else None

    return {
        "url": url,
        "title": title
    }
