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


# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
def to_lower_case(string):
    ans = ""
    for c in string:
        n = ord(c)
        # 97 122 65 90 -> a, z, A, Z
        if 64 < n < 91:
            ans = ans + chr(n + 32)
        else:
            ans = ans + c
    return ans


# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error,
# one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and
# loss of another number. Return missing number and it's previous number
import re


def missing_num(list_):
    # bubble sort
    for i in range(len(list_) - 1, 0, -1):
        for j in range(i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
    for i in range(len(list_) - 1):
        if list_[i + 1] != list_[i] + 1:
            return f'{list_[i]}, {list_[i] + 1}'


# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have
# different values.
def find_pattern(n):
    if n > 1:
        print(bin(5), bin(10))
        return (n & (n >> 1)) == 0
    else:
        return False


# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
def count_chars(string):
    i = 0
    count = 0
    while i < len(string):
        if string[i] == '0':
            i += 1
        else:
            i += 2
        count += 1
    return count


# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of
# all the numbers strictly to the index's right.
def pivot_index(list_):
    total = sum(list_)
    left_sum = 0
    for index, number in enumerate(list_):
        if left_sum == (total - left_sum - number):
            return index
        left_sum += number
    return -1


# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
def is_toeplitz(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False
    return True


# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
# elements
def move_zero(arr):
    count = 0
    for i in arr:
        if i == 0:
            arr.remove(i)
            count = count + 1
    for i in range(count):
        arr.append(0)
    return arr


# Check if string1 and string2 are same, string2 is has rotated characters
def rotating_string(string1, string2):
    if len(string1) != len(string2):
        return 0
    temp = string1 + string1
    if temp.count(string2) > 0:
        return 1
    else:
        return 0


# Python program to print the numbers from a given number n till 0 using recursion
def print_till_zero(n):
    if n < 0:
        return
    print(n, end=' ')
    n = n - 1
    print_till_zero(n)


# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers
def rearrange_even_odd(arr):
    j = -1
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            j = j + 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    return arr


# Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
def substitute_colon():
    text = 'Python program to replace all occurrences of a space, comma, or dot with a colon'
    return re.sub(r"[ ,.]", ":", text)


# Write a Python program to remove all vowels from a given string.
def remove_vowels(text):
    return re.sub(r'[aeiou]+', ' ', text)


# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its
# binary representation.
def compliment(n):
    a = str(f'{n:b}')
    for i in range(len(a)):
        if a[i] == 1:
            a[i].replace('1', '0')
        else:
            a[i].replace('0', '1')
    return int(a, 2)


# Given a binary array nums, return the maximum number of consecutive 1's in the array.
def max_consecutive_ones(arr):
    max_one_count = 0
    for i in range(len(arr)):
        one_count = 0
        for j in range(i, len(arr)):
            if arr[j] == 1:
                one_count = one_count + 1
            else:
                break
        if one_count > max_one_count:
            max_one_count = one_count
    return max_one_count


# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and
# initial word order.
def reverse_words(s):
    return " ".join(s.split(" ")[::-1])[::-1]


# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such
# that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
def array_partition(list_):
    # bubble sort
    for i in range(len(list_) - 1, 0, -1):
        for j in range(i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
    result = 0
    for i in range(0, len(list_) - 1, 2):
        result += list_[i]
    return result


# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
def check_lower(str_):
    x = ""
    for i in str_:
        if i.isupper():
            x += i.lower()
        else:
            x += i
    return x


# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
def is_one_bit_character(list_):
    while len(list_) > 1:
        current = list_.pop(0)
        if current == 1:
            list_.pop(0)
    if len(list_) == 0:
        return False
    return list_[0] == 0


# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not
# banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
def most_common_word(str_, banned):
    str1 = str_.lower()
    list_ = list(str1.split(' '))
    while banned in list_:
        list_.remove(banned)
    set_ = set(list_)
    k = 0
    word_ = ''
    for word in set_:
        if list_.count(word) > k:
            k = list_.count(word)
            word_ = word
    return word_


from functools import reduce

from Algorithms.sort_merge import divide


# Recursive multiplication
def recursive_product(a, b):
    if a == 0 or b == 0:
        return 0
    if b == 1:
        return a

    return a + recursive_product(a, b - 1)


# Determine whether the largest element in the array is at least twice as much as every other number in the array.
# If it is, return the largest element, or return -1 otherwise.
def largest_num(arr):
    # merge sort
    arr = divide(arr)
    if arr[-1] >= (arr[-2] * 2):
        return arr[-1]
    return -1


# Write a Python program to create a string with no duplicate consecutive letters from a given string.
def no_consecutive_letters(txt):
    return txt[0] + ''.join(txt[i] for i in range(1, len(txt)) if txt[i] != txt[i - 1])


# You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
# There are at least two different characters in letters.
def smallest_greater_than_target(letters, target):
    letters.append(target)
    # merge sort
    letters = divide(letters)
    return letters[letters.index(target) + 1]


from functools import reduce
from Algorithms.sort_merge import divide


# Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums
# after separating them in the same order they appear in nums.
def divide_nums(arr):
    return list(''.join(list(map(str, arr))))


# You are given a 0-indexed array of string words and two integers left and right.
# Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].
def vowel_string(arr):  # ["are", "amy", "u"]
    vowels = ['a', 'e', 'i', 'o', 'u']
    return reduce(lambda x, y: x + y, list(map(lambda x: 1 if x[0] and x[-1] in vowels else 0, arr)))


# sort the squares of array
def squares(arr):
    list_ = list(map(lambda x: x * x, arr))
    return divide(list_)


# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
def add_integer(arr, k):
    return int(''.join(list(map(str, arr)))) + k


# If there exists more than one number in nums, pick the first element and last element in nums respectively and add
# the value of their concatenation to the concatenation value of nums, then delete the first and last element from nums.
# If one element exists, add its value to the concatenation value of nums, then delete it.
# Return the concatenation value of the nums.
def concatenation_sum(arr):  # [5, 14, 13, 8, 12]  # 512 + 22 + 13
    sum_ = 0
    while len(arr) != 0:
        if len(arr) == 1:
            sum_ = sum_ + int(arr[0])
            arr.remove(arr[0])
        else:
            sum_ = sum_ + int(str(arr[0]) + str(arr[-1]))
            arr.remove(arr[0])
            arr.remove(arr[-1])
    return sum_


if __name__ == '__main__':
    # print(day_of_date('2023/3/14'))
    # print(count__primes_nums(10))
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
    # print(intersection([1, 2, 2, 1], [2, 2, 1]))
    # print(to_lower_case('Hello'))
    # print(missing_num([1, 2, 6, 5, 3]))
    # print(find_pattern(10))
    # print(count_chars('11010'))
    # print(pivot_index([1, 7, 3, 6, 5, 6]))
    mat = [[6, 7, 8, 9],
           [4, 6, 7, 8],
           [1, 4, 6, 7],
           [0, 1, 4, 6],
           [2, 0, 1, 4]]
    # print(is_toeplitz(mat))
    # print(move_zero([1, 2, 0, 3, 0, 5]))
    # print(rotating_string('abcd', 'bcda'))
    # print_till_zero(8)
    # print(rearrange_even_odd([12, 10, 9, 45, 2, 10, 10, 45]))
    # print(substitute_colon())
    # print(remove_vowels('python'))
    # print(compliment(5))
    # print(max_consecutive_ones([1, 1, 0, 1, 1, 1]))
    # print(reverse_words('Hi I am Chandru'))
    # print(array_partition([1, 4, 3, 2]))
    # print(array_partition([6, 2, 6, 5, 1, 2]))
    # print(check_lower('Hello'))
    # print(is_one_bit_character([1, 0, 0]))
    # print(most_common_word('Bob hit a ball the hit BALL flew far after it was hit', 'hit'))
    # print(largest_num([3, 6, 1, 0]))
    # print("3 x 4 = {}".format(recursive_product(3, 4)))
    # print(no_consecutive_letters("hello"))
    # print(smallest_greater_than_target(letters=["c", "f", "j"], target="a"))
    # print(divide_nums([13, 25, 83, 77]))
    # print(vowel_string(["are", "amy", "u"]))
    # print(squares([-4, -1, 0, 3, 10]))
    # print(add_integer([1, 2, 0, 0], 34))
    # print(concatenation_sum([7, 52, 2, 4]))  # 74 + 522
    # print(concatenation_sum([5, 14, 13, 8, 12]))  # 512 + 22 + 13
    print(None)