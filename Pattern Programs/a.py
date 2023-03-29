# Create a function that takes a string's characters as ASCII and returns each character's hexadecimal value as a string
# Examples
# convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"
# convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"
# convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"
def convert_to_hex(str_):
    list_ = list(str_)
    list1 = [ord(list_[i]) for i in range(len(list_))]
    list2 = [hex(list1[i])[2:] for i in range(len(list1))]
    return ' '.join(list2)


# Given a name, return the letter with the highest index in alphabetical order, with its corresponding index,
# in the form of a string. You are prohibited to use max() nor is reassigning a value to the alphabet list allowed.
#
# Examples
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
# "v", "w", "x", "y", "z"]
# alphabet_index(alphabet, "Flavio") ➞ "22v"
# alphabet_index(alphabet, "Andrey") ➞ "25y"
# alphabet_index(alphabet, "Oscar") ➞ "19s
def alphabet_index(list_, str_):
    list2 = [ord(i) for i in str_]
    # bubble sort
    for i in range(len(list2) - 1, 0, -1):
        for j in range(i):
            if list2[j] > list2[j + 1]:
                list2[j], list2[j + 1] = list2[j + 1], list2[j]
    return f'{list_.index(chr(list2[-1])) + 1}{chr(list2[-1])}'


# Your spouse is not concerned with the loss of material possessions but rather with his/her favorite pet. Is it gone?!
# Given a dictionary of the stolen items and a string in lowercase representing the name of the pet (e.g. "rambo"),
# return:
# "Rambo is gone..." if the name is on the list.
# "Rambo is here!" if the name is not on the list.
# Note that the first letter of the name in the return statement is capitalized.
def fun(dict_, a):
    if a in dict_.keys():
        return f'{a.capitalize()} is gone'
    return f'{a.capitalize()} is here'


if __name__ == '__main__':
    print(convert_to_hex("hello world"))
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    print(alphabet_index(alphabet, "Flavio"))
    print(fun({'rambo': 1, 'car': 2, 'cup': 3}, 'rambo'))


# list_ = [list_.append(symbol + i + symbol) for i in string.split(' ') if
#          i.lower() == word.lower() else list_.append(i)]

# Create a class with a few functions like these examples.
# magic.replace("string", 'char', char') is a function that replaces all of the specified characters with different
# specified characters.
# magic.str_length("string") is a function that returns the length of the string.
# magic.trim(" string ") is a function that returns a string with truncated spaces at both the beginning and end.
# magic.list_slice(list, tuple) is a function that returns the items in the list that are between the specified indexes.
# If the length of the new list is 0, return -1.
# Examples
# magic.replace("AzErty-QwErty", "E", "e") ➞ "Azerty-Qwerty"
# magic.str_length("hello world") ➞ 11
# magic.trim("      python is awesome      ") ➞ "python is awesome"
# magic.list_slice([1, 2, 3, 4, 5], (2, 4)) ➞ [ 2, 3, 4 ]
class Magic:
    @staticmethod
    def replace(string, char, char1):
        return string.replace(char, char1)

    @staticmethod
    def str_length(string):
        return len(string)

    @staticmethod
    def trim(string):
        return string.strip()

    @staticmethod
    def list_slice(list_, tuple_):
        return list_[tuple_[0] - 1: tuple_[-1]]


# October 22nd is CAPS LOCK DAY. Apart from that day, every sentence should be lowercase, so write a function to
# normalize a sentence.
# Create a function that takes a string. If the string is all uppercase characters, convert it to lowercase and add an
# exclamation mark at the end.
# Examples
# normalize("CAPS LOCK DAY IS OVER") ➞ "Caps lock day is over!"
# normalize("Today is not caps lock day.") ➞ "Today is not caps lock day."
# normalize("Let us stay calm, no need to panic.") ➞ "Let us stay calm, no need to panic."
def normalize(str_):
    if str_.isupper():
        str_ = str_.capitalize() + '!'
    return str_


# Given a string, reverse all the words which have odd length. The even length words are not changed.
# Examples
# reverse_odd("Bananas") ➞ "sananaB"
# reverse_odd("One two three four") ➞ "enO owt eerht four"
# reverse_odd("Make sure uoy only esrever sdrow of ddo length") ➞ "Make sure you only reverse words of odd length"
def reverse_odd(str_):
    list_ = list(str_.split(' '))
    list1 = []
    for i in list_:
        if len(i) % 2 == 0:
            list1.append(i)
        else:
            list1.append(i[::-1])
    return list1


