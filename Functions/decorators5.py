import time
import logging
from functools import wraps


def my_logger(original_function):
    logging.basicConfig(filename=f'decorators5.log', level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        print('log wrapper executed this before {} function'.format(original_function.__name__))
        logging.info(f'ran with args: {args}, kwrgs:{kwargs}')
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        print('timer wrapper executed this before {} function'.format(original_function.__name__))
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{original_function.__name__} ran in: {t2} sec')
        return result

    return wrapper


@my_logger
@my_timer
def display(name, city):
    time.sleep(1)
    print(f'display function : {name}, {city}')


# display = my_logger(my_timer(display))
# display = my_timer(display)
# display = my_logger(display)
display(name='Chandru', city="Bangalore")
