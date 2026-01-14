"""Polymorphism examples"""

class Shape:
    def area(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, a):
        self.a = a
    def area(self):
        return self.a * self.a

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14159 * self.r * self.r


# Practice (5):
# 1) Add a `Triangle` class implementing `area`.
# 2) Use polymorphism by iterating over a list of different shapes and computing total area.
# 3) Implement a `perimeter` method and show different implementations across shapes.
# 4) Use duck typing: accept any object with `area` method (no inheritance).
# 5) Add validation for shape dimensions and raise ValueError for invalid input.
#
# Sample solutions (examples):
class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b; self.h = h
    def area(self):
        return 0.5 * self.b * self.h

if __name__ == "__main__":
    shapes = [Square(2), Circle(1), Triangle(3,4)]
    print([s.area() for s in shapes], 'total=', sum(s.area() for s in shapes))
