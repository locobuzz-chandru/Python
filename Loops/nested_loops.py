def function():
    names = ['A', 'B', 'C']
    for name in names:
        count = 0
        while count < 5:
            print(name, end=' ')
            count = count + 1
        print()


function()


def function2():
    first = [2, 4, 6]
    second = [2, 4, 6]
    for i in first:
        for j in second:
            if i == j:
                continue
            print(i, '*', j, '= ', i * j)


function2()


def function3():
    print('Perfect number fom 1 to 100')
    n = 2
    while n <= 100:
        x_sum = 0
        for i in range(1, n):
            if n % i == 0:
                x_sum += i
        if x_sum == n:
            print('Perfect number:', n)
        n += 1


function3()
