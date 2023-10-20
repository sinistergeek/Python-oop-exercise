class Doc:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(strings='{self.string}')"
    def __str__(self):
        return f'{self.string}'
    def __len__(self):
        return len(self.string)

    def __add__(self, other):

        return Doc(self.string + " " + other.string)

    def __eq__(self, other):

        return self.string == other.string

doc1 = Doc('Python')
doc2 = Doc('3.89')
print(doc1 == doc2)
