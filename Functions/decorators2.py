def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {} function'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function  # returning function without executing it (return inner function waiting to be executed)


@decorator_function
def display(name, city):
    print(f'display function {name}, {city}')


# display = decorator_function(display)
display(name='Chandru', city="Bangalore")
