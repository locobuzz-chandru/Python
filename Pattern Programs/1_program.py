def star(n):
    for i in range(1, n + 1):
        for j in range(i):
            print('*', end='')
        print()


def reverse_star(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end='')
        print()


def number(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end='')
        print()


def reverse_num(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(i, end='')
        print()


def space_star(rows):
    for i in range(1, rows + 1):
        for j in range(rows, i, -1):
            print(' ', end=' ')
        for k in range(1, i + 1):
            print('*', end=' ')
        print()


def rev_space_star(rows):
    for i in range(rows, 0, -1):
        for j in range(rows, i, -1):
            print(' ', end=' ')
        for k in range(1, i + 1):
            print('*', end=' ')
        print()


def star_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, rows - i + 1):
            print(end=' ')
        for j in range(i):
            print('*', end=' ')
        print()


def rev_star_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(1, rows - i + 1):
            print(end=' ')
        for j in range(i):
            print('*', end=' ')
        print()


def star_diamond(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i), '* ' * i)
    for j in range(rows - 1, 0, -1):
        print(' ' * (rows - j), '* ' * j)


def space_similar_num(rows):
    for i in range(1, rows + 1):
        for j in range(rows, i, -1):
            print(' ', end=' ')
        for k in range(1, i + 1):
            print(i, end=' ')
        print()


def space_similar_rev_num(rows):
    for i in range(rows, 0, -1):
        for j in range(rows, i, -1):
            print(' ', end=' ')
        for k in range(1, i + 1):
            print(i, end=' ')
        print()


def space_num(rows):
    for i in range(1, rows + 1):
        for j in range(rows, i, -1):
            print(' ', end=' ')
        for k in range(1, i + 1):
            print(k, end=' ')
        print()


def rev_space_num(rows):
    for i in range(rows, 0, -1):
        for j in range(rows, i, -1):
            print(' ', end=' ')
        for k in range(i, 0, -1):
            print(k, end=' ')
        print()


def num_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()


def reverse_num_pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end='')
        print()


def rev_num_pattern(n):
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            print(j, end='')
        print()


def reverse_rev_num_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end='')
        print()


def incrementing_nums(rows):
    num = 1
    col = 1
    for i in range(1, rows + 1):
        for j in range(1, col + 1):
            print(num, end=' ')
            num = num + 1
        print()
        col = col + 2


def increment_decrement_nums(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        for k in range(j - 1, 0, -1):
            print(k, end=' ')
        print()


def star_hallow_diamond(rows=5):
    for row in range(rows):
        for col in range(rows):
            if row + col == 2 or col - row == 2 or row - col == 2 or row + col == 6:
                print('*', end='')
            else:
                print(end=' ')
        print()


if __name__ == "__main__":
    # n = int(input('Enter number of rows : '))
    # rev_star_pyramid(n)
    # star_pyramid(n)
    # space_similar_rev_num(n)
    # space_similar_num(n)
    # rev_space_num(n)
    # space_num(n)
    # rev_space_star(n)
    # space_star(n)
    # increment_decrement_nums(n)
    # incrementing_nums(n)
    # reverse_rev_num_pattern(n)
    # rev_num_pattern(n)
    # reverse_num_pattern(n)
    # num_pattern(n)
    # reverse_num(n)
    # star(n)
    # reverse_star(n)
    # star_diamond(n)
    # number(n)
    star_hallow_diamond()
