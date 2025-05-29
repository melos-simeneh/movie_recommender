# 🎬 Movie Recommendation System API

A simple movie recommendation system built with **FastAPI** and **Python**, using **TF-IDF** and **cosine similarity** for content-based recommendations based on movie titles and genres.

## 🚀 Features

- ✅ FastAPI backend with auto-generated Swagger UI
- ✅ Content-based filtering using TF-IDF and cosine similarity
- ✅ RESTful API with both GET and POST endpoints
- ✅ Clean and lightweight – perfect for beginners

## 🧠 Machine Learning Algorithm

This project uses a Content-Based Filtering approach powered by:

- **TF-IDF Vectorization:** Converts movie titles and genres into numerical vectors based on the importance of words.
- **Cosine Similarity:** Measures how similar two movies are based on their vectorized text.

## 🔍 How It Works

1. Combine title and genres into a single text feature.
2. Apply TF-IDF vectorization to extract relevant features from text.
3. Compute cosine similarity scores between movies.
4. Recommend the most similar movies based on the input movie title.

## 📂 Project Structure

```bash
movie_recommender/
│
├── data/
│   └── movies.csv
├── main.py
├── recommender.py
├── schemas.py
├── requirements.txt
└── README.md
```

## 📦 Installation

1. **Clone the repo**

    ```bash
    git clone https://github.com/melos-simeneh/movie_recommender.git
    cd movie_recommender
    ```

2. **Create and activate a virtual environment**

    ```bash
    python -m venv env
    .\env\Scripts\activate # Windows
    source env/bin/activate # macOS/Linux
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure your movies.csv is properly formatted**
(Titles with commas must be enclosed in double quotes.)

## ▶️ Running the API

```bash
uvicorn main:app --reload
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

The Swagger documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📡 API Endpoints

- **GET** `/`

    Returns a simple welcome message.

- **POST** `/recommend`

    Get movie recommendations by sending a JSON body with the movie title and number of recommendations.

## Example usage

**Request body:**

```json
{
    "title": "Toy Story (1995)",
    "num_recs": 5
}
```

**Response:**

```json
{
    "recommendations": [
        "Jumanji (1995)",
        "Grumpier Old Men (1995)",
        "Father of the Bride Part II (1995)",
        "Heat (1995)",
        "Sabrina (1995)"
    ]
}
```

## 📬 Contact

Feel free to reach out for questions, feedback, or collaboration!

**Happy Coding!** 🚀
