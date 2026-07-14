import requests

url = "https://www.omdbapi.com/?apikey=f205566d&t=Avatar"

try:
    response = requests.get(url, timeout=10)

    print("Status:", response.status_code)
    print(response.text)

except Exception as e:
    print(e)