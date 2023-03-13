from datetime import date
import re


# python program to print day of a date
def day_of_date(str1):
    y, m, d = map(int, str1.split('/'))
    weeks = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    w = date.isoweekday(date(y, m, d))
    return f'Name of the date: {weeks[w]}'


# Python program to count the number of prime numbers
def count__primes_nums(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr


# Write a Python program to create a string with no duplicate consecutive letters from a given string.
def no_consecutive_letters(txt):
    return txt[0] + ''.join(txt[i] for i in range(1, len(txt)) if txt[i] != txt[i - 1])


# Write a Python program to remove all vowels from a given string.
def test(text):
    return re.sub(r'[aeiou]+', ' ', text)


if __name__ == '__main__':
    # print(day_of_date('2023/3/14'))
    # print(count__primes_nums(10))
    # print(no_consecutive_letters("PPYYYTTHON"))
    print(test('python'))
