class Human:
    #class attribute
    species = "Homo Sapiens"
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

x = Human("lame", 32, "Male")
y = Human("learning", 30, "Female")

print(x.age)
print(y.name)
