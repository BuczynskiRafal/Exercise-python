class Employee:

    count = 0

    def __init__(self, first_name, last_name, email, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = salary
        Employee.count += 1

    def get_annual_salary(self):
        return 12 * self.salary

    def show_employee_information(self):
        return f"Pracownik: {self.first_name} {self.last_name}, adres e-mail: {self.email}, wynagrodzenie miesięczne: {self.salary}"


class Library:

    def __init__(self, books=None):
        self._collection = []

        if books:
            for book in books:
                self._collection.add_book(book)

    @property
    def number_of_books(self):
        return len(self._collection)

    def add_book(self, book):
        if book not in self._collection:
            self._collection.append(book)

    def borrow_book(self, book):
        if book in self._collection:
            self._collection.remove(book)
            return self._collection

    def show_books(self):
        print(self._collection)