# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error,
# one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and
# loss of another number.
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


if __name__ == '__main__':
    # print(missing_num([1, 2, 6, 5, 3]))
    # print(find_pattern(10))
    # print(to_lower_case('Hello'))
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
    print(remove_vowels('python'))
