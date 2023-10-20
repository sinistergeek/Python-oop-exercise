class Human:
    #class attribute
    species = "Homo Sapiens"
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speak(self):
        return f"Hello everyone! I am {self.name}"
    def eat(self, favouriteDish):
        return f"I love to eat {favouriteDish}!!!"

x = Human("lame", 32, "Male")
y = Human("learning", 30, "Female")

print(x.speak())
print(y.eat("rice"))
