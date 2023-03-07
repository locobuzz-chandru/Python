def reverse_array2():
    array_ = [1, 3, 5, 7, 9]
    array1_ = []
    for i in range(len(array_) - 1, -1, -1):
        array1_.append(array_[i])
    return array1_


# print(reverse_array2())


def no_of_occurrence3():
    array_ = [1, 2, 5, 4, 3, 7, 9, 7, 5, 3, 4, 6, 7, 1]
    return array_.count(7)


# print(no_of_occurrence3())


def remove_first_occurrence4():
    array_ = [1, 2, 5, 4, 3, 7, 9, 7, 5, 3, 4, 6, 7, 1]
    array_.remove(7)
    return array_


# print(remove_first_occurrence4())


def create_array1():
    array_ = [1, 3, 5, 7, 9]
    for i in array_:
        print(i)

# create_array1()
