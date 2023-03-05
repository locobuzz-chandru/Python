# for loop-> is used in the case where a programmer needs to execute a part of the code until the given condition is
# satisfied. It is best to use for loop if the number of iterations is known in advance

def function1():
    tuple_ = (3, 4, 6, 8, 9, 2, 3, 8, 9, 7)
    for value in tuple_:
        if value % 2 == 0:
            print(f'even {value}', end=' ')
        print(f"odd {value}", end=' ')
    print()


function1()


def function2():
    for i in range(10):
        print(i, end=' ')
    print()


function2()
