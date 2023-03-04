def check(function):
    def wrapper(a, b):
        if a < b:
            a, b = b, a
        if b == 0:
            print('Can not divide by zero')
            return
        return function(a, b)

    return wrapper


@check
def division(a, b):
    print(a // b)


division(0, 20)
