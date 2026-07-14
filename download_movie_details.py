import pickle
import pandas as pd
import requests
import time
from tqdm import tqdm

movies = pickle.load(open("models/movies.pkl", "rb"))

API_KEY =   "f205566d"

movie_details = []

session = requests.Session()

for index, title in enumerate(tqdm(movies["title"])):

    url = f"https://www.omdbapi.com/?t={title}&apikey={API_KEY}"

    for attempt in range(3):

        try:
            response = session.get(url, timeout=15)
            data = response.json()

            movie_details.append({
                "title": title,
                "poster": data.get("Poster", ""),
                "rating": data.get("imdbRating", ""),
                "year": data.get("Year", ""),
                "genre": data.get("Genre", ""),
                "plot": data.get("Plot", "")
            })

            break

        except Exception as e:

            if attempt == 2:
                print(f"Skipped: {title}")

                movie_details.append({
                    "title": title,
                    "poster": "",
                    "rating": "",
                    "year": "",
                    "genre": "",
                    "plot": ""
                })

            time.sleep(2)

    if (index + 1) % 100 == 0:
        pd.DataFrame(movie_details).to_csv(
            "data/movie_details.csv",
            index=False
        )

    time.sleep(0.2)

pd.DataFrame(movie_details).to_csv(
    "data/movie_details.csv",
    index=False
)

print("\n✅ Download Complete!")