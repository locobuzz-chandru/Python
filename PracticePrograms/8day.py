from datetime import date
import re


# python program to print day of a date
def day_of_date(str1):
    y, m, d = map(int, str1.split('/'))
    weeks = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    w = date.isoweekday(date(y, m, d))
    return f'Name of the date: {weeks[w]}'


# Python program to count the number of prime numbers
def count__primes_nums(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr


# Write a Python program to create a string with no duplicate consecutive letters from a given string.
def no_consecutive_letters(txt):
    return txt[0] + ''.join(txt[i] for i in range(1, len(txt)) if txt[i] != txt[i - 1])


# Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)


# Write a Python program to find the occurrence and position of substrings within a string.
def find_txt():
    text = 'Python exercises, Django exercises, SQL exercises'
    pattern = r'exercises'
    for match in re.finditer(pattern, text):
        s = match.start()
        e = match.end()
        print('%d:%d' % (s, e))


# Write a Python program to convert a camel-case string to a snake-case string.
def camel_to_snake(text):
    str1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', str1).lower()


# Python program to display the given integer in a reverse manner
def reverse_num(number):
    rev = 0
    while number != 0:
        digit = number % 10
        rev = (rev * 10) + digit
        number = number // 10
    return rev


# a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
def valid_brackets(s):
    left_symbols = []
    for c in s:
        if c in ['(', '{', '[']:
            left_symbols.append(c)
        elif c == ')' and len(left_symbols) != 0 and left_symbols[-1] == '(':
            left_symbols.pop()
        elif c == '}' and len(left_symbols) != 0 and left_symbols[-1] == '{':
            left_symbols.pop()
        elif c == ']' and len(left_symbols) != 0 and left_symbols[-1] == '[':
            left_symbols.pop()
        else:
            return False
    return left_symbols == []


def roman_to_integer(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman:
            num = num + roman[s[i:i + 2]]
            i += 2
        else:
            num = num + roman[s[i]]
            i += 1
    return num


def integer_to_roman(num):
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // value[i]):
            roman_num = roman_num + symbol[i]
            num = num - value[i]
        i = i + 1
    return roman_num


# add two binary numbers
def add_binary_strings(a, b):
    return '{:b}'.format(int(a, 2) + int(b, 2))


# Given an array of strings, group the anagrams together. You can return the answer in any order.
def anagrams(li):
    dictionary = {}
    for word in li:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in dictionary:
            dictionary[sorted_word] = [word]
        else:
            dictionary[sorted_word] = dictionary[sorted_word] + [word]
    return [dictionary.values()]


# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
# integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer
# does not contain any leading 0's.
def plus_one(digits):
    index = len(digits) - 1
    while index >= 0 and digits[index] == 9:
        digits[index] = 0
        index -= 1
    if index < 0:
        digits.insert(0, 1)
    else:
        digits[index] += 1
    return digits


# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
def climb_stairs(n):
    if n < 2:
        return 1
    else:
        return climb_stairs(n - 1) + climb_stairs(n - 2)


# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
# numbers.
def palindrome(string):
    if string == string[::-1]:
        return "palindrome"
    else:
        return "not a palindrome"


# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
def generate(result, s, open_, close, n):
    if open_ == n and close == n:
        result.append(s)
        return
    if open_ < n:
        generate(result, s + "(", open_ + 1, close, n)
    if close < open_:
        generate(result, s + ")", open_, close + 1, n)


def generate_parenthesis(n):
    result = []
    generate(result, "", 0, 0, n)
    return result


# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
# always exists in the array.
def majority_element(nums):
    count = 0
    x = 0
    for num in nums:
        if count == 0:
            x = num
        if num == x:
            count = count + 1
        else:
            count = count - 1
    return x


# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
# element is distinct.
def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(0, i):
            if nums[i] == nums[j]:
                return True
    return False


# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
def digit_sum(n):
    if n == 0:
        return 0
    if n % 9 == 0:
        return 9
    else:
        return n % 9


# Write a function that reverses a string. The input string is given as an array of characters s.
def reverse_list(list_):
    start = 0
    end = len(list_) - 1
    while start < end:
        list_[start], list_[end] = list_[end], list_[start]
        start += 1
        end -= 1
    return list_


# Given an integer n, return true if n is a perfect number.
def perfect_number(n):
    sum_ = 0
    for x in range(1, n):
        if n % x == 0:
            sum_ = sum_ + x
    return sum_ == n


# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
def single_number(nums):
    if not isinstance(nums, list):
        raise ValueError
    for i in range(len(nums)):
        if nums.count(nums[i]) == 1:
            return nums[i]


# Given a string s consisting of words and spaces, return the length of the last word in the string.
def last_word(string):
    count = 0
    for i in range(len(string) - 1, -1, -1):
        if string[i] == ' ':
            break
        count += 1
    return count


# Given a string s, reverse only all the vowels in the string and return it.
def reverse_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    i, j = 0, len(string) - 1
    char = list(string)
    while i < j:
        if char[i] not in vowels:
            i += 1
            continue
        if char[j] not in vowels:
            j -= 1
            continue
        char[i], char[j] = char[j], char[i]
        i += 1
        j -= 1
    return ''.join(char)


# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be
# unique and you may return the result in any order.
def intersection(list1, list2):
    intersect1 = [num for num in list1 if num in list2]
    intersect2 = [num for num in list2 if num in list1]

    if len(intersect1) < len(intersect2):
        return intersect1
    else:
        return intersect2


if __name__ == '__main__':
    # print(day_of_date('2023/3/14'))
    # print(count__primes_nums(10))
    # print(no_consecutive_letters("PPYYYTTHON"))
    # print(change_date_format('2023-03-16'))
    # find_txt()
    # print(camel_to_snake('PythonProgramming'))
    # print(reverse_num(958))
    # print(palindrome('gadag'))
    # print(valid_brackets(s="()[]{}"))
    # print(roman_to_integer("CDXLIII"))
    # print(integer_to_roman(1520))
    # print(add_binary_strings('11', '1'))
    # print(anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # print(plus_one([1, 7, 8, 9]))
    # print(climb_stairs(3))
    # print(palindrome('Too hot to hoot'))
    # print(generate_parenthesis(3))
    # print(majority_element([3, 2, 3]))
    # print(contains_duplicate([5, 2, 1, 6, 5]))
    # print(digit_sum(183))
    # print(reverse_list(["h", "e", "l", "l", "o"]))
    # print(perfect_number(6))
    # print(single_number([2, 2, 1]))
    # print(last_word('Hello World'))
    # print(reverse_vowels('hello'))
    print(intersection([1, 2, 2, 1], [2, 2, 1]))
