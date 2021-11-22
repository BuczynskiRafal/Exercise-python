class Book:
    language = 'ENG'
    is_ebook = True

    def set_title(self, value):
        if not isinstance(value, str):
            raise TypeError('The value of the title attribute must be of str '
                'type.')
        self.title = value

book = Book()

try:
    book.set_title(False)
except TypeError as error:
    print(error)

