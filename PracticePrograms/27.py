from functools import reduce


def fun(n):
    from functools import reduce
    # lst = [[list(f"{i:b}")] for i in range(n + 1)]
    # lst1 = [reduce(lambda x, y: int(x) + int(y), i) for i in lst]
    # lst1 = list(map(sum, lst))
    # for i in lst:
    #     sum()
    # print(lst)
    from functools import reduce
    lst = [bin(i).replace("0b", "") for i in range(n + 1)]
    lst1 = [int(reduce(lambda x, y: int(x) + int(y), i)) for i in lst]
    return lst1


# print(fun(n=2))
# print(fun(5))


def fun1(s):
    return [s[i] for i in range(len(s) - 1, -1, -1)]
    # lst = []
    # for i in range(len(s)-1, -1, -1):
    #     lst.append(s[i])
    # return lst


# print(fun1(["h", "e", "l", "l", "o"]))


def fun2(s):
    vowel = "aeiouAEIOU"
    a = ""
    for char in s:
        if char in vowel:
            a = a + char
    # l = lambda char: a+=char for char in s if char in vowel
    result = ""
    for char in s:
        if char in vowel:
            result += a[-1]
            a = a[:-1]
        else:
            result += char
    return result


# print(fun2("leetcode"))


def fun3(list1, list2):
    d = {}
    for i in list1:
        if i in list2:
            c = list2.index(i) + list1.index(i)
            d[c] = d.get(c, []) + [i]
    print(d)
    return [d.get(min(d.keys()))]


# print(fun3(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
#            list2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
#            ))
# print(fun3(list1=["happy", "sad", "good"], list2=["sad", "happy", "good"]))


def function(nums):
    lst = [abs(i) for i in nums]
    print(lst[2])
    d1 = {i: nums[i] for i in range(len(nums))}
    print(d1)
    d2 = {lst[i]: i for i in range(len(lst))}
    d2 = list(enumerate(lst))
    print(d2)
    lst.sort()
    a = lst[::-1][:3]
    indexes = []
    # for i in range(3):
    #     b = d2.get(a[i])
    #     indexes.append(b)
    # # print(indexes)
    # max_nums = []
    # for i in range(3):
    #     b = d1.get(indexes[i])
    #     max_nums.append(b)
    # return max_nums


# print(function([1, 2, 3, 4]))
# print(function([-100, -98, -1, 2, 3, 4]))
# print(function([1, 0, 100]))
# print(function([-1, -2, 1]))


def fun6(nums, k):
    lst = [abs(i) for i in nums]
    d1 = {i: nums[i] for i in range(len(nums))}
    d2 = {lst[i]: i for i in range(len(lst))}
    lst.sort()
    a = lst[::-1][:k]
    indexes = []
    for i in range(k):
        b = d2.get(a[i])
        indexes.append(b)
    max_nums = []
    for i in range(k):
        b = d1.get(indexes[i])
        max_nums.append(b)
    return sum(max_nums) / k


# print(fun6([1, 12, -5, -6, 50, 3], 4))
# print(fun6([5], 1))


def func(nums):
    lst = []
    count = 1
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            count += 1
        elif i == len(nums) - 1:
            lst.append(count)
        else:
            lst.append(count)
            count = 1
    return lst


# print(func([1, 3, 5, 4, 7]))


# print(func([2, 2, 2, 2, 2]))


def fun7(n):
    a = list(str(bin(n)).replace("0b", ""))
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            return False
    return True


# print(fun7(11))


def fun8(image):
    list1 = []
    lst = [image[i][::-1] for i in range(len(image))]
    for i in range(len(image)):
        list2 = []
        for j in range(len(lst[i])):
            if lst[i][j] == 1:
                list2.append(0)
            else:
                list2.append(1)
        list1.append(list2)
    return list1


# print(fun8([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))


def fun9(s, goal):
    if len(s) != len(goal):
        return False
    if s == goal and len(set(s)) < len(s):
        return True
    differences = []
    for x in range(len(goal)):
        if s[x] != goal[x]:
            differences.append([s[x], goal[x]])
    print(differences)
    if len(differences) == 2 and differences[0] == differences[-1][::-1]:
        return True
    return False


# print(fun9(s="ab", goal="ba"))


def fun10(matrix):
    lst1 = []
    for i in range(len(matrix)):
        lst = []
        for j in range(len(matrix[0])):
            lst.append(matrix[j][i])
        lst1.append(lst)
    return lst1
    # print(*matrix)
    # return list(zip(*matrix))


print(fun10([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
