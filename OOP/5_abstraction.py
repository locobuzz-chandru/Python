# Abstraction is a process of handling complexity by hiding unnecessary information from the user
from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass


class Triangle(Polygon):
    def sides(self):
        print("Triangle has 3 sides")


class Pentagon(Polygon):
    def sides(self):
        print("Pentagon has 5 sides")


class Hexagon(Polygon):
    def sides(self):
        print("Hexagon has 6 sides")


class Square(Polygon):
    def sides(self):
        print("I have 4 sides")


t = Triangle()
t.sides()
s = Square()
s.sides()
p = Pentagon()
p.sides()
k = Hexagon()
k.sides()
