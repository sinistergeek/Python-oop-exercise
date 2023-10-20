from abc import ABC,asbtractmethod
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
                if self.salary<8000:
                    return self.salary*0.17
                else:
                    return 8000*0.17 + (self.salary - 8000) * 0.32

worker1 = WorkerTaxPayer(7000)
worker2 = WorkerTaxPayer(9500)
print(worker1.calculate_tax())
print(worker2.calculate_tax())
