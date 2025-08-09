# 🎭 Emotion-Based Movie Recommendation System

An interactive web app built with **Streamlit**, **DeepFace**, and the **TMDB API** that detects your facial emotion via webcam and recommends movies accordingly.

---

## 🚀 Features
- 🎥 **Webcam Integration** – Capture your photo directly in the browser.
- 😀 **Emotion Detection** – Uses DeepFace with RetinaFace backend to detect your dominant emotion.
- 🍿 **Smart Movie Recommendations** – Movies fetched from TMDB API, tailored to your mood.
- 🎨 **Netflix-like UI** – Clean, responsive design.

---

## 🛠 Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python
- **AI Models:** DeepFace (RetinaFace backend)
- **API:** TMDB API (for movie data & posters)

---

## 📂 Project Structure
.
├── Frontend.py # Main Streamlit app
├── premode.py # Emotion detection logic
├── Data.py # Movie recommendation logic
├── requirements.txt # Dependencies
├── .gitignore # Ignored files & secrets
└── .streamlit/secrets.toml # TMDB API key (not in repo)

🌐 Deployment
This project can be deployed on Streamlit Community Cloud or any cloud service supporting Python.
