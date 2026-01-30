# 🎬 Movie Recommender System

A content-based movie recommendation system built using **Python**, **Streamlit**, and the **TMDB API**, capable of suggesting similar movies along with posters, ratings, release dates, and descriptions.

---

## 🚀 Features

- ✔ Recommend top 5 similar movies  
- ✔ Fetch movie details using the TMDB API  
- ✔ Display posters, ratings, release dates, and descriptions  
- ✔ Simple and clean Streamlit UI  
- ✔ Fast similarity-based recommendations  
- ✔ Uses preprocessed `.pkl` model files  

---

## 🖥 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python** | Core programming |
| **Pandas** | Data handling |
| **Scikit-Learn** | Similarity model |
| **Streamlit** | Web UI |
| **TMDB API** | Movie details |
| **Pickle** | Model data loading |

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Shreyaaaaa07/Movie-recommender-system.git

Navigate into the project:

cd Movie-recommender-system


Install required packages:

pip install -r requirements.txt

▶️ Run the App
streamlit run app.py


This will open the app in your browser.

🔑 TMDB API Setup

Create a free account on TMDB

Go to Settings → API and get your API key

Replace the API key in app.py:

API_KEY = "YOUR_API_KEY"

📁 Project Structure
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── .gitignore
├── requirements.txt
└── README.md

🧠 How It Works

User selects a movie

The system finds its index in the similarity matrix

Retrieves the top 5 most similar movies

Fetches posters + movie details using the TMDB API

Displays everything in a clean Streamlit interface

🙌 Author

Shreya
Movie Recommender System using ML + Streamlit
Open to feedback and collaboration!

⭐ Contribute

If you like this project, please ⭐ star the repository!
Contributions, issues, and pull requests are welcome.

