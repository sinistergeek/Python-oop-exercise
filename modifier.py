class Employee:
    def __init__(self, name, employeeId, salary):
        self.name = name
        self._empID = employeeId
        self.__salary = salary
    def getSalary(self):
        print(f"THe salary of Employee is {self.__salary}")
employee1 = Employee("Edcorner", "121112","$1599")

print(f"The Employee's name is {employee1.name}")
print(f"The Employee's id is {employee1._empID}")
employee1.getSalary()

#print(f"The Employee's salary is {employee1.salary}")



