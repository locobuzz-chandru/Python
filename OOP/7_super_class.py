# The super() function is used to give access to methods and properties of a parent or sibling class.

# The super() function returns an object that represents the parent class

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        return f'{self.firstname}, {self.lastname}'


class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.graduation_year = 2019


x = Student("Mike", "Olsen")
print(x.printname())
print(x.graduation_year)
