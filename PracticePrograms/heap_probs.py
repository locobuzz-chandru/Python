# Write a program to check if a binary heap is a min heap.
def is_min_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True


#  Write a program to check if a binary heap is a max heap.
def is_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True


# Write a program to heapify a binary heap.
def heapify(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sink_down(arr, i, n)
    return arr


def sink_down(arr, index, size):
    left = 2 * index + 1
    right = 2 * index + 2
    largest = index
    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        sink_down(arr, largest, size)


# Write a program to merge two binary heaps.
def merge_heaps(heap1, heap2):
    merged_heap = heap1 + heap2
    return heapify(merged_heap)


# Write a program to insert an element into a binary heap.
class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)

    def bubble_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.bubble_up(parent)


if __name__ == '__main__':
    # print(is_min_heap([1, 5, 3, 10, 8]))
    # print(is_max_heap([10, 8, 3, 5, 1]))
    # print(heapify([5, 10, 3, 8, 1]))
    # print(merge_heaps([1, 3, 5], [2, 4, 6]))
    heap = BinaryHeap()
    heap.insert(5)
    heap.insert(10)
    heap.insert(3)
    print(heap.heap)
