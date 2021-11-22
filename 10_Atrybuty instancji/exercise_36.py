class Book:
    language = "ENG"
    is_ebook = True


book = Book()
print(book.__dict__)
book.author = "Dan Brown"
book.title = "Inferno"
print(book.__dict__)
