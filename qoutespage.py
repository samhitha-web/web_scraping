import requests

url = "https://quotes.toscrape.com/"

response = requests.get(url)

print("Status Code:", response.status_code)
print("------------------------------------------------")

print(response.text)  
