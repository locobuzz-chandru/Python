def set_program1():
    a = set(([1, 2]))
    return a


# print(set_program1())


def set_iterate2():
    set_ = {1, 2, 3, 4, 5}
    for i in set_:
        return i


# print(set_iterate2())


def add_set3():
    set_ = {1, 2, 3, 4}
    set_.add(5)
    return set_


# print(add_set3())


def remove_set4():
    set_ = {1, 2, 3, 4}
    set_.remove(3)
    return set_


# print(remove_set4())


def remove_item5():
    set_ = {1, 2, 3, 4}
    if 2 in set_:
        set_.remove(2)
    return set_


# print(remove_item5())


def set_intersection6():
    set1 = {1, 2, 3, 4}
    set2 = {4, 2, 6, 3}
    set3 = set1.intersection(set2)
    return set3


# print(set_intersection6())


def set_union7():
    set1 = {1, 2, 3, 4}
    set2 = {4, 2, 6, 3}
    set3 = set1.union(set2)
    return set3


# print(set_union7())


def set_difference8():
    set1 = {1, 2, 3, 4}
    set2 = {4, 2, 6, 3}
    set3 = set1.difference(set2)
    return set3


# print(set_difference8())


def symmetric_diff9():
    set1 = {1, 2, 3, 4}
    set2 = {4, 2, 6, 3}
    set3 = set1.symmetric_difference(set2)
    return set3


# print(symmetric_diff9())


def set_clear10():
    set1 = {1, 2, 3, 4}
    set1.clear()
    return set1


# print(set_clear10())


def frozen_set11():
    set1 = {1, 2, 3, 4}
    set2 = frozenset(set1)
    return set2


# print(frozen_set11())


def max_min_set12():
    set1 = {1, 2, 3, 4}
    maximum = max(set1)
    minimum = min(set1)
    return minimum, maximum


# print(max_min_set12())