# you can surround text with asterisks, double asterisks, underscores and tildes to add formatting to certain words.
# Complete the function markdown() so it takes a symbol as input, and returns a function which applies that formatting
# to a given word in a given sentence.
# Examples
# italicise = markdown("*")
# italicise("Hello there!", "Hello") ➞ "*Hello* there!"
# italicise("The tale of the two sparrows", "the") ➞ "*The* tale of *the* two sparrows"
# italicise("Include punctuation!", "punctuation") ➞ "Include *punctuation!*"
# inline = markdown("`")
# inline("Remember to return as a boolean value.", "boolean") ➞ "Remember to return as a `boolean` value."
# inline("I want you to create the class Programmer...", "PROGRAMMER") ➞ "I want you to create the class `Programmer...
# inline("Do not forget to return the value", "return") ➞ "Do not forget to `return` the value"
class Markdown:
    def __init__(self, symbol):
        self.symbol = symbol

    def __call__(self, string, word):
        if word.lower() in string.lower().split(' '):
            list_ = []
            for i in string.split(' '):
                if i.lower() == word.lower():
                    str_ = self.symbol + i + self.symbol
                    list_.append(str_)
                else:
                    list_.append(i)
            return ' '.join(list_)


# italicise = Markdown("*")
# print(italicise("Hello there!", "Hello"))
# inline = Markdown("`")
# print(inline("Do not forget to return the value", "return"))


def markdown(symbol):
    def italicise(string, word):
        if word.lower() in string.lower().split(' '):
            list_ = []
            for i in string.split(' '):
                if i.lower() == word.lower():
                    list_.append(symbol + i + symbol)
                else:
                    list_.append(i)
            return ' '.join(list_)

    return italicise


if __name__ == '__main__':
    italicise = markdown("*")
    print(italicise("Hello there!", "Hello"))
    # magic = Magic()
    # print(magic.replace("AzErty-QwErty", "E", "e"))
    # print(magic.str_length("hello world"))
    # print(magic.trim("      python is awesome      "))
    # print(magic.list_slice([1, 2, 3, 4, 5], (2, 4)))
    # print(normalize("CAPS LOCK DAY IS OVER"))
    # print(normalize("Today is not caps lock day."))
    # print(normalize("Let us stay calm, no need to panic."))
    # print(reverse_odd("Make sure uoy only esrever sdrow of ddo length"))
    # print(reverse_odd("One two three four"))


# The volume of a spherical shell is the difference between the enclosed volume of the outer sphere and the enclosed
# volume of the inner sphere:
# V=(4/3) * pi(R^3 - r^3)
# Create a function that takes r1 and r2 as arguments and returns the volume of a spherical shell rounded to the nearest
# thousandth.
# Examples
# vol_shell(3, 3) ➞ 0
# vol_shell(7, 2) ➞ 1403.245
# vol_shell(3, 800) ➞ 2144660471.753
def vol_shell(r2, r1):
    list1 = str((4 / 3) * (22 / 7) * ((r2 ** 3) - (r1 ** 3))).split('.')
    return list1[0] + '.' + list1[1][:3]


vol_shell(7, 2)
print(vol_shell(3, 800))


# Write a function that transforms a list of characters into a list of dictionaries, where:
#
# The keys are the characters themselves.
# The values are the ASCII codes of those characters.
# Examples
# to_dict(["a", "b", "c"]) ➞ [{"a": 97}, {"b": 98}, {"c": 99}]
# to_dict(["^"]) ➞ [{"^": 94}]
# to_dict([]) ➞ []
def to_dict(lst):
    return [{lst[i]: ord(lst[i])} for i in range(len(lst))]


print(to_dict(["a", "b", "c"]))
print(to_dict(["^"]))
print(to_dict([]))


# Write a function that takes coordinates of two points on a two-dimensional plane and returns the length of the line
# segment connecting those two points.
#
# Examples
# line_length([15, 7], [22, 11]) ➞ 8.06
# line_length([0, 0], [0, 0]) ➞ 0
# line_length([0, 0], [1, 1]) ➞ 1.41
#
# Note:
# use operator for exponent value
def line_length(lst1, lst2):
    x1, x2 = lst1[0], lst1[1]
    y1, y2 = lst2[0], lst2[1]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


print(line_length([15, 7], [22, 11]))
print(line_length([0, 0], [1, 1]))

# sqrt((a2 - b2) +
# x2 - x1 ^ 2 + y2 - y1 ^ 2 , ^ 0.5

