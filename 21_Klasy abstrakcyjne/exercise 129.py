from abc import ABC, abstractmethod


class TaxPayer(ABC):

    def __init__(self, salary):
        self.salary = salary

    @abstractmethod
    def calculate_tax(self):
        pass


class StudentTaxPayer(TaxPayer):

    def calculate_tax(self):
        return self.salary * 0.15


class DisabledTaxPayer(TaxPayer):

    def calculate_tax(self):
        return self.salary * 0.12


class WorkerTaxPayer(TaxPayer):

    def calculate_tax(self):
        if self.salary < 80000:
            return self.salary * 0.17
        else:
            return 80000 * 0.17 + (self.salary - 80000) * 0.32


payers = [StudentTaxPayer(50000), DisabledTaxPayer(70000), WorkerTaxPayer(68000), WorkerTaxPayer(120000)]
for payer in payers:
    print(payer.calculate_tax())