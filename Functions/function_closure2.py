import logging

logging.basicConfig(filename='function_closure2.log', level=logging.INFO)


def logger(function):
    def log_function(*args):
        logging.info(f'Ran with {function.__name__, args}')
        print(function(*args))

    return log_function


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(4, 5)
sub_logger(10, 5)
