
import requests
from bs4 import BeautifulSoup

url = "https://uww.org/athletes-results"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)
print("status:", r.status_code)

soup = BeautifulSoup(r.text, "html.parser")


text = soup.get_text("\n")


