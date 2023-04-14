# Iterator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
# The iterator object is initialized using the iter() method. It uses the next() method for iteration.

# iterator is an object that contains a countable number of values, that can be iterated upon,
# we can traverse through all the values
# Lists, tuples, dictionaries, and sets are all iterable objects
def fun1():
    tup = ('a', 'b', 'c')
    string = "abcd"
    itr = iter(string)
    print(next(itr))
    print(next(itr))
    print(next(itr))


# fun1()


# __iter__() method must always return the iterator object itself
# __next__() method also allows us to do operations, and must return the next item in the sequence
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


# cls = MyNumbers()
# itr = iter(cls)
#
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# To prevent the iteration to go on forever, we can use the StopIteration statement
class MyNumbers1:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


# cls1 = MyNumbers1()
# itr1 = iter(cls1)
#
# for x in itr1:
#     print(x)


class PowTwo:
    def __init__(self, max_num=0):
        self.max_num = max_num

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max_num:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


numbers = PowTwo(3)


# i = iter(numbers)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# for i in PowTwo(3):
#     print(i)


# A sequence is a specific type of iterable that represents a linear sequence of elements

# Generator ----------------------------------------------------------------
# A generator is a special type of function which does not return a single value, instead, it returns an iterator object
# with a sequence of values. In a generator function, a yield statement is used rather than a return statement.

# Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in
# memory at once.

# When the generator function is called, it does not execute the function body immediately. Instead, it returns a
# generator object that can be iterated over to produce the values.

# The difference between yield and return is that yield returns a value and pauses the execution while maintaining the
# internal states, whereas the return statement returns a value and terminates the execution of the function
def square(number):
    for i in range(number):
        return i * i


def generator_square(number):
    for i in range(number):
        yield i * i


# print(square(9))
# print(list(generator_square(9)))

# gen = generator_square(5)
# while True:
#     try:
#         print(next(gen))
#     except StopIteration:
#         break


def pow_two_gen(max_num=0):
    n = 0
    while n < max_num:
        yield 2 ** n
        n += 1


# print(list(pow_two_gen(5)))
