#  Higher Order Function-> a function that either accepts a function as an argument or returns a function
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def function(func):
    print(func(10, 5))


function(add)
function(sub)


def divisor(x):
    def dividend(y):
        return y / x

    return dividend

# divide = divisor(2)
# print(divide(10))
