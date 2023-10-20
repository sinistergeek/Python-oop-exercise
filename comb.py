class Shape:
    def no_of_sides(self):
        pass
    def three_dimensional(self):
        print("I am 3D from shape class")

class Rectangle(Shape):
    def no_of_sides(self):
        print("I have 4 slides. I am from Rectangle class")

class Polygon(Shape):
    def no_of_sides(self):
        print("I have 3 sides, I am from Polygon class")

re = Rectangle()
re.no_of_sides()
po = Polygon()
po.no_of_sides()
