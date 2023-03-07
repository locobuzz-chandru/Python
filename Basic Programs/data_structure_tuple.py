def create_tuple1():
    tuple1 = tuple(([1, 2, 3, 4]))
    return tuple1


# print(create_tuple1())


def tuple2():
    tuple1 = tuple(([1, 'A', True, False]))
    return tuple1


# print(tuple2())


def unpack_tuple3():
    tuple1 = ('A', 'B', 'C', 'D')
    (A, B, *C) = tuple1
    return A, B, C


# print(unpack_tuple3())


def colon_tuple4():
    tuplex = ("HELLO", 5, [], True)
    tuplex[2].append(50)
    return tuplex


# print(colon_tuple4())


def repeated_item5():
    tup = (1, 3, 4, 32, 1, 1, 32)
    set_ = set()
    for i in tup:
        if tup.count(i) > 1:
            set_.add(i)
    return set_


# print(repeated_item5())


def check_item6(n):
    tup = (1, 2, 3, 4, 5, 6)
    for x in tup:
        if n in tup:
            return True
        return False


# print(check_item6(5))


def list_to_tuple7():
    list1 = [1, 2, 3, 4]
    tup = tuple(list1)
    return tup


# print(list_to_tuple7())


def remove_item8():
    tup = (1, 2, 3, 4)
    a = list(tup)
    a.remove(3)
    tup = tuple(a)
    return tup


# print(remove_item8())


def tuple_slice9():
    tup = (1, 2, 3, 4)
    tup1 = tup[1:3]
    return tup1


# print(tuple_slice9())


def reverse_tuple10():
    tup = (1, 2, 3, 4)
    list1 = list(tup)
    list1.reverse()
    tup = tuple(list1)
    return tup

# print(reverse_tuple10())
