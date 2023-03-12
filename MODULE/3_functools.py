from functools import reduce, total_ordering, cached_property


@total_ordering
class Car:
    def __init__(self, name, milage):
        self.name = name
        self.milage = milage

    def __eq__(self, other):
        return self.milage == other.milage

    def __lt__(self, other):
        return self.milage < other.milage


class Marks:
    def __init__(self, *grades):
        self.grades = grades

    @cached_property
    def total(self):
        return sum(self.grades)

    @cached_property
    def average(self):
        return self.total // len(self.grades)


def fun1():
    list_ = [1, 2, 3, 4, 5]
    return reduce(lambda x, y: x + y, list_, 10)


if __name__ == "__main__":
    # c1 = Car('Audi', 25)
    # c2 = Car('Benz', 28)
    # c3 = Car('BMW', 25)
    # print(c1 > c2, c1 == c3, c2 >= c1)
    # print(fun1())
    marks = Marks(10, 12, 15)
    print(marks.grades, marks.total, marks.average)