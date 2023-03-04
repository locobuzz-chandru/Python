def decorator1(function):
    def wrapper(*args, **kwargs):
        a = function(*args, **kwargs)
        return a * 5

    return wrapper


def decorator2(function):
    def wrapper(*args, **kwargs):
        a = function(*args, **kwargs)
        return a + 5

    return wrapper


# @decorator2
# @decorator1
def number():
    return 10


number = decorator2(decorator1(number))
print(number())
