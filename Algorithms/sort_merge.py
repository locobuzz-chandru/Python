def divide(arr):
    if len(arr) <= 1:
        return arr
    left_arr = divide(arr[:len(arr) // 2])
    right_arr = divide(arr[len(arr) // 2:])
    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    merged = []
    while len(left_arr) != 0 and len(right_arr) != 0:
        if left_arr[0] < right_arr[0]:
            merged.append(left_arr[0])
            left_arr.remove(left_arr[0])
        else:
            merged.append(right_arr[0])
            right_arr.remove(right_arr[0])
    if len(left_arr) == 0:
        merged = merged + right_arr
    else:
        merged = merged + left_arr
    return merged


print(divide([1, 4, 3, 2]))
