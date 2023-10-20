class StringListOnly(list):
    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only objects of type str can be added to the list.')
        super().append(string.lower())

slo = StringListOnly()
slo.append('Data')
slo.append('Science')
slo.append('Machine Learning')
print(slo)
