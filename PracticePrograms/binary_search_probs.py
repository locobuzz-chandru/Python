# Implement a function to find the square root of a given non-negative integer using binary search
def square_root(num):
    start = 0
    end = num
    res = 1
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == num:
            res = mid
            break
        if mid * mid < num:
            start = mid + 1
            res = mid
        else:
            end = mid - 1
    return res


# Write a function to find the first occurrence of a target value in a sorted list of integers using binary search.
# Return the index of the target if found, or -1 if not found
def first_occurrence(nums, target):
    start, end = 0, len(nums) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            result = mid
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return result


# Given a sorted list of integers that has been rotated at an unknown pivot index, implement a function to find the
# minimum element in the list. The list does not contain any duplicates
def find_minimum(nums):
    start = 0
    end = len(nums) - 1
    while start < end:
        mid = (start + end) // 2
        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid
    return nums[start]


if __name__ == '__main__':
    # print(square_root(81))
    # print(first_occurrence([1, 2, 3, 4, 4, 4, 5, 6, 7], 4))
    print(find_minimum([4, 5, 6, 7, 0, 1, 2]))
