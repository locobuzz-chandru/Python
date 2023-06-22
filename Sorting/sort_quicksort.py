# def quicksort(arr, left, right):
#     if left < right:
#         partition_pos = partition(arr, left, right)
#         quicksort(arr, left, partition_pos - 1)
#         quicksort(arr, partition_pos + 1, right)
#
#
# def partition(arr, left, right):
#     i = left
#     j = right
#     pivot = arr[right]
#     while i < j:
#         while i < right and arr[i] < pivot:
#             i += 1
#         while j > left and arr[j] >= pivot:
#             j -= 1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#     if arr[i] > pivot:
#         arr[i], arr[right] = arr[right], arr[i]
#     return i
#
#
# array = [22, 11, 88, 66, 55, 77, 33, 44]
# quicksort(array, 0, len(array) - 1)
# print(array)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        print(less, pivot, greater)
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([4, 5, 1, 3, 2, 6]))
