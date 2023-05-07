def selection_sort(array):
    for step in range(len(array)):
        min_idx = step

        for i in range(step + 1, len(array)):
            if array[i] < array[min_idx]:
                min_idx = i

        temp = array[step]
        array[step] = array[min_idx]
        array[min_idx] = temp


data = [-2, 45, 0, 11, -9]
selection_sort(data)
print(data)
