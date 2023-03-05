# Switch Case is a selection control statement. The switch expression is evaluated once.
# The value of the expression is compared with the values of each case;
# if there is a match, the associated block of code is executed.

def number_to_string(arg):
    match arg:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
            return "does not exist"


argument = 4
print(number_to_string(argument))


def numbers_to_strings(arg):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(arg, "nothing")


argument = 0
print(numbers_to_strings(argument))
