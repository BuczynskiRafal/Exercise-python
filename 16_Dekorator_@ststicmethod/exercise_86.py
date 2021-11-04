import uuid


class Book:

    def __init__(self, title, author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

    def __repr__(self):
        return f"{self.__class__.__name__}(title='{self.title}', author='{self.author}')"


book1 = Book('Inferno', 'Dan Brown')
print(book1)