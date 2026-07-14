# 🎬 AI Movie Recommendation Engine

An AI-powered Movie Recommendation System built using **Python**, **Machine Learning**, and **Streamlit**. The application recommends movies similar to a selected movie based on content similarity and also displays movie details such as poster, IMDb rating, release year, genres, and plot.

---

## 🚀 Features

- 🎥 Recommend 5 similar movies
- ⭐ IMDb Ratings
- 📅 Release Year
- 🎭 Movie Genres
- 📝 Movie Plot
- 🔍 Search movies by title
- 🖼️ Movie Posters
- ⚡ Fast and interactive Streamlit interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Pickle
- Requests
- OMDb API

---

## 📂 Project Structure

```
AI-Movie-Recommendation-Engine/
│
├── app.py                      # Main Streamlit Application
├── recommender.py              # Recommendation logic
├── download_movie_details.py   # Downloads movie details from OMDb API
├── requirements.txt
├── README.md
│
├── models/
│   ├── movies.pkl
│   └── similarity.pkl
│
├── data/
│   └── movies_metadata.csv
│
├── assets/
│
└── notebooks/
```

---

## 📊 How It Works

1. User selects a movie.
2. The recommendation model finds similar movies using cosine similarity.
3. The application retrieves:
   - Movie Poster
   - IMDb Rating
   - Release Year
   - Genres
   - Plot
4. Results are displayed in a clean Streamlit interface.

---

## 🧠 Machine Learning

The recommendation engine uses **Content-Based Filtering**.

### Workflow

- Data Cleaning
- Feature Engineering
- Text Vectorization
- CountVectorizer
- Cosine Similarity
- Recommendation Generation

---

## 📷 Screenshots

### Home Page

(Add Screenshot Here)

### Recommendation Results

(Add Screenshot Here)

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/ShubhamRai2255/AI-Movie-Recommendation-Engine.git
```

Go to the project directory

```bash
cd AI-Movie-Recommendation-Engine
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🔑 API Used

OMDb API

Get your free API key from

https://www.omdbapi.com/apikey.aspx

Create a file named `.env`

```env
OMDB_API_KEY=YOUR_API_KEY
```

---

## 📦 Dataset

TMDB 5000 Movie Dataset

Contains approximately 5000 movies with metadata used for generating recommendations.

---

## 🎯 Future Improvements

- User Login
- Movie Watchlist
- Favorites
- Search Suggestions
- Dark Mode
- Filters by Genre
- Filters by IMDb Rating
- Release Year Filter
- Top Rated Movies
- Trending Movies
- Deployment on Streamlit Cloud

---

## 👨‍💻 Author

**Shubham Rai**

B.Tech CSE Student

GitHub:
https://github.com/ShubhamRai2255

---

## ⭐ Support

If you like this project,

⭐ Star this repository

Fork it

Contribute with pull requests

---

## 📄 License

This project is licensed under the MIT License.
