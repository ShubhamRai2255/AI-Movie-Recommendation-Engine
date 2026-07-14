import requests

url = "https://api.themoviedb.org/3/movie/550?api_key=2271efb2b410bca33942fe80feb6bc47"

try:
    response = requests.get(url, timeout=10)
    print("Status:", response.status_code)
    print(response.json()["title"])
except Exception as e:
    print(e)