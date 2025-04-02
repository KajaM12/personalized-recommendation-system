from flask import Flask, request, jsonify
from recommend import recommend_books, recommend_movies, recommend_music
import pandas as pd

app = Flask(__name__)

# Load data
books_df = pd.read_csv("data/books.csv")
movies_df = pd.read_csv("data/movies.csv")
music_df = pd.read_csv("data/music.csv")

@app.route("/recommend/books", methods=["GET"])
def recommend_book():
    book = request.args.get("book")
    recommendations = recommend_books(book, books_df)
    return jsonify(recommendations)

@app.route("/recommend/movies", methods=["GET"])
def recommend_movie():
    movie = request.args.get("movie")
    recommendations = recommend_movies(movie, movies_df)
    return jsonify(recommendations)

@app.route("/recommend/music", methods=["GET"])
def recommend_song():
    song = request.args.get("song")
    recommendations = recommend_music(song, music_df)
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
