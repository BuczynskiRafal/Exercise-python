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


class CustomDate:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        if self.day < 10:
            if self.month < 10:
                return f"0{self.day}-0{self.month}-{self.year}"
            return f"0{self.day}-{self.month}-{self.year}"
        if self.month < 10:
            return f"{self.day}-0{self.month}-{self.year}"

    @classmethod
    def date_form_txt(cls, text):
        day, mont, year = text.split("-")
        return cls(int(day), int(mont), int(year))


    @classmethod
    def



d1 = CustomDate(7, 8, 2000)
d2 = CustomDate(12, 8, 2001)
d3 = CustomDate.date_form_txt("14-09-2002")
print(d1)
print(d2)
print(d3)

    # try:
    #     datetime.datetime.strptime(dataod, "%Y-%m-%d")
    # except ValueError:
    #     raise ValueError("Incorrect data format, should be YYYY-MM-DD")
















