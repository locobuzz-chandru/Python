# Polymorphism is a programming term that refers to the use of the same function name, but with different signatures,
# for multiple types

# Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to
# provide a specific implementation of a method that is already provided by one of its super-classes or parent classes
class Vehicle:
    def fun1(self):
        return 'Vehicle is moving'


class Car(Vehicle):
    def fun1(self):
        avr = super().fun1()
        return avr


car = Car()
print(car.fun1())


# Two or more methods have the same name but different numbers of parameters or different types of parameters, or both.
# These methods are called overloaded methods and this is called method overloading
class Product:
    def multiply(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            product = a * b * c
        elif a is not None and b is not None:
            product = a * b
        else:
            product = a
        return product


obj = Product()
print(obj.multiply(2, 5, 4))
