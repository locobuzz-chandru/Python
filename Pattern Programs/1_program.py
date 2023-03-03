def star():
    n = int(input("Enter number of rows to be displayed: "))
    for i in range(1, n + 1):
        for j in range(i):
            print('*', end='')
        print()


# star()


def reverse_star():
    n = int(input("Enter number of rows to be displayed: "))
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end='')
        print()


# reverse_star()

def number():
    n = int(input("Enter number of rows to be displayed: "))
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end='')
        print()


# number()

def reverse_num():
    n = int(input("Enter number of rows to be displayed: "))
    for i in range(n, 0, -1):
        for j in range(i):
            print(i, end='')
        print()


# reverse_num()

def num_pattern():
    n = int(input("Enter number of rows to be displayed: "))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()


# num_pattern()

def reverse_num_pattern():
    n = int(input("Enter number of rows to be displayed: "))
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end='')
        print()


# reverse_num_pattern()


def rev_num_pattern():
    n = int(input("Enter number of rows to be displayed: "))
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            print(j, end='')
        print()


# rev_num_pattern()


def reverse_rev_num_pattern():
    n = int(input("Enter number of rows to be displayed: "))
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end='')
        print()


# reverse_rev_num_pattern()
