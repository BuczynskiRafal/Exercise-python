class Book:
    language = 'ENG'
    is_ebook = True

    def set_title(self, title):
        if isinstance(title, str):
            self.title = title
        else:
            raise TypeError('The value on the title attribute must be of str type.')
        return self.title

book = Book()

book.set_title('Inferno')
print(book.title)