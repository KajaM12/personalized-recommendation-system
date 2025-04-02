from flask import Flask, request, jsonify
from recommend import recommend_books
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("data/book_ratings.csv")

@app.route("/recommend", methods=["GET"])
def recommend():
    book = request.args.get("book")
    recommendations = recommend_books(book, df)
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
