# Maulahna Robinson
# CS620 Professor Dushan

import pandas as pd

data=pd.read_json("https://www.cs.odu.edu/~sampath/courses/data/books.json")
books_df = pd.json_normalize(data["books"])
# print(books_df.columns)
# print(books_df.head())

addy_books = books_df[books_df["author"] == "Addy Osmani"]["title"]
print("Books by Addy Osmani:\n",addy_books.tolist())