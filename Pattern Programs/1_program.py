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

def incrementing_nums():
    rows = int(input("Enter number of rows to be displayed: "))
    num = 1
    col = 1
    for i in range(1, rows + 1):
        for j in range(1, col + 1):
            print(num, end=' ')
            num = num + 1
        print()
        col = col + 2


# incrementing_nums()


def increment_decrement_nums():
    rows = int(input("Enter number of rows to be displayed: "))
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        for k in range(j - 1, 0, -1):
            print(k, end=' ')
        print()


# increment_decrement_nums()

def space_star():
    rows = int(input("Enter number of rows to be displayed: "))
    for i in range(1, rows + 1):
        for j in range(rows, i, -1):
            print(' ', end=' ')
        for k in range(1, i + 1):
            print('*', end=' ')
        print()


# space_star()


def rev_space_star():
    rows = int(input("Enter number of rows to be displayed: "))
    for i in range(rows, 0, -1):
        for j in range(rows, i, -1):
            print(' ', end=' ')
        for k in range(1, i + 1):
            print('*', end=' ')
        print()


# rev_space_star()

def space_num():
    rows = int(input("Enter number of rows to be displayed: "))
    for i in range(1, rows + 1):
        for j in range(rows, i, -1):
            print(' ', end=' ')
        for k in range(1, i + 1):
            print(k, end=' ')
        print()


# space_num()


def rev_space_num():
    rows = int(input("Enter number of rows to be displayed: "))
    for i in range(rows, 0, -1):
        for j in range(rows, i, -1):
            print(' ', end=' ')
        for k in range(i, 0, -1):
            print(k, end=' ')
        print()


# rev_space_num()


def space_similar_num():
    rows = int(input("Enter number of rows to be displayed: "))
    for i in range(1, rows + 1):
        for j in range(rows, i, -1):
            print(' ', end=' ')
        for k in range(1, i + 1):
            print(i, end=' ')
        print()


# space_similar_num()


def space_similar_rev_num():
    rows = int(input("Enter number of rows to be displayed: "))
    for i in range(rows, 0, -1):
        for j in range(rows, i, -1):
            print(' ', end=' ')
        for k in range(1, i + 1):
            print(i, end=' ')
        print()


# space_similar_rev_num()


def star_pyramid():
    rows = int(input("Enter number of rows to be displayed: "))
    for i in range(1, rows + 1):
        for j in range(1, rows - i + 1):
            print(end=' ')
        for j in range(i):
            print('*', end=' ')
        print()


# star_pyramid()


def rev_star_pyramid():
    rows = int(input("Enter number of rows to be displayed: "))
    for i in range(rows, 0, -1):
        for j in range(1, rows - i + 1):
            print(end=' ')
        for j in range(i):
            print('*', end=' ')
        print()


# rev_star_pyramid()


def star_diamond():
    r = int(input("Enter number of rows to be displayed: "))
    rows = r // 2
    for i in range(1, rows + 1):
        print(' ' * (rows - i), '* ' * (i))
    for j in range(rows - 1, 0, -1):
        print(' ' * (rows - j), '* ' * (j))


star_diamond()
