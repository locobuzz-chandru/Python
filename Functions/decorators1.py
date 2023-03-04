# decorator-> function that takes another fun as an argument and extends its behavior without explicitly modifying it.
# decorator-> it allows programmers to modify the behaviour of a function or class


def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {} function'.format(original_function.__name__))
        return original_function()

    return wrapper_function  # returning function without executing it (return inner function waiting to be executed)


# @decorator_function
def display():
    print('display function')


display = decorator_function(display)
display()  # decorator_function(display)()
