class strp:

    def __init__(self, lenggy):
        self.lenggy = lenggy
    def __repr__(self):
        return f"strp(strings = '{self.lenggy}')"
    def __str__(self):
        return f'{self.lenggy}'

    def __add__(self, other):
        return strp(self.lenggy + " " + other.lenggy)

stp1 = strp("luee")
stp2 = strp("da")
print(stp1 + stp2)
