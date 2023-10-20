from abc import ABC,abstractmethod
class TaxPayer(ABC):
    def __init__(self,salary):
        self.salary = salary
    @abstractmethod
    def calculate_tax(self):
        pass

class StudentTaxPayer(TaxPayer):
    def calculate_tax(self):
        return self.salary*0.15

class DisabledTaxPayer(TaxPayer):
    def calculate_tax(self):
        return self.salary*0.12

class WorkerTaxPayer(TaxPayer):
    def calculate_tax(self):
        if self.salary<80000:
            return self.salary*0.17
        else:
            return 8000*0.17 + (self.salary - 8000) * 0.32
        tax_payers = [StudentTaxPayer(5000),DisabledTaxPayer(70000),
                      WorkerTaxPyer(6800), WorkerTaxPayer(123666)]
        for tax_payer in tax_payers:
            print(tax_payer.calculate_tax())
