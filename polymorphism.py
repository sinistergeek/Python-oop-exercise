class lion:
    def color(self):
        print("The lion is yellow coloured!")
    def eats(self):
        print("The lion eats a lot!")

class deer:
    def color(self):
        print("The deer is white coloured!")
    def eats(self):
        print("The deer eats less!")


lio = lion()
dee = deer()
for animal in (lio, dee):
    animal.color()
    animal.eats()
