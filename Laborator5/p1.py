import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    """ aria cercului = pi*raza^2 """
    def area(self):
        return math.pi * self.radius ** 2

    """ perimetrul cercului este 2*pi*raza"""
    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    """ aria dreptunghiului este lungimea*latimea"""
    def area(self):
        return self.length * self.width

    """ perimetrul dreptunghiului este 2*(lungimea + latimea) """
    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    """ aria triunghiului este radical (s*(s-latura1)*(s-latura2)*(s-latura3))
        unde s este semiperimetru """
    def area(self):
        # Utilizăm formula semi-perimetrului pentru a calcula aria unui triunghi
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)

    print("Circle - Area:", circle.area())
    print("Circle - Perimeter:", circle.perimeter())

    print("Rectangle - Area:", rectangle.area())
    print("Rectangle - Perimeter:", rectangle.perimeter())

    print("Triangle - Area:", triangle.area())
    print("Triangle - Perimeter:", triangle.perimeter())
