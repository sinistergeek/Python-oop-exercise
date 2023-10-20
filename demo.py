class abc:

    def __init__(self, *test):
        self.test = test

    
    def __repr__(self):
        return f'{self.test}'
    print(repr)

    def __bool__(self):
        if not self.test:
            return False
        return False if not self.test[0] else True
    print(bool)

t1 = abc()
t2 = abc(0,23,2)
print(t1)
print(bool(t1))
print(t1)
print(bool(t2))
print (t1)
