class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('wrapper executed this before {} function'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display(name, city):
    print(f'display function {name}, {city}')


# display = DecoratorClass(display)
display(name='Chandru', city="Bangalore")
