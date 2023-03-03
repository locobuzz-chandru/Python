# The Python interpreter has a number of functions and types built into it that are always available

# abs() function Returns the absolute value of a number
x = abs(-10.11)
print(x)

# all() function returns True if all items in an iterable are true, otherwise it returns False.
x = [0, 1, 1]
print(all(x))

# any()	Returns True if any item in an iterable object is true
x = [0, 1, 1]
print(any(x))

# The bin() function returns the binary version of a specified integer. The result will always start with the prefix 0b.
print(bin(14))
print(f'{14:#b}')
print(f'{14:b}')

# bool() function returns the boolean value of a specified object.
# Always return True, unless object is empty, like [], (), {}, False, 0, None
print(bool(1))
print(bool(0))


# callable() function returns True if the specified object is callable, otherwise it returns False
def x():
    pass


print(callable(x))


# classmethod()	Converts a method into a class method
class A:
    @classmethod
    def x(cls):
        pass


# complex() function returns a complex number by specifying a real number and an imaginary number
print(complex(3, 5))


# delattr()	Deletes the specified attribute (property or method) from the specified object
class Person:
    name = "John"
    age = 36
    country = "Norway"


delattr(Person, 'age')

# dict() function creates a dictionary
print(dict(a="A", b="B"))


# dir() function returns all properties, methods and built-in properties, without the values
class Person:
    name = "John"
    age = 36
    country = "Norway"


print(dir(Person))

# divmod() function returns a tuple containing the quotient  and the remainder
print(divmod(5, 2))

# enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object
# adds a counter as the key of the enumerate object
x = ('A', 'B', 'C')
y = enumerate(x)
print(list(y))

# filter() returns an iterator were the items are filtered through a function to test if the item is accepted or not
nums = [5, 12, 17, 18, 24, 32]


def even(x):
    if x % 2 == 0:
        return True
    return False


even_nums = filter(even, nums)

for x in even_nums:
    print(x)

# frozenset() function returns an unchangeable frozenset object
z = ["A", "B", "C", "D"]
z[1] = "x"
z = frozenset(z)


# getattr() function returns the value of the specified attribute
class Person:
    name = "John"
    age = 36
    country = "Norway"


x = getattr(Person, 'age', 'No attribute')
print(x)


# hasattr() function returns True if the specified object has the specified attribute, otherwise False
class Person:
    name = "John"
    age = 36
    country = "Norway"


x = hasattr(Person, 'age')
print(x)

# isinstance() function returns True if the specified object is of the specified type, otherwise False
print(isinstance("Hello", (float, int, str, list, dict, tuple)))
print(isinstance({1: 'a'}, dict))

# iter() function returns an iterator object
# next() function returns the next item in an iterator
x = iter(['a', 'b', 'c'])
print(next(x))
print(next(x))
print(next(x))

# len() function returns the number of items in an object
x = ['a', 'b', 'c']
print(len(x))

# list() function creates a list object
x = list(('a', 'b', 'c'))
print(x)


# map()	executes a specified function for each item in an iterable. The item is sent to the function as a parameter
def fun1(a):
    return len(a)


x = map(fun1, ('abcdef', 'klm46', 'xyz', '42589921476'))
print(list(x))


def fun2(a, b):
    return a + b


x = map(fun2, ('a', 'b', 'c'), ('1', '2', '3'))
print(list(x))

# max() function returns the item with the highest value, or the item with the highest value in an iterable
print(max(1, 20, 5, 8))
print(max('a', 'm', 'd', 'p'))

# min() function returns the item with the lowest value, or the item with the lowest value in an iterable
print(min(12, 8, 11, 25))
print(min('a', 'm', 'd', 'p'))

# pow() function returns the value of x to the power of y
print(pow(4, 3))
print(pow(4, 3, 5))  # ((4 * 4 * 4) % 5)

# range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and stops before a specified number
x = range(6)
for n in x:
    print(n)


# Python programming provides us with a built-in @property decorator which makes usage of getter and setters much
# easier in Object-Oriented Programming
class Num:
    def __init__(self):
        self._number = 100000

    @property
    def number(self):
        return self._number


n = Num()
print(n.number)

# round() function returns a floating point number that is a rounded version of the specified number
print(round(5.76543, 2))

# set() function creates a set object
print(set((1, 2, 3)))


# setattr() function sets the value of the specified attribute of the specified object
class Person:
    name = "John"
    age = 36
    country = "Norway"


setattr(Person, 'age', 40)

# slice object is used to specify how to slice a sequence
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = slice(1, 6, 2)
print(a[b])

# sorted() function returns a sorted list of the specified iterable object
print(sorted((5, 8, 2, 6, 10, 1)))


# staticmethod() Converts a method into a static method
class A:
    @staticmethod
    def a():
        print("ABCD")


A.a()


# super() function is used to give access to methods and properties of a parent or sibling class
class MyClass1:
    def __init__(self, txt):
        self.txt = txt

    def message(self):
        print(self.txt)


class MyClass2(MyClass1):
    def __init__(self, txt):
        super().__init__(txt)


my_class = MyClass2('Hi')
my_class.message()

# tuple() function creates a tuple object
print(tuple((1, 2, 3)))

# type() function returns the type of the specified object
a = {1: 'a'}
b = (1, 2)
c = 'b'
print(type(a))
print(type(b))
print(type(c))

# zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator
# is paired together, and then the second item in each passed iterator are paired together
a = ('a', 'b', 'c')
b = (1, 2, 3)
print(list(zip(a, b)))
