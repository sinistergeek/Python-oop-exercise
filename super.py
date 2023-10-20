class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def description(self):
        print(f"Hey! My name is {self.name}, I'm a {self.gender} and I'm {self.age} years old")
    def code(self):
        print(f"I can code{self.name}")

class Girl(Human):
    def codecode(self):
        print(f"i can teach{self.age}")
    def activity(self):
        super().code()
g = Girl('sinister', 30, 'girl')
g.description()
g.activity()
g.codecode()
