# if statement is used to test a specific condition. If the condition is true, a block of code will be executed
def function1(num):
    if num != 0:
        value = num // 2
        print(value)


function1(10)


# if-else statement is similar to if statement except the fact that, it also provides the block of the code for the
# false case of the condition to be checked.
# If the condition provided in the if statement is false, then the else statement will be executed
def function2(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')


function2(20)


# elif statement enables us to check multiple conditions and execute the specific block of statements depending upon
# the true condition among them. We can have any number of elif statements in our program depending upon our need
def function3(marks):
    if 85 < marks <= 100:
        print("grade A")
    elif 60 < marks <= 85:
        print("grade B")
    elif 40 < marks <= 60:
        print("grade C")
    elif 30 < marks <= 40:
        print("grade D")
    else:
        print("fail")


function3(58)


# Nested if statements enable us to use if-else statement inside an outer if statement
def function4(arg):
    if isinstance(arg, int):
        if arg % 2 == 0:
            print('even')
        else:
            print('odd')
    else:
        print(f'{arg} is not an integer')


function4(5)
