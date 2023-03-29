import collections
from functools import reduce


# 1207) Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or
# false
# otherwise.
def occurrences(arr):
    set_ = set(arr)
    if len(set_) == 1:
        return True
    list_ = list(map(lambda x: arr.count(x), set_))
    if len(set(list_)) == 1:
        return False
    list1 = set(list(map(lambda x: list_.count(x), list_)))
    if len(list1) == 1:
        return True
    return False


# 1281) Given an integer number n, return the difference between the product of its digits and the sum of its digits.
def maths(n):
    list_ = list(str(n))
    sum_ = reduce(lambda x, y: int(x) + int(y), list_)
    multiplication = reduce(lambda x, y: int(x) * int(y), list_)
    return multiplication - sum_


# 1089) Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to
# the right.
def remove_duplicates(arr):
    list1 = []
    for i in arr:
        if i == 0:
            list1.append(0)
            list1.append(0)
        else:
            list1.append(i)
    length = len(list1) - len(arr)
    for i in range(length):
        list1.pop()
    return list1


def element(arr):
    set_ = set(arr)
    for i in set_:
        a = arr.count(i)
        percentage25 = (len(arr) * 25) / 100
        if a > percentage25:
            return i


# 1295) Given an array nums of integers, return how many of them contain an even number of digits.
def even_digits(nums):
    list1 = [str(i) for i in nums]
    count = 0
    for i in list1:
        a = len(i)
        if a % 2 == 0:
            count += 1
    return count


# 1299) Given an array arr, replace every element in that array with the greatest element among the elements to its
# right, and replace the last element with -1.
def replace_index(arr):
    for i in range(len(arr)):
        if i < len(arr) - 1:
            right_arr = arr[i + 1:]
            right_arr.sort()
            arr[i] = right_arr[-1]
        else:
            arr[i] = -1
    return arr


# 1313. Decompress Run-Length Encoded List
def decompress(arr):
    list1 = []
    start = 0
    for i in range((len(arr) // 2)):
        list1.append(arr[start:start + 2])
        start += 2
    print(list1)
    list2 = []
    for i in list1:
        for j in range(i[0]):
            list2.append(i[1])
    return list2


# 1317. Convert Integer to the Sum of Two No-Zero Integers
def non_zero(n):
    import random
    a = random.randint(1, n - 1)
    b = n - a
    string = str(a) + str(b)
    if b > 0 and str(0) not in string:
        return [a, b]
    non_zero(n)


def two_sum(num):
    count = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        count += 1
    return count


def count_negative(s):
    count = 1
    max_ = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
            max_ = max(count, max_)
        else:
            count = 1
    return max_


if __name__ == '__main__':
    # print(remove_duplicates([1, 0, 2, 3, 0, 4, 5, 0]))
    # print(remove_duplicates([1, 2, 3]))
    # print(occurrences([1, 2, 2, 1, 1, 3]))
    # print(occurrences([1, 2]))
    # print(occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
    # print(maths(234))
    # print(element([1, 2, 2, 6, 6, 6, 6, 7, 10]))
    # print(binary([1, 0, 1]))
    # print(even_digits([12, 345, 2, 6, 7896]))
    # print(replace_index([17, 18, 5, 4, 6, 1]))
    # print(replace_index([400]))
    # print(decompress([1, 2, 3, 4]))
    # print(decompress([55, 11, 70, 26, 62, 64]))
    # print(non_zero(1010))
    # print(two_sum(14))
    print(count_negative("abbcccddddeeeeedcba"))

# for m in range(len(right_arr) - 1, 0, -1):
#     for j in range(m):
#         if right_arr[j] > right_arr[j + 1]:
#             right_arr[j], right_arr[j + 1] = right_arr[j + 1], right_arr[j]
