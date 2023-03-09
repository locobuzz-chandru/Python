# Inheritance allows us to define a class that inherits all the methods and properties from another class

# Single inheritance is when child class is derived from only one parent class

# Parent class
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun(self):
        return f'Name: {self.name}, Age: {self.age}'


# Child class
class Child(Parent):
    def __init__(self, name, age):
        Parent.__init__(self, name, age)


p = Child('John', 36)
print(p.fun())


# Multiple level inheritance enables one derived class to inherit properties from more than one base class
class Parent1:
    def fun1(self):
        return 'Parent1 class'


class Parent2:
    def fun2(self):
        return 'Parent2 class'


class Child1(Parent1, Parent2):
    def fun3(self):
        return 'Child1 class'


c = Child1()
print(c.fun1(), c.fun2(), c.fun3())


# Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn
# inherits properties from his parent class
class Parent3:
    def fun1(self):
        return 'Parent3 class'


class Parent4(Parent3):
    def fun2(self):
        return 'Parent4 class'


class Child2(Parent4):
    def fun3(self):
        return 'Child2 class'


obj1 = Child2()
print(obj1.fun1(), obj1.fun2(), obj1.fun3())


# Hierarchical level inheritance enables more than one derived class to inherit properties from a parent class
class Parent5:
    def fun1(self):
        return 'Parent5 class'


class Parent6(Parent5):
    def fun2(self):
        return 'Parent6 class'


class Child3(Parent5):
    def fun3(self):
        return 'Child3 class'


obj2 = Child3()
print(obj2.fun1(), obj2.fun3())
obj3 = Child3()
print(obj3.fun1(), obj3.fun3())
