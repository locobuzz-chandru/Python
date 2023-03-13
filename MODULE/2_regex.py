# Regular Expression is a sequence of characters that forms a search pattern

# RegEx is used to check if a string contains the specified search pattern

# findall-> Returns a list containing all matches. If no matches are found, an empty list is returned

# search-> Returns a Match object if there is a match anywhere in the string
# If there is more than one match, only the first occurrence of the match will be returned
# -> span, string, group

# split-> Returns a list where the string has been split at each match

# sub-> Replaces one or many matches with a string

import re


def fun1():
    txt = "regular expression, is a sequence of characters that forms a search pattern"
    x = re.findall("[k-o]", txt)
    return x


def fun2():
    txt = "regular 98 expression"
    x = re.findall("\d", txt)
    y = re.findall("\D", txt)
    return f'{x}, {y}'


def fun3():
    txt = """regular expression, is a sequence of characters that forms a search pattern"""
    x = re.findall("re...ar", txt)  # any char except new line
    return x


def fun4():
    txt = """regular expression, is a sequence of characters that forms a search pattern"""
    x = re.findall("^regu", txt)
    return x


def fun5():
    txt = """regular expression, is a sequence of characters that forms a search pattern"""
    x = re.findall("tern$", txt)
    return x


def fun6():
    txt = """regular expression, is a sequence of characters that forms a search pattern"""
    x = re.findall("reg..ar", txt)
    y = re.findall("e*ar", txt)  # zero or more
    z = re.findall("e+ar", txt)  # one or more
    return f'{x}, {y}, {z}'


def fun7():
    txt = """regular expression, is a sequence of characters that forms a search pattern"""
    x = re.findall("e?ar", txt)  # zero or one
    return x


def fun8():
    txt = """regular expression, is a sequence of characters that forms a search pattern"""
    x = re.findall("reg.{2}ar", txt)
    return x


def fun9():
    txt = """regular expression, is a sequence of characters that forms a search pattern"""
    x = re.findall("is|search|number|that", txt)
    return x


def fun10():
    txt = """regex, 98 is of char"""
    a = re.findall("\s", txt)  # space only
    b = re.findall("\S", txt)  # not space
    c = re.findall("\w", txt)  # words only
    d = re.findall("\W", txt)  # not words
    return f'{a}, {b}, {c}, {d}'


def fun11():
    txt = """A regular expression shortened as regex or regexp; sometimes referred to as rational expression is a 
    sequence of characters that specifies a match pattern in text. Usually such patterns are used by string-searching 
    algorithms for find or find and replace operations on strings, or for input validation"""
    x = re.findall(r"\bfin", txt)  # beginning of char
    y = re.findall(r"on\b", txt)  # end of char
    w = re.findall("on$", txt)  # end of string
    z = re.findall("on\Z", txt)  # end of string

    return f'{x},{y},{w},{z}'


if __name__ == "__main__":
    print(fun1())
    print(fun2())
    print(fun3())
    print(fun4())
    print(fun5())
    print(fun6())
    print(fun7())
    print(fun8())
    print(fun9())
    print(fun10())
    print(fun11())
