import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and prepare data
df = pd.read_csv("data/movies.csv", quotechar='"', on_bad_lines='skip')

df = df.dropna(subset=["genres"])

# Build TF-IDF matrix
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["genres"])

# Cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Map movie titles to indices
indices = pd.Series(df.index, index=df["title"]).drop_duplicates()

def get_recommendations(title, num_recs=5):
    if title not in indices:
        return []

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recs+1]
    movie_indices = [i[0] for i in sim_scores]

    return df["title"].iloc[movie_indices].tolist()
