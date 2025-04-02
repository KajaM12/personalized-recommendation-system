import pandas as pd

def load_books_data():
    df = pd.read_csv("data/books.csv")
    return df

def load_movies_data():
    df = pd.read_csv("data/movies.csv")
    return df

def load_music_data():
    df = pd.read_csv("data/music.csv")
    return df

if __name__ == "__main__":
    books = load_books_data()
    movies = load_movies_data()
    music = load_music_data()
    
    print(books.head())
    print(movies.head())
    print(music.head())
