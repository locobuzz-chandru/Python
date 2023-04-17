def fun(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] == nums[mid + 1]:
            low = mid + 2
        else:
            high = mid
    return nums[low]


print(fun(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8]))


def fun1(n, a, b, c):
    a, b, c = sorted([a, b, c])
    ugly_a = a
    ugly_b = b
    ugly_c = c
    for i in range(n - 1):
        if ugly_a == ugly_b or ugly_a == ugly_c:
            ugly_a += a
        elif ugly_b == ugly_c:
            ugly_b += b
    if ugly_a < ugly_b and ugly_a < ugly_c:
        ugly_a += a
    # elif ugly_b < ugly_a and


print(fun1(n=3, a=2, b=3, c=5))
