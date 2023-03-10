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
        super().__init__(name, age)


# p = Child('John', 36)
# print(p.fun())


# Multiple level inheritance enables one derived class to inherit properties from more than one base class
class Parent1(object):
    def fun(self):
        print('Parent1 class')


class Parent2(object):
    def fun(self):
        print('Parent2 class')


class Child1(Parent2, Parent1):
    def fun(self):
        Parent1.fun(self)
        Parent2.fun(self)
        print('Child1 class')


c = Child1()
c.fun()
print(Child1.mro())


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


# obj1 = Child2()
# print(obj1.fun1(), obj1.fun2(), obj1.fun3())


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


# obj2 = Child3()
# print(obj2.fun1(), obj2.fun3())
# obj3 = Child3()
# print(obj3.fun1(), obj3.fun3())

# Method resolution order ->
# In multiple inheritance members of class are searched first in the current class. If not found, the search continues
# into parent classes in depth-first, let to right manner without searching the same class twice.
class Base1(object):
    def __init__(self):
        self.__str1 = "ABC"
        print("Base1", self.__str1)


class Base2(object):
    def __init__(self):
        self.__str1 = "XYZ"
        print("Base2", self.__str1)


class Derived(Base2, Base1):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        self.str1 = 'MNO'
        print("Derived")

    def print_strs(self):
        return f'{self.str1}'


# ob = Derived()
# ob._Base1__str1 = 'ABCD'
# ob._Base2__str1 = 'WXYZ'
# print(ob.print_strs())


class Class1:
    def __init__(self):
        super().__init__()
        print('Class1')


class Class2:
    def __init__(self):
        super().__init__()
        print('Class2')


class Class3(Class1, Class2):
    def __init__(self):
        super().__init__()
        print('Class3')

# obj_ = Class3()
