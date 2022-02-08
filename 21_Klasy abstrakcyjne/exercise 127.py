from abc import ABC, abstractmethod


class TaxPayer(ABC):

    def __init__(self, salary):
        self.salary = salary

    @abstractmethod
    def calculate_tax(self):
        pass


class DisabledTaxPayer(TaxPayer):
    def calculate_tax(self):
        return min(self.salary * 0.12, 5000.0)


disabled = DisabledTaxPayer(50000)
print(disabled.calculate_tax())


class StudentTaxPayer(TaxPayer):

    def calculate_tax(self):
        return self.salary * 0.15

