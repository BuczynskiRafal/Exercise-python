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
        if self.salary > 80000:
            return (80000 * 0.17) + ((self.salary - 80000) * 0.32)
        return self.salary * 0.17


worker1 = WorkerTaxPayer(70000)
worker2 = WorkerTaxPayer(95000)
print(worker1.calculate_tax())
print(worker2.calculate_tax())
