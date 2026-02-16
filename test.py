import requests

url = "https://practiceapi.geeksforgeeks.org/api/vr/problems/?pageMode=explore&page=2&sortBy=submissions"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

session = requests.Session()

res = session.get(url, headers=headers)

print("Status:", res.status_code)

data = res.json()

print(data)