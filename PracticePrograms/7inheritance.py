# Create a Python class Person with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student  which inherits from the Person class and which also has a section attribute.
# Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# Create a student object via an instantiation on the Student class and then call displayStudent method.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f'name: {self.name}, age:{self.age}'


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def display_student(self):
        return f'name: {self.name}, age:{self.age}, section: {self.section}'


if __name__ == '__main__':
    p = Person("Chandru", 20)
    print(p.display())
    s = Student("Ajay", 21, "C")
    print(s.display_student())
