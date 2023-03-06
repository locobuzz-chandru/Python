def f1():
    first_name = input("Enter First Name : ")
    last_name = input("Enter your Last Name : ")
    print(f'First Name : {first_name}, Last Name : {last_name}')


# f1()


def f2():
    values = input("Enter comma separated numbers : ")
    list_ = values.split(",")
    tuple_ = tuple(list_)
    print('List : ', list_)
    print('Tuple : ', tuple_)


# f2()


def f3():
    colors = ["Red", "Green", "White", "Black"]
    print("%s %s" % (colors[0], colors[3]))


# f3()


def f4(num):
    """Return the absolute value of the input number.
    The number must be integer.
    """
    print(abs.__doc__)
    print(f4.__doc__)
    print(abs(num))


# f4(2)


def f5():
    import calendar
    y = int(input("Year : "))
    m = int(input("Month : "))
    print(calendar.month(y, m))


# f5()


def f6():
    from datetime import date
    f_date = date(2014, 7, 2)
    l_date = date(2014, 7, 11)
    date_difference = l_date - f_date
    print(date_difference.days)


# f6()


def is_group_member7(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False


# print(is_group_member7([1, 5, 8, 3], 3))
# print(is_group_member7([5, 8, 3], -1))


def histogram8(items):
    for n in items:
        output = ''
        times = n
        while times > 0:
            output += '*'
            times = times - 1
        print(output)


# histogram8([2, 3, 6, 5])


def concatenate_list_data9(list_):
    result = ''
    for element in list_:
        result += str(element)
    return result


# print(concatenate_list_data9([74, 0, 614, 129]))


def color_list10(color_list_1, color_list_2):
    print("color list 1 and list 2:")
    print(color_list_1.difference(color_list_2))
    print("color list 1 and list 2:")
    print(color_list_2.difference(color_list_1))


list_1 = set(["White", "Black", "Red"])
list_2 = set(["Red", "Green"])


# color_list10(list_1, list_2)


def check_file11():
    import os.path
    print(os.path.isfile('python_basic.py'))
    print(os.path.exists('python_basic.py'))


# check_file11()


def external_command12():
    import os
    os.system("dir *.py")


# external_command12()


def cpu13():
    import multiprocessing
    print(multiprocessing.cpu_count())


# cpu13()


def all_files_in_dir14():
    import os
    path = "E:/Projects/Python/Functions"
    dir_list = os.listdir(path)
    print("Files and directories in '", path, "' :")
    print(dir_list)


# all_files_in_dir14()


def env_variables15():
    import os
    for item, value in os.environ.items():
        print('{}: {}'.format(item, value))


# env_variables15()


def get_username16():
    import getpass
    username = getpass.getuser()
    print(username)


# get_username16()


def execution_time17(n):
    import time
    start_time = time.time()
    for i in range(1, n + 1):
        print(i)
    end_time = time.time()
    return end_time - start_time


n = 1000


# print("time required is :", execution_time17(n))


def absolute_file_path18(file_name):
    import os
    return os.path.abspath(file_name)


# print(absolute_file_path18("python_basic.py"))


def file_details19():
    import os.path, time
    print("Last modified: ", time.ctime(os.path.getmtime("python_basic.py")))
    print("Created: ", time.ctime(os.path.getctime("python_basic.py")))


# file_details19()


def sort_nums20(x, y, z):
    a1 = min(x, y, z)
    a3 = max(x, y, z)
    a2 = (x + y + z) - a1 - a3
    print("Numbers in sorted order: ", a1, a2, a3)


# sort_nums20(10, 8, 9)


def sort_files21():
    pass


# sort_files21()


def arguments_list22():
    pass


# arguments_list22()


def built_in_modules23():
    import sys
    import textwrap
    module_name = ', '.join(sorted(sys.builtin_module_names))
    print(textwrap.fill(module_name, width=70))


# built_in_modules23()


def size_in_bytes24():
    import sys
    dict_ = {'apple', 'orange', 'apple', 'pear'}
    print("Size of", dict_, "=", sys.getsizeof(dict_), " bytes")


# size_in_bytes24()


def recursion_limit25():
    import sys
    print()
    print("Current value of the recursion limit:")
    print(sys.getrecursionlimit())
    print()


# recursion_limit25()


def no_of_occurrence26():
    count = 0

    my_string = "Write a Python program to count the number occurrence of a specific character in a string"
    my_char = "r"

    for i in my_string:
        if i == my_char:
            count += 1

    print(count)


# no_of_occurrence26()


def system_time27():
    import time
    print(time.ctime())


# system_time27()


def clear_screen28():
    import os
    os.system('cls')


# clear_screen28()


def host_name29():
    import socket
    host_name = socket.gethostname()
    print("Host name:", host_name)


# host_name29()


def url_content30():
    from http.client import HTTPConnection
    conn = HTTPConnection("w3schools.com")
    conn.request("GET", "/")
    result = conn.getresponse()
    contents = result.read()
    print(contents)


# url_content30()


def system_cmd31():
    import subprocess
    returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
    print(returned_text)


# system_cmd31()


def group_id32():
    pass


# group_id32()


def user_env33():
    import os
    print(os.environ)


# user_env33()


def file_properties34():
    import os.path
    import time

    print('File         :', __file__)
    print('Access time  :', time.ctime(os.path.getatime(__file__)))
    print('Modified time:', time.ctime(os.path.getmtime(__file__)))
    print('Change time  :', time.ctime(os.path.getctime(__file__)))
    print('Size         :', os.path.getsize(__file__))


# file_properties34()


def divisible_by_fifteen35():
    num_list = [15, 22, 60, 16, 90, 105, 45, 145, 155]
    result = list(filter(lambda x: (x % 15 == 0), num_list))
    print(result)


# divisible_by_fifteen35()


def variable36():
    try:
        x = 1
    except NameError:
        print("Variable is not defined")
    print("Variable is defined")


# variable36()


def empty_var37():
    n = 20
    d = {"x": 200}
    print(type(n)())
    print(type(d)())


# empty_var37()


def zeroes_to_string38():
    str1 = '122.22'
    print(str1.ljust(8, '0'))
    print(str1.rjust(8, '0'))


# zeroes_to_string38()


def skip_dir39():
    import os
    print([f for f in os.listdir('E:/Projects/Python') if os.path.isfile(os.path.join('E:/Projects/Python', f))])


# skip_dir39()


def extract_dict40():
    d = {'Red': 'Green'}
    (c1, c2), = d.items()
    print(c1)
    print(c2)


# extract_dict40()


def int_to_bin41():
    x = 50
    print(format(x, '08b'))
    print(format(x, '010b'))


# int_to_bin41()


def check_python_shell42():
    import struct
    print(struct.calcsize("P") * 8)


# check_python_shell42()


def max_min_nums43(data):
    l = data[0]
    s = data[0]
    for num in data:
        if num > l:
            l = num
        elif num < s:
            s = num
    return l, s


print(max_min_nums43([5, 47, 12, -5, 112, -23, 0, 45]))
