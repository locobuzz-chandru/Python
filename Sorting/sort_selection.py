def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


data = [-2, 45, 0, 11, -9]
selection_sort(data)
print(data)
