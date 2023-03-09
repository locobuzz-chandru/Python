# A class method is a method that is bound to the class and not the object of the class
# They have the access to the state of the class as it takes a class parameter that points to the class
# it can modify a class state that would apply across all the instances of the class

# A static method is also a method that is bound to the class and not the object of the class
# This method can’t access or modify the class state
# generally use static methods to create utility functions

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        if age > 18:
            return True
        else:
            return False

    @classmethod
    def emp_from_year(cls, name, age):
        return cls(name, age)

    def __str__(self):
        return 'Employee Name: {} and Age: {}'.format(self.name, self.age)


e1 = Employee('Ram', 25)
print(e1)
e2 = Employee.emp_from_year('John', 36)
print(e2)
print(Employee.is_adult(25))
print(Employee.is_adult(16))
