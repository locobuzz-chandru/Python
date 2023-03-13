from math import pi


# Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor
# Define a Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
#  testBelongs() method of the class which allows to test whether a point A(x, y) belongs to the circle C(O, r) or not.
class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def perimeter(self):
        return 2 * pi * self.r

    def area(self):
        return pi * self.r ** 2

    def equation(self, x, y):
        return (x - self.a) ** 2 + (y - self.b) ** 2 - self.r ** 2

    def test_belong(self, x, y):
        if self.equation(x, y) == 0:
            return f"point2: {x, y} belongs to the circle"
        return f"point2: {x, y} do not belong to the circle"


if __name__ == '__main__':
    C = Circle(1, 2, 1)
    print(C.perimeter())
    print(C.area())
    print(C.test_belong(1, 1))
