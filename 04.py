class Person:
    instances = []
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        Person.instances.append(self)
    @classmethod
    def count_instances(cls):
        return len(Person.instances)

p1= Person('seet','leet')
p2= Person('met','dat')
print(p1.count_instances())
