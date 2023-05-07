# Given a list of 10 numbers, return whether or not the list is shuffled sufficiently enough. In this case, if 3 or more
# numbers appear consecutively (ascending or descending), return False.
#
# Examples
# is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]) ➞ False
# # 1, 2, 3 appear consecutively
#
# is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]) ➞ False
# # 9, 8, 7, 6 appear consecutively
#
# is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]) ➞ True
# # No consecutive numbers appear
# is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) ➞ True
# # No consecutive numbers appear
# Notes
# Only steps of 1 in either direction count as consecutive (i.e. a sequence of odd and even numbers would count as being
# properly shuffled (see example #4)).
# You will get numbers from 1-10.
import operator


def is_shuffled_well(lst):
    inc_count = 1
    dec_count = 1
    for i in range(len(lst) - 1):
        if lst[i + 1] == lst[i] + 1:
            inc_count += 1
            if inc_count >= 3:
                return False
        elif lst[i + 1] == lst[i] - 1:
            dec_count += 1
            if dec_count >= 3:
                return False
        else:
            inc_count = 1
            dec_count = 1
    return True


# print(is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]))
# print(is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]))
# print(is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]))
# print(is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]))


# A broken bridge can be represented by 1s and 0s, where contiguous 0s represent holes. You can walk across a bridge
# with a hole with a maximum width of 1, but any holes bigger than
# that you must fix first. For example, the bridge below is walkable:
#
# [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1]
# This bridge is not:
#
# [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# You own several wooden planks, each with different widths. You can patch the holes on the bridge with these planks.
# More specifically, a plank size n can fill a n-sized hole.
# If you had a plank of size 2, the un-walkable bridge above could be filled in:
#
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# But even if you only had a plank of size 1, you could still transform the un-walkable bridge into a walkable one:
#
# [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Write a function that takes in a broken bridge, a list of plank sizes, and returns True if the bridge can be patched
# up enough to walk over, and False otherwise.
#
# Examples
# can_patch([1, 0, 0, 0, 0, 0, 0, 1], [5, 1, 2]) ➞ True
# # You can use the 5 plank to transform the 6 hole to a 1 hole.
# # Leftover planks [1, 2] are okay.
#
# can_patch([1, 0, 0, 0, 0, 0, 0, 1], [4, 1, 2, 3, 4]) ➞ False
# # None of your planks are long enough (you can't combine them).
#
# can_patch([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 2]) ➞ True
# can_patch([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 1]) ➞ False
# Notes
# Individual planks may NOT be combined to form a longer plank.
# Leftover planks are okay.
def can_patch(bridge, planks):
    l = []
    for i in bridge:
        if i == 0:
            l.append(i)
        else:
            if l and not l[-1]:
                l.append(i)
    if l[-1] == 1:
        l = l[:len(l) - 1]
    lst = list(map(str, l))
    print(''.join(lst).split('1'))
    return all([1 if i - 1 in planks else 0 for i in list(map(len, ''.join(lst).split('1')))])


# print(can_patch([1, 0, 0, 1, 1, 0, 0, 0, 0, 1], [1, 2]))
# print(can_patch([1, 0, 0, 0, 0, 0, 0, 1], [4, 1, 2, 3, 4]))


# Mubashir needs your help to find out number of animals hidden in a given string txt.
#
# You are provided with an array of animals given below:
#
# animals = ["dog", "cat", "bat", "cock", "cow", "pig",
# "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
# "frog", "hen", "mole", "duck", "goat"]
# Rule: Return the maximum number of animal names. See the below example:
#
# txt = "goatcode"
#
# count_animals(txt) ➞ 2
# # First animal = "dog"
# # Remaining string = "atcoe",
# # Second animal = "cat".
# # count = 2 (correct)
#
# # If you got a "goat" first time
# # remaining string = "code",
# # no animal will be found during next time.
# # count = 1 (wrong)
# Examples
# count_animals("goatcode") ➞ 2
# # "dog", "cat"
#
# count_animals("cockdogwdufrbir") ➞ 4
# # "cow", "duck", "frog", "bird"
#
# count_animals("dogdogdogdogdog") ➞ 5
def count_animals(animals, text):
    animals.sort()
    animals = sorted(animals, key=len)

    def fun(animal, text):
        for ltr in animal:
            if ltr not in text:
                return False
        return True

    def fun2(animal, text):
        for ltr in animal:
            text = text.replace(ltr, '', 1)
        return text

    count = 0
    i = 0
    while i < len(animals):
        if fun(animals[i], text):
            count += 1
            text = fun2(animals[i], text)
        else:
            i += 1
    return count


# print(count_animals(animals=["dog", "cat", "bat", "cock", "cow", "pig",
#                              "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
#                              "frog", "hen", "mole", "duck", "goat"]
#                     , text='goatcode'))
# print(count_animals(animals=["dog", "cat", "bat", "cock", "cow", "pig",
#                              "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
#                              "frog", "hen", "mole", "duck", "goat"]
#                     , text='dogdogdogdogdog'))


# Given two lists smlst and biglst, we say smlst is an ordered sublist of biglst if all the elements of smlst can be
# found in biglst, and in the same order.
#
# Examples:
#
# [4, 3, 2] is an ordered sublist of [5, 4, 3, 2, 1].
# [5, 3, 1] is an ordered sublist of [5, 4, 3, 2, 1].
# [5, 3, 1] is not and ordered sublist of [1, 2, 3, 4, 5] since elements are not in the same - [1, 2, 3] is an ordered
# sublist of [3, 2, 1, 2, 3].
# Write a function that, given lists smlst and biglst, decides if smlst is an ordered sublist of biglst.
#
# Examples
# is_ord_sub([4, 3, 2], [5, 4, 3, 2, 1]) ➞ True
#
# is_ord_sub([5, 3, 1], [5, 4, 3, 2, 1]) ➞ True
#
# is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]) ➞ False
#
# is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3]) ➞ True
# Notes
# Be careful of examples like the fourth example, where the elements of smlst appear multiple times in biglst.
def is_ord_sub(smlst, biglst):
    d = {}
    for num in smlst:
        i = 0
        while i < len(biglst):
            if biglst[i] == num:
                d[num] = d.get(num, []) + [i]
            i += 1
    lst = [max(val) for val in d.values()]
    for i in range(len(lst) - 1):
        if not lst[i + 1] > lst[i]:
            return False
    return True


# print(is_ord_sub([4, 3, 2], [5, 4, 3, 2, 1]))
# print(is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]))
# print(is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3]))

