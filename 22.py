class Doc:
    def __init__(self, *test):
        self.test = test

    def __str__(self):
        return f'{self.test}'

    def __add__(self, other):

        test = tuple( x + y for x, y in zip(self.test , other.test))
        return Doc(*test)

doc1 = Doc('Object')
doc2 = Doc('Oriented')
print(doc1 + doc2)
