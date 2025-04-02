import pandas as pd
from sklearn.neighbors import NearestNeighbors

def recommend_books(book_title, data):
    book_ratings = data.pivot(index="user_id", columns="book_title", values="rating")
    book_ratings = book_ratings.fillna(0)
    
    model = NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(book_ratings.T)

    book_idx = list(book_ratings.columns).index(book_title)
    distances, indices = model.kneighbors([book_ratings.T.iloc[book_idx]], n_neighbors=5)

    recommended_books = [book_ratings.columns[i] for i in indices.flatten()]
    return recommended_books

# Load sample data
df = pd.read_csv("data/book_ratings.csv")

# Test recommendation
print(recommend_books("The Hobbit", df))
