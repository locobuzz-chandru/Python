def reverse_number(num):
    reverse = 0
    while num != 0:
        reverse = reverse * 10 + num % 10
        num = num // 10
    return reverse


def armstrong_number(num):
    count = len(str(num))
    sum_ = sum([int(digit) ** count for digit in list(str(num))])
    return num == sum_


def prime_number(num):
    temp = 0
    for n in range(2, num // 2):
        if num % n == 0:
            temp = 1
            break
    return temp == 1


def fib_series(num):
    lst = [0, 1]
    first = lst[0]
    second = lst[1]
    for i in range(num):
        if not i <= 1:
            third = first + second
            first = second
            second = third
            lst.append(third)
    return lst


def recursive_fib_series(num):
    numbers = {0: 0, 1: 1}
    result = numbers.get(num)
    if result:
        return result
    return recursive_fib_series(num - 1) + recursive_fib_series(num - 2)


def swap(a: int, b: int):
    a = a - b
    b = a + b
    a = b - a
    return a, b


def palindrome(num):
    reverse = 0
    temp = num
    while temp != 0:
        reverse = reverse * 10 + temp % 10
        temp = temp // 10
    return reverse == num


def recursive_palindrome(num):
    def reverse(n):
        if n < 10:
            return n
        else:
            return int(str(n % 10) + str(reverse(n // 10)))

    return num == reverse(num)


def is_binary(num):
    while num > 0:
        if (num % 10) not in [0, 1]:
            return False
        num = num // 10
        if num == 0:
            return True


def prime_factors(n):
    factors = []
    for i in range(1, 1 + n):
        if n % i == 0:
            flag = 0
            for j in range(2, i):
                if i % j == 0:
                    flag = 1
                    break
            if flag == 0:
                factors.append(i)
    return factors


def add_two_numbers(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x


def perfect_numbers(n):
    sum_ = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            sum_ += i
    return sum_ == n


def is_valid_parentheses(s):
    stack = []
    d = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in d:
            if not stack or stack.pop() != d[char]:
                return False
        else:
            stack.append(char)
    return len(stack) == 0


if __name__ == '__main__':
    # print(reverse_number(123))
    # print(armstrong_number(407), armstrong_number(153))
    # print(prime_number(6))
    # print(fib_series(10))
    # for i in range(10):
    #     print(recursive_fib_series(i), end=' ')
    # print(swap(9, 2))
    # print(palindrome(12321))
    # print(recursive_palindrome(12321))
    # print(prime_factors(24))
    # print(add_two_numbers(5, 7))
    # print(perfect_numbers(28))
    print(is_valid_parentheses("()[]{}"))
