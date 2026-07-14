import streamlit as st
import pandas as pd
import pickle

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="🎬 Movie Recommendation Engine",
    page_icon="🎬",
    layout="wide"
)

# ----------------------------
# LOAD DATA
# ----------------------------
movies = pickle.load(open("models/movies.pkl", "rb"))
similarity = pickle.load(open("models/similarity.pkl", "rb"))
details = pd.read_csv("data/movie_details.csv")

# ----------------------------
# RECOMMENDATION FUNCTION
# ----------------------------
def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for item in movie_list:

        title = movies.iloc[item[0]].title

        info = details[details["title"] == title]

        if info.empty:
            recommendations.append({
                "title": title,
                "poster": "",
                "rating": "N/A",
                "year": "N/A",
                "genre": "N/A",
                "plot": "Plot not available."
            })

        else:

            row = info.iloc[0]

            recommendations.append({

                "title": title,

                "poster": row.get("poster", ""),

                "rating": row.get("rating", "N/A"),

                "year": row.get("year", "N/A"),

                "genre": row.get("genre", "N/A"),

                "plot": row.get("plot", "Plot not available.")

            })

    return recommendations


# ----------------------------
# TITLE
# ----------------------------
st.title("🎬 AI Movie Recommendation Engine")

st.write(
    "Find movies similar to your favourite movie using Machine Learning."
)

st.markdown("---")

# ----------------------------
# SEARCH BOX
# ----------------------------
search = st.text_input("🔍 Search Movie")

filtered_movies = movies

if search:

    filtered_movies = movies[
        movies["title"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

selected_movie = st.selectbox(
    "Select Movie",
    filtered_movies["title"].values
)

# ----------------------------
# BUTTON
# ----------------------------
if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    cols = st.columns(5)

    for col, movie in zip(cols, recommendations):

        with col:

            poster = movie["poster"]

            if isinstance(poster, str) and poster.startswith("http"):
                st.image(poster, use_container_width=True)
            else:
                st.write("🖼️ Poster not available")

            st.markdown(f"### {movie['title']}")

            st.write(f"⭐ IMDb: {movie['rating']}")

            st.write(f"📅 Year: {movie['year']}")

            st.write(f"🎭 Genre: {movie['genre']}")

            plot = movie["plot"]

            if pd.isna(plot) or plot == "":
                st.caption("Plot not available.")
            else:
                st.caption(str(plot)[:120] + "...")

# ----------------------------
# SIDEBAR
# ----------------------------
st.sidebar.title("About")

st.sidebar.info(
    """
Movie Recommendation Engine

Built Using

✅ Python

✅ Machine Learning

✅ NLP

✅ Cosine Similarity

✅ Streamlit

Dataset:
TMDB 5000 Movies
"""
)

# ----------------------------
# FOOTER
# ----------------------------
st.markdown("---")

st.markdown(
    "<center><h4>Made by Shubham Rai ❤️</h4></center>",
    unsafe_allow_html=True
)