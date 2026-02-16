import requests

url = "https://uww.org/apiv4/getrankinglist/api/rankings/current/seniors/fs/61?page=1&season=2024"

res=requests.get(url)

print(res.status_code)

fs61 = res.json()

athletes = fs61["content"]["hydramember"]

for a in athletes:
    person = a["person"]

    name = person["name"]
    country = person["noc"]
    rank = a["rank"]
    points = a["uwwPoints"]
    img = person["profilePicture"]

    print({
        "rank": rank,
        "name": name,
        "country": country,
        "points": points,
        "image": img
    })