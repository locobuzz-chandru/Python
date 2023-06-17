class FunctionalList:
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)


# a = FunctionalList([1, 2, 3, 4])
# print(len(a.values))
# print(a.values.__getitem__(2))


class A:
    def __new__(cls):
        print('Creation of A')
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        self.a = 2

    def __format__(self, f):
        if f == 'f':
            return str(self.a)
        return str(self)


# a = A()
# print(format(a, 'f'))


class C:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age


# alice = C(15)
# bob = C(30)
# rel = 'younger' if alice < bob else 'older'
# print(f'Alice is {rel} than Bob')

class H:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.fp = open(self.name)
        return self.fp

    def __exit__(self, exc, exc_value, traceback):
        print(f'Exception: {exc_value}')
        self.fp.close()
        self.fp = None

    # h = H('a.txt')
    # with h as v:
    #     print(v.read())


def string_freq(queries, words):
    queries_count = [s.count(min(s)) for s in queries]
    word_count = [w.count(min(w)) for w in words]
    answer = [sum(q < w for w in word_count) for q in queries_count]
    return answer


# print(string_freq(queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]))
# print(string_freq(queries=["cbd"], words=["zaaaz"]))

# import bank_merge_sort
# bank_merge_sort.__doc__ = 'abcd'
# print(bank_merge_sort.__name__)
# print(bank_merge_sort.__doc__)


# Implement
# a
# function
# that
# takes
# a
# list
# of
# numbers and returns
# the
# longest
# increasing
# subsequence
# within
# the
# list.

def longest_increasing_subsequence(nums):
    n = len(nums)
    if n == 0:
        return []

    # Initialize an array to store the lengths of increasing subsequences
    lengths = [1] * n

    # Initialize an array to store the previous indices of elements in the subsequences
    prev_indices = [-1] * n

    # Compute the lengths of increasing subsequences
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev_indices[i] = j

    # Find the index of the element with the maximum length
    max_length_index = 0
    for i in range(1, n):
        if lengths[i] > lengths[max_length_index]:
            max_length_index = i

    # Reconstruct the longest increasing subsequence
    lis = []
    curr_index = max_length_index
    while curr_index != -1:
        lis.append(nums[curr_index])
        curr_index = prev_indices[curr_index]

    # Reverse the subsequence to get the correct order
    lis.reverse()

    return lis
