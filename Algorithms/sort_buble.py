def bubble_sort(list_):
    for i in range(len(list_) - 1, 0, -1):
        for j in range(i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
    return list_


l1 = [3, 1, 4, 2]
print(bubble_sort(l1))