class Book:
    language = "ENG"
    is_ebook = True


books_data = [
    {"author": "Dan Brown", "title": "Inferno"},
    {"author": "Dan Brown", "title": "The Da Vinci Code", "year_of_publishment": 2003},
]

books = []
for book_data in books_data:
    book = Book()
    for attr, val in book_data.items():
        setattr(book, attr, val)
    books.append(book)

for _ in books:
    print(_.__dict__)
