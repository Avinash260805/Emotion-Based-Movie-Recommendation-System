import streamlit as st
from PIL import Image
import numpy as np
from premode import detect_emotion
from Data import movie_recommend
import html

st.set_page_config(page_title="Emotion-Based Movie Recommender", layout="wide")
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
    }
    html, body, [class*="stApp"] {
        color: white;
    }
    div.stButton > button {
        background-color: #1E90FF;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 8px 20px;
        font-size: 16px;
    }
    div.stButton > button:hover {
        background-color: #104E8B;
    }
    div[data-testid="stCameraInput"] > div > label {
    color: white !important;           /* Change button text color */
    font-weight: 600 !important;
    /* Optional: add text shadow for better contrast */
    text-shadow: 0 0 5px black;
}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎥 Emotion-Based Movie Recommender")
st.write("Take a selfie and we’ll recommend movies based on your mood!")

img_data = st.camera_input("📸 Click to take a photo")
if 'last_img_data' not in st.session_state:
        st.session_state.last_img_data = None

if img_data != st.session_state.last_img_data:
    st.session_state.detected_emotion = None
    st.session_state.emotion_scores = None
    st.session_state.movie_html = ""
    st.session_state.last_img_data = img_data

if 'movie_html' not in st.session_state:
    st.session_state.movie_html = ""

if 'detected_emotion' not in st.session_state:
    st.session_state.detected_emotion = None
if 'emotion_scores' not in st.session_state:
    st.session_state.emotion_scores = None
if 'movie_html' not in st.session_state:
    st.session_state.movie_html = ""

if img_data:



    if st.button("🍿 Welcome to Movies"):
        img = Image.open(img_data)
        img_np = np.array(img)

        with st.spinner("Detecting your emotion..."):
            dominant_emotion, emotion_scores = detect_emotion(img_np)

        st.session_state.detected_emotion = dominant_emotion
        st.session_state.emotion_scores = emotion_scores

        st.success(f"Detected Emotion: **{dominant_emotion.upper()}**")


        movies = movie_recommend(dominant_emotion)

        html_code = '<div style="display: flex; overflow-x: auto; padding: 10px;">'
        for movie in movies:
            safe_title = html.escape(movie['title'])
            html_code += (
                f'<div style="flex: 0 0 auto; margin-right: 15px; text-align: center; width: 150px;">'
                f'<img src="{movie["poster"]}" alt="{safe_title}" style="width:150px; border-radius:10px;">'
                f'<p style="color:white; font-size:14px; margin: 5px 0 0 0; word-wrap: break-word; white-space: normal;">{safe_title}</p>'
                f'</div>'
            )
        html_code += '</div>'
        st.session_state.movie_html = html_code
    
    if st.session_state.movie_html:
        st.markdown(st.session_state.movie_html,unsafe_allow_html=True)





