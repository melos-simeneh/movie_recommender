from fastapi import FastAPI
from recommender import get_recommendations
from schemas import MovieRequest

app = FastAPI(title="Movie Recommendation API")

@app.get("/")
def root():
    return {"message": "Movie Recommendation API is running!"}

@app.post("/recommend")
def recommend_movies(req: MovieRequest):
    recs = get_recommendations(req.title, req.num_recs)
    if not recs:
        return {"message": "Movie not found in the dataset."}
    return {"recommendations": recs}
