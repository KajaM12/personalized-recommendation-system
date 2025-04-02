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

def recommend_movies(movie_title, data):
    movie_ratings = data.pivot(index="user_id", columns="movie_title", values="rating")
    movie_ratings = movie_ratings.fillna(0)

    model = NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(movie_ratings.T)

    movie_idx = list(movie_ratings.columns).index(movie_title)
    distances, indices = model.kneighbors([movie_ratings.T.iloc[movie_idx]], n_neighbors=5)

    recommended_movies = [movie_ratings.columns[i] for i in indices.flatten()]
    return recommended_movies

def recommend_music(song_title, data):
    music_ratings = data.pivot(index="user_id", columns="song_title", values="rating")
    music_ratings = music_ratings.fillna(0)

    model = NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(music_ratings.T)

    song_idx = list(music_ratings.columns).index(song_title)
    distances, indices = model.kneighbors([music_ratings.T.iloc[song_idx]], n_neighbors=5)

    recommended_songs = [music_ratings.columns[i] for i in indices.flatten()]
    return recommended_songs
