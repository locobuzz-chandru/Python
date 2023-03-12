from collections import namedtuple, ChainMap, OrderedDict, defaultdict, Counter, deque


def namedtuple_fun():
    a = namedtuple('courses', 'name, technology')
    tup = a('django', 'python')
    return tup


# optimised list - insertion and deletion easy
def deque_fun():
    a = ['p', 'y', 't', 'h', 'o', 'n']
    deque1 = deque(a)
    deque1.pop()
    deque1.append('python')
    deque1.popleft()
    deque1.appendleft('django')
    return deque1


def chainmap_fun():
    a = {1: 'A', 2: 'B'}
    b = {3: 'C', 4: 'D'}
    chainmap1 = ChainMap(a, b)
    return chainmap1


def counter_fun():
    a = [1, 2, 4, 5, 1, 3, 6, 5, 3, 4, 1, 5, 3, 1, 2, 4, 3, 3, 3]
    counter = Counter(a)
    return f'{counter}, {list(counter.elements())}, {counter.most_common()}'


def counter_fun1():
    a = [1, 2, 4, 5, 1, 3, 6, 5, 3, 4, 1, 5, 3, 1, 2, 4, 3, 3, 3]
    counter = Counter(a)
    s = {3: 1, 4: 1}
    counter.subtract(s)
    return counter


# remembers the order in which the items are added
def ordered_dict():
    dict_ = OrderedDict()
    dict_[1] = 'A'
    dict_[3] = 'C'
    dict_[2] = 'B'
    return dict_


# dict subclass which calls a factory function to supply missing values
# does not give error if value is missing
def default_dict():
    dict_ = defaultdict(int)
    dict_['a'] = 45
    dict_[2] = 82
    return f'{dict_}, {dict_[3]}'


if __name__ == "__main__":
    # print(namedtuple_fun())
    # print(deque_fun())
    # print(chainmap_fun())
    # print(counter_fun())
    # print(counter_fun1())
    # print(ordered_dict())
    print(default_dict())