# Create a function that takes in a list of intervals and returns how many intervals overlap with a given point.
#
# An interval overlaps a particular point if the point exists inside the interval, or on the interval's boundary.
# For example the point 3 overlaps with the interval [2, 4] (it is inside) and [2, 3] (it is on the boundary).
# To illustrate:
#     count_overlapping([[1, 2], [2, 3], [1, 3], [4, 5], [0, 1]], 2) ➞ 3
#     # Since [1, 2], [2, 3] and [1, 3] all overlap with point 2
#
# Examples
# count_overlapping([[1, 2], [2, 3], [3, 4]], 5) ➞ 0
# count_overlapping([[1, 2], [5, 6], [5, 7]], 5) ➞ 2
# count_overlapping([[1, 2], [5, 8], [6, 9]], 7) ➞ 2
from functools import reduce


def count_overlapping(l1, num):
    count = 0
    l2 = list(map(lambda x: range(x[0], x[1] + 1), l1))
    return sum(list(map(lambda x: count + 1 if num in x else count, l2)))
    # return reduce(lambda x, y: x + y, list(map(lambda x: count + 1 if num in x else count, l2)))


print(count_overlapping([[1, 2], [2, 3], [3, 4]], 5))
print(count_overlapping([[1, 2], [5, 6], [5, 7]], 5))
print(count_overlapping([[1, 2], [5, 8], [6, 9]], 7))

# Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
# Examples
# format_date("11/12/2019") ➞ "20191211"
# format_date("12/31/2019") ➞ "20193112"
# format_date("01/15/2019") ➞ "20191501"
from datetime import datetime
from functools import reduce


def format_date(str_):
    c = str(datetime.strptime(str_, '%m/%d/%Y').date()).split('-')
    c[-1], c[-2] = c[-2], c[-1]
    return ''.join(c)


# Write a function that takes a list of numbers and returns a list with two elements:
# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.
# Example
# sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9] # 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
# sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])
# sum_odd_and_even([0, 0]) ➞ [0, 0])


def sum_odd_and_even(arr):
    if not all(arr):
        return arr
    return [reduce(lambda x, y: x + y, list(filter(lambda x: x % 2 == 0, arr))),
            reduce(lambda x, y: x + y, list(filter(lambda x: x % 2 != 0, arr)))]


# Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a
# dictionary of objects like { "name": "John", "top_note": 5 }.
# Examples
# top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }
# top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }
# top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }
def top_note(dict_):
    list_ = dict_.get('notes')
    # bubble sort
    for i in range(len(list_) - 1, 0, -1):
        for j in range(i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
    dict_.update(top_note=list_[-1])
    dict_.pop('notes')
    return dict_


# Write a function that accepts the height and width (m, n) and an optional proc s and generates a list with m elements.
# Each element is a string consisting of either:
# The default character (hash #) repeating n times (if no proc is given).
# The character passed in through the proc repeating n times.
# Examples
# make_rug(3, 5, '#') ➞ [
#   "#####",
#   "#####",
#   "#####"
# ]
# make_rug(3, 5, '$')  ➞ [
#   "$$$$$",
#   "$$$$$",
#   "$$$$$"
# ]
# make_rug(2, 2, 'A')  ➞ [
#   "AA",
#   "AA"
# ]
def make_rug(m, n, s='#'):
    for i in range(m):
        for j in range(n):
            print(s, end='')
        print()


# A list is given. Return a new list having the sum of all its elements except itself. For more clarity, check the
# examples below.
#
# Clarification
# [1, 2, 3, 4] = for first element => sum will be 2+3+4 = [9]
# [1, 2, 3, 4] = for second element => sum will be 1+3+4 = [9, 8]
# [1, 2, 3, 4] = for third element => sum will be 1+2+4 = [9, 8, 7]
# [1, 2, 3, 4] = for fourth element => sum will be 1+2+3 = [9, 8, 7, 6]
# Examples
# lst_ele_sum([1, 2, 3, 2, 1]) ➞ [8, 7, 6, 7, 8]
# lst_ele_sum([1, 2]) ➞ [2, 1]
# lst_ele_sum([1, 2, 3]) ➞ [5, 4, 3]
# lst_ele_sum([1, 2, 3, 4, 5]) ➞ [14, 13, 12, 11, 10]
# lst_ele_sum([10, 20, 30, 40, 50, 60]) ➞ [200, 190, 180, 170, 160, 150]
from functools import reduce


def lst_ele_sum(arr):
    list_ = []
    sum_list = []
    for i in range(len(arr)):
        list_.append(arr[i])
        arr.remove(arr[i])
        sum_ = reduce(lambda x, y: x + y, arr)
        sum_list.append(sum_)
        arr.insert(i, list_[0])
        list_.clear()
    return sum_list


if __name__ == '__main__':
    print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
    print(format_date("11/12/2019"))
    print(top_note({"name": "John", "notes": [3, 5, 4]}))
    make_rug(3, 5, '$')
    print(lst_ele_sum([10, 20, 30, 40, 50, 60]))
