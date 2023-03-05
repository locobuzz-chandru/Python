# continue-> skips the current iteration of the loop and the control flow of the program goes to the next iteration

def function():
    for i in range(8):
        if i == 3:
            continue
        print(i, end=' ')
    print()


function()


def function2():
    num = 0
    while num < 10:
        num += 1

        if (num % 2) == 0:
            continue

        print(num, end=' ')
    print()


function2()
