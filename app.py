import streamlit as st
import pickle
import pandas as pd
import requests
import random

# -----------------------------
# TMDB API KEY
# -----------------------------
API_KEY = "0e30c963a21cec9409972d586cfd60d4"

# -----------------------------
# Load Pickle Files Safely
# -----------------------------
try:
    with open('movie_dict.pkl', 'rb') as f:
        movies_dict = pickle.load(f)
except FileNotFoundError:
    st.error("movie_dict.pkl not found. Make sure it's in the project folder.")
    st.stop()

try:
    with open('similarity.pkl', 'rb') as f:
        similarity = pickle.load(f)
except FileNotFoundError:
    st.error("similarity.pkl not found. Make sure it's in the project folder.")
    st.stop()

movies = pd.DataFrame(movies_dict)

# -----------------------------
# Function to get movie details from TMDB with fallback
# -----------------------------
@st.cache_data
def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException:
        # Offline / fallback info
        return "", "No description available.", "N/A", "N/A"

    poster = data.get("poster_path")
    poster_url = "https://image.tmdb.org/t/p/w500" + poster if poster else ""
    overview = data.get("overview", "No description available.")
    rating = data.get("vote_average", "N/A")
    release = data.get("release_date", "N/A")
    return poster_url, overview, rating, release

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = [movies.iloc[i[0]].title for i in movie_list]
    recommended_ids = [movies.iloc[i[0]].movie_id for i in movie_list]

    return recommended_movies, recommended_ids

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🎬 Movie Recommender System with TMDB Details")

selected_movie_name = st.selectbox("Select a movie:", movies['title'].values)

if st.button("Recommend"):
    names, ids = recommend(selected_movie_name)
    st.subheader("Recommended Movies:")

    for i in range(len(names)):
        poster, overview, rating, release = get_movie_details(ids[i])

        # Fallback if poster is missing
        if not poster:
            poster = "https://via.placeholder.com/150x225.png?text=No+Image"

        st.markdown(f"## {names[i]}")
        cols = st.columns([1, 2])

        with cols[0]:
            st.image(poster, width=150)  # replace use_column_width

        with cols[1]:
            st.markdown(f"**Rating:** ⭐ {rating}/10")
            st.markdown(f"**Release Date:** {release}")
            st.markdown("**Overview:**")
            st.write(overview)

        st.markdown("---")


