import uuid


class Book:

    def __init__(self, title, author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]


book1 = Book(title='Inferno', author='Dan Brown')
print(book1.__dict__.keys())
