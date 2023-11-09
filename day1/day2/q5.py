#5. **Create a list of dictionaries, where each dictionary represents a book.
#Include keys for "title," "author," and "year." Then, print the titles of all the books.**

books = [
    {"title": "Book 1", "author": "Author 1", "year": 2020},
    {"title": "Book 2", "author": "Author 2", "year": 2018},
    {"title": "Book 3", "author": "Author 3", "year": 2022},
    {"title": "Book 4", "author": "Author 4", "year": 2019},
]

for book in books:
    print(book["title"])

