def sum_items1():
    list1 = [1, 2, 3, 4, 5, 6]
    sum1 = sum(i for i in list1)
    return sum1


# print(sum_items1())


def multiply_list2():
    list1 = [1, 2, 3, 4, 5, 6]
    mult = 1
    for x in list1:
        mult = mult * x
    return mult


# print(multiply_list2())


def smallest_num3():
    list1 = [7, 5, 4, 9, 2, 8, 3]
    min1 = list1[0]
    for a in list1:
        if a < min1:
            min1 = a
    return min1


# print(smallest_num3())


def match_words4(words):
    ctr = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr


# print(match_words4(['abc', 'xyz', 'aba', '1221']))


def last(n):
    return n[-1]


def sort_list_last(tuples):
    return sorted(tuples, key=last)


# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


def remove_duplicates6():
    list1 = [1, 5, 8, 4, 6, 3, 5, 4, 9, 2, 8, 1]
    dup_items = set()
    uniq_items = []
    for x in list1:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)
    return dup_items


# print(remove_duplicates6())


def copy_list7():
    list1 = [1, 2, 3, 4]
    list2 = list1.copy()
    return list2


# print(copy_list7())


def long_words8(n, str1):
    word_len = []
    txt = str1.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len


# print(long_words8(3, "Python program to find the list of words"))


def common_data9(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
    return result


# print(common_data9([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))


def remove_list10():
    list1 = [1, 2, 3, 4, 5, 6]
    list1.remove(2)
    list1.remove(3)
    list1.remove(6)
    return list1


# print(remove_list10())


def list_permutations11():
    import itertools
    return list(itertools.permutations([1, 2, 3]))


# print(list_permutations11())


def list_diff12():
    list1 = [200, 400, 300, 80, 90]
    list2 = [200, 400, 300, 70, 100]

    list_difference = []
    for item in list1:
        if item not in list2:
            list_difference.append(item)

    return list_difference


# print(list_diff12())


def list_append13():
    list1 = [1, 2, 3, 4]
    list3 = []
    for x in list1:
        list3.append(x)
    return list3


# print(list_append13())


def circular_list14():
    list1 = [10, 10, 0, 0, 10]
    list2 = [10, 10, 10, 0, 0]
    list3 = [1, 10, 10, 0, 0]

    print('Compare list1 and list2')
    print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
    print('Compare list1 and list3')
    print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))


# circular_list14()


def common_items15():
    list1 = [200, 400, 300, 80, 90]
    list2 = [200, 400, 300, 70, 100]
    list3 = []
    for x in list1:
        if x in list2:
            list3.append(x)
    return list3


# print(common_items15())


def group_word16():
    from itertools import groupby
    from operator import itemgetter
    word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
                 'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']
    for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
        print(letter)
        for word in words:
            print(word)
        print()


# group_word16()


def remove_duplicates17():
    import itertools
    num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    print("Original List", num)
    num.sort()
    new_num = list(num for num, _ in itertools.groupby(num))
    print("New List", new_num)


# remove_duplicates17()
