class Book:
    language = "ENG"
    is_ebook = True

    def set_title(self, title):
        self.title = title


book = Book()
book.set_title("Inferno")
print(book.title)
