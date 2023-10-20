class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def description(self):
        print(f"Hey! My Name is {self.name}, I'm a {self.gender} and I'm {self.age} years old")

class Boy(Human):
    def schoolName(self, schoolname):
        print(f"I study in {schoolname}")

b = Boy('sinister', 32, 'male')
b.description()
b.schoolName("MMIT")
