import operator


def add_key2():
    dict_ = {0: 10, 1: 20}
    dict_.update({'A': 'B'})
    return dict_


# print(add_key2())


def concatenate_dict3():
    dict1 = {1: 10, 2: 20}
    dict2 = {3: 30, 4: 40}
    dict3 = {5: 50, 6: 60}
    dict4 = {}
    for d in (dict1, dict2, dict3):
        dict4.update(d)
    return dict4


# print(concatenate_dict3())


def dict_with_for_loop4():
    d = {'Red': 1, 'Green': 2, 'Blue': 3}
    for color_key, value in d.items():
        print(color_key, d[color_key])


# print(dict_with_for_loop4())


def square_value5():
    n = int(input("Input a number "))
    d = {x: x * x for x in range(1, n + 1)}
    return d


# print(square_value5())


def remove_key6(x):
    dict_ = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    if x in dict_:
        del dict_[x]
    return dict_


# print(remove_key6('a'))


def distinct_values7():
    list_ = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
             {"VIII": "S007"}]
    u_value = set()
    for dict_ in list_:
        for val in dict_.values():
            u_value.add(val)
    return u_value


# print(distinct_values7())


def str_dict8():
    str1 = 'kalahalamath'
    my_dict = {}
    for letter in str1:
        my_dict[letter] = my_dict.get(letter, 0) + 1
    return my_dict


# print(str_dict8())


def dict_table9():
    dict1 = {1: ["A", 21, 'B'],
             2: ["C", 20, 'D'],
             3: ["E", 21, 'F'], }
    print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))
    for key, value in dict1.items():
        name, age, course = value
        print("{:<10} {:<10} {:<10}".format(name, age, course))


# dict_table9()


def count_value10():
    student = [{'id': 1, 'success': True},
               {'id': 2, 'success': False},
               {'id': 3, 'success': True}]
    return sum(d['id'] for d in student), sum(d['success'] for d in student)


# print(count_value10())


def list_to_nested_dict11():
    num_list = [1, 2, 3, 4]
    new_dict = current = {}
    for name in num_list:
        current[name] = {}
        current = current[name]
    return new_dict


# print(list_to_nested_dict11())


def multiple_keys12():
    student = {
        'name': 'Alex',
        'class': 'V',
        'roll_id': '2'
    }
    keys = student.keys()
    a = keys >= {'class', 'name'}
    b = keys >= {'name', 'Alex'}
    c = keys >= {'roll_id', 'name'}
    return a, b, c


# print(multiple_keys12())


def no_of_items13():
    dict_ = {'A': ['1', '2', '3'], 'B': ['1', '2']}
    return sum(map(len, dict_.values()))

# print(no_of_items13())


def sort_dict1():
    dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    ascending_order = dict(sorted(dict_.items(), key=operator.itemgetter(1)))
    descending_order = dict(sorted(dict_.items(), key=operator.itemgetter(1), reverse=True))
    return ascending_order, descending_order


# print(sort_dict1())
