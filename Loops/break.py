# break-> Terminates the loop statement and transfers execution to the statement immediately following the loop

def function():
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1


function()


def function1():
    i = 1
    while i <= 10:
        print('6 * ', i, '=', 6 * i)
        if i >= 5:
            break
        i = i + 1


function1()
