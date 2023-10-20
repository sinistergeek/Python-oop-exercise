class abc:
    def __init__(self, *comp):
        self.comp = comp

    def __str__(self):
        return f'{self.comp}'

    def __repr__(self):
        return f'{self.comp}'

    def __add__(self, anddy):
        comp = tuple (x+y for x,y in zip(self.comp, anddy.comp))
        return abc(*comp)

a1 = abc(4, 2)
a2 = abc(-1, 3)
print(a1 + a2)
