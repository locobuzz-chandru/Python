def create_array1():
    array_ = [1, 3, 5, 7, 9]
    for i in array_:
        print(i, end=' ')


# create_array1()


def reverse_array2():
    array_ = [1, 3, 5, 7, 9]
    array1_ = []
    for i in range(len(array_) - 1, -1, -1):
        array1_.append(array_[i])
    print(array1_)


# reverse_array2()


def no_of_occurrence3():
    array_ = [1, 2, 5, 4, 3, 7, 9, 7, 5, 3, 4, 6, 7, 1]
    print(array_.count(7))


# no_of_occurrence3()


def remove_first_occurrence4():
    array_ = [1, 2, 5, 4, 3, 7, 9, 7, 5, 3, 4, 6, 7, 1]
    array_.remove(7)
    print(array_)


remove_first_occurrence4()
