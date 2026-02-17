import requests

url = "https://graphql-prod-4843.edge.aws.worldathletics.org/graphql"

headers = {
    "content-type": "application/json",
    "origin": "https://worldathletics.org",
    "referer": "https://worldathletics.org/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}


payload = {
    "operationName": "GetSingleCompetitorResultsDiscipline",
    "variables": {
        "id": 14549089,
        "resultsByYear": 2025,
        "resultsByYearOrderBy": "discipline"
    },
    "query": """
    query GetSingleCompetitorResultsDiscipline($id: Int, $resultsByYearOrderBy: String, $resultsByYear: Int) {
      getSingleCompetitorResultsDiscipline(id: $id, resultsByYear: $resultsByYear, resultsByYearOrderBy: $resultsByYearOrderBy) {
        activeYears
        resultsByEvent {
          discipline
          results {
            date
            competition
            venue
            country
            place
            mark
          }
        }
      }
    }
    """
}

res = requests.post(url, headers=headers, json=payload)

print("STATUS:", res.status_code)
print("CONTENT TYPE:", res.headers.get("content-type"))
print("RESPONSE PREVIEW:\n", res.text[:500])

exit()  


#not working website is protected need to use selenium or playwright