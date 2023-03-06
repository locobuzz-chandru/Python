# Write a function that takes an integer minutes and converts it to seconds.
# convert(5) ➞ 300

def function(min):
    sec = min * 60
    return sec


# print(function(5))

# Write a function that takes the base and height of a triangle and return its area.
def function1(base, height):
    area = 0.5 * base * height
    return area


# print(function1(base=10, height=15))

# Given a list, rotate the values clockwise by one (the last value is sent to the first position).
#
# rotate_by_one([1, 2, 3, 4, 5]) ➞ [5, 1, 2, 3, 4]

def function2():
    list_ = [1, 2, 3, 4, 5]
    a = [list_[-1]]
    b = list_[0:-1]
    c = a + b
    return c


print(function2())
