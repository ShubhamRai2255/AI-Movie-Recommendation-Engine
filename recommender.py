import pickle

# Load saved files
movies = pickle.load(open('models/movies.pkl', 'rb'))
similarity = pickle.load(open('models/similarity.pkl', 'rb'))


def recommend(movie):
    # Find the index of the selected movie
    movie_index = movies[movies['title'] == movie].index[0]

    # Get similarity scores
    distances = similarity[movie_index]

    # Sort movies based on similarity
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    # Get movie titles
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies
print(recommend("Avatar"))
