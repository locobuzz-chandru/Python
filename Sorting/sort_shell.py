def shell_sort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2


data = [5, 3, 4, 2, 1]
size = len(data)
shell_sort(data, size)
print(data)
