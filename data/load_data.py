import pandas as pd

def load_books_data():
    df = pd.read_csv("data/books.csv")
    return df

if __name__ == "__main__":
    books = load_books_data()
    print(books.head())
