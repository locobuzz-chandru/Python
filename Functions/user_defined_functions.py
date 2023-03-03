# A function is a block of code which only runs when it is called.
# User defined functions -> Functions that we define ourselves to do certain specific task are UDF

# User-defined functions help to decompose a large program into small segments which makes program easy to
# understand, maintain and debug. If repeated code occurs in a program. Function can be used to include those codes
# and execute when needed by calling that function.

# A function can return data as a result.
def function1():
    return "Hi"


function1()


# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses.
# We can add as many arguments as we want, just separate them with a comma.
def function2(name):
    print(f"Name is {name}")


function2("Chandru")


# Chandru - argument
# name - parameter

# Types of Arguments -> Default arguments, Keyword arguments, Required arguments, Variable-length arguments

# function must be called with the correct number of arguments.
# We can also send arguments with the key = value syntax. Order of the arguments does not matter.
def function3(name, city, contact):
    print(f"Name is {name, city, contact}")


function3(name="Chandru", city="Bangalore", contact=123456)


# If we do not know how many arguments that will be passed into our function, add a * before the parameter name in
# the function definition. This way the function will receive a tuple of arguments, and can access the items accordingly
def function4(*args):
    print(f"Name is {args[1]}")


function4("A", "B", "C", "D")


# If we do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before
# the parameter name in the function definition. This way the function will receive a dictionary of arguments,
# and can access the items accordingly
def function5(**kwrgs):
    print(f"Name is {kwrgs['name'], kwrgs['city'], kwrgs['contact']}")


function5(name="Chandru", city="Bangalore", contact=123456)


# Using a default parameter value. If we call the function without argument, it uses the default value.
def function6(name=None):
    print(f"Name is {name}")


function6("Chandru")


# You can send any data types of argument to a function (string, number, list, dictionary etc.)
# it will be treated as the same data type inside the function.
def function7(food):
    for x in food:
        print(x)


fruits = ["A", "B", "C", "D"]
function7(fruits)


# function definitions cannot be empty, but if we for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
def function8():
    pass


function8()


# function recursion, which means a defined function can call itself, we can loop through data to reach a result
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


num = 3
print("The factorial of", num, "is", factorial(num))


# A lambda function is a special type of function without the function name.
# It can take any number of arguments, but can only have one expression
# Use lambda functions when an anonymous function is required for a short period of time
# syntax -> lambda arguments : expression
def function9():
    x = lambda a: a + 10
    print(x(5))


function9()


def function10():
    x = lambda a, b: a * b
    print(x(5, 6))


function10()


# Nested function -> refers to a function defined within another defined function.
# Inner functions can access the parameters of the outer scope.
# Inner functions are constructed to cover them from the changes that happen outside the function.
def function11():
    x = 10

    def function12():
        print(x)

    function12()


function11()
