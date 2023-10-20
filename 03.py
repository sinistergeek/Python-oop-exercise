class person:
    
    instances = []

    def __init__(self):
        person.instances.append(self)
    @classmethod
    def count_instances(cls):
        return person.instances

p1 = person()
p2 = person()
p3 = person()

print(person.count_instances())
