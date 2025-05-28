# 🎬 Movie Recommendation System API

A simple movie recommendation system built with **FastAPI** and **Python**.
This API provides movie suggestions based on similarity of movie genres and titles.

## Features

- FastAPI backend with endpoints to get movie recommendations
- Sample dataset with 100 popular movies
- Uses cosine similarity on movie features for recommendations
- Easy to extend with more data or better recommendation logic

## Project Structure

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

## Installation

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

## Running the API

```bash
uvicorn main:app --reload
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)
Swagger at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints

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

## Contact

Feel free to reach out for questions, feedback, or collaboration!

**Happy Coding!** 📬
