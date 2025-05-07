import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dummy movie dataset
data = {
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['Inception', 'The Matrix', 'Interstellar', 'The Prestige', 'The Imitation Game'],
    'description': [
        'dreams within dreams, heist, sci-fi, action',
        'simulation, AI, dystopia, action',
        'space, time, black hole, love, sci-fi',
        'magic, rivalry, illusion, obsession',
        'codebreaking, WWII, Turing, biography'
    ]
}

movies_df = pd.DataFrame(data)

# Vectorize
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(movies_df['description'])
cosine_sim = cosine_similarity(tfidf_matrix)

def recommend_movies(title, top_n=3):
    if title not in movies_df['title'].values:
        return []
    idx = movies_df[movies_df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    return [movies_df.iloc[i[0]]['title'] for i in sim_scores]
