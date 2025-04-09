import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        paragraphs = soup.find_all("p")
        return " ".join(p.get_text() for p in paragraphs)
    except Exception:
        return ""
