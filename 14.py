class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)
    
    def __bool__(self):
        if not self.components:
            return False
        return False if not self.components[0] else True



v1 = Vector(0,4,5)
v2 = Vector()
v3 = Vector(5,0,-1)
print(bool(v1))
print(bool(v2))
print(bool(v3))

