import requests
from bs4 import BeautifulSoup
url = "https://iwf.sport/weightlifting_/athletes-bios/?athlete=yoo-diego-martin-2009-11-05&id=21652"

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "Accept" : "*/*"
}
res = requests.get(url, headers=headers)

print(res.status_code)

print(res.text)


soup = BeautifulSoup(res.text, "html.parser")

print(soup)