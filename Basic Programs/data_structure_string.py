def string_length1(str1):
    count = 0
    for char in str1:
        count += 1
    return count


# print(string_length1('python'))


def char_frequency2(str1):
    dict_ = {}
    for n in str1:
        if n in dict_.keys():
            dict_[n] += 1
        else:
            dict_[n] = 1
    return dict_


# print(char_frequency2('python programming'))


def change_char3(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]
    return str1


# print(change_char3('restart'))


def add_string4(str1):
    if str1[-3:] == 'ing':
        str1 += 'ly'
    str1 += 'ing'

    return str1


# print(add_string4('python'))
# print(add_string4('programming'))


def find_longest_word5(words_list):
    word_len = [(len(n), n) for n in words_list]
    for i in range(len(word_len) - 1, 0, -1):
        for j in range(i):
            if word_len[j] > word_len[j + 1]:
                temp = word_len[j]
                word_len[j] = word_len[j + 1]
                word_len[j + 1] = temp
    return word_len[-1][1]


# print(find_longest_word5(["python", "java", "typescript"]))


def user_input6():
    str1 = input('str1 :')
    upper_ = str.upper(str1)
    lower_ = str.lower(str1)
    return upper_, lower_


# print(user_input6())


def sorted_form7():
    items = input("Input comma separated sequence of words :")
    words = list(set([word for word in items.split(",")]))
    for i in range(len(words) - 1, 0, -1):
        for j in range(i):
            if words[j] > words[j + 1]:
                temp = words[j]
                words[j] = words[j + 1]
                words[j + 1] = temp

    return words


# print(sorted_form7())


def last_part_of_str8():
    str1 = 'https://www.w3resource.com/python-exercises/string'
    print(str1.rsplit('/', 1)[0])
    print(str1.rsplit('-', 1)[0])


# last_part_of_str8()


def formatted_text9():
    import textwrap
    sample_text = '''
      Python is a widely used high-level, general-purpose, interpreted,
      dynamic programming language. Its design philosophy emphasizes
      code readability, and its syntax allows programmers to express
      concepts in fewer lines of code than possible in languages such
      as C++ or Java.
      '''
    print(textwrap.fill(sample_text, width=50))


# formatted_text9()


def substring10():
    str1 = 'a Python program to count occurrences of a substring in a string'
    return str1.count("Python")


# substring10()


def string_reverse11(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index = index - 1
    return rstr1


# print(string_reverse11('python'))


def lowercase_str12():
    str1 = 'PYTHON'
    print(str1[:2].lower() + str1[2:])

# lowercase_str12()
