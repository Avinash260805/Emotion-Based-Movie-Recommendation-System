import requests
from premode import detect_emotion
import streamlit as st
import time


@st.cache_data(ttl=3600)
def movie_recommend(emotion):
    genres = {
        'happy': ['Comedy', 'Adventure', 'Romance'],
        'sad': ['Romance', 'Comedy','Drama', 'Inspirational', 'Animation', 'Slice of Life'],
        'angry': ['Action','comedy', 'Thriller', 'War', 'Crime', 'Revenge'],
        'fear': ['Horror', 'Mystery', 'Psychological Thriller', 'Suspense'],
        'neutral': ['Sci-Fi', 'Fantasy', 'Mystery', 'Documentary', 'Anthology'],
    }

    Base_url = "https://api.themoviedb.org/3"
    API_KEY = st.secrets["TMDB_API_KEY"]
    Endpoint =  "/search/movie"
    IMAGE_BASE = "https://image.tmdb.org/t/p/w500"
 
    recommend_movies = []
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    for genre in genres.get(emotion,[]):
        params = {
            "api_key": API_KEY,
            "query": genre,
            "language": "en-US",
            "page": 1
        }
        response = requests.get(Base_url+Endpoint,params=params)
        time.sleep(1)
        if response.status_code == 200:
            data = response.json()
            for movie in data.get('results', [])[:10]:
                title = movie.get('title')
                poster_path = movie.get('poster_path')
                movie_id = movie.get('id')
                
                if poster_path:
                    poster_url = IMAGE_BASE + poster_path
                    movie_link = f"https://www.themoviedb.org/movie/{movie_id}"
                    recommend_movies.append({
                        "title": title,
                        "poster": poster_url,
                        "link": movie_link
                    })
        else:
            print('unable to retrieve data')
    return recommend_movies





