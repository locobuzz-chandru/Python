from functools import reduce


def sum_items1():
    list1 = [1, 2, 3, 4, 5, 6]
    return reduce(lambda x, y: x + y, list1)


# print(sum_items1())


def multiply_list2():
    list1 = [1, 2, 3, 4, 5, 6]
    return reduce(lambda x, y: x * y, list1)


# print(multiply_list2())


def smallest_num3():
    list_ = [4, 3, 7, 1]
    for i in range(len(list_) - 1, 0, -1):
        for j in range(i):
            if list_[j] > list_[j + 1]:
                temp = list_[j]
                list_[j] = list_[j + 1]
                list_[j + 1] = temp
    return list_[0]


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


def sort_list_last(tuple_):
    for i in range(len(tuple_) - 1, 0, -1):
        for j in range(i):
            if tuple_[j][1] > tuple_[j + 1][1]:
                temp = tuple_[j]
                tuple_[j] = tuple_[j + 1]
                tuple_[j + 1] = temp
    return tuple_


# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


def remove_duplicates6():
    list1 = [1, 5, 8, 4, 6, 3, 5, 4, 9, 2, 8, 1]
    return list(set(list1))


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
    dup_items_list = [x for x in list2 if x in list1]
    return dup_items_list


# print(common_data9([1, 2, 3], [2, 3, 5]))


def remove_list10(rem_list):
    list1 = [1, 2, 3, 4, 5, 6]
    for x in rem_list:
        list1.remove(x)
    return list1


# print(remove_list10([2, 4, 6]))


def list_permutations11():
    import itertools
    return list(itertools.permutations([1, 2, 3]))


# print(list_permutations11())


def list_diff12():
    list1 = [200, 400, 300, 80, 90]
    list2 = [200, 400, 300, 70, 100]

    list_diff = [i for i in list1 + list2 if i not in list1 or i not in list2]
    return list_diff


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

    list12 = ' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2))
    list23 = ' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2))
    return list12, list23


# print(circular_list14())


def common_items15():
    list1 = [200, 400, 300, 80, 90]
    list2 = [200, 400, 300, 70, 100]
    list_diff = [i for i in list1 if i in list2]
    return list_diff


# print(common_items15())


def group_word16():
    from itertools import groupby
    from operator import itemgetter
    words_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
                  'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']
    dict_ = {}
    for letter, words in groupby(sorted(words_list), key=itemgetter(0)):
        word_list = []
        for word in words:
            word_list.append(word)
        dict_[letter] = word_list
    return dict_


# print(group_word16())


def remove_duplicates17():
    import itertools
    num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    num.sort()
    new_num = list(num for num, _ in itertools.groupby(num))
    return new_num


# print(remove_duplicates17())
