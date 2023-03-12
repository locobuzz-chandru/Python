import re


def text_match(text):
    pattern = 'ab{3}?'
    if re.search(pattern, text):
        return 'Found a match'
    return 'Not matched'


def upper_lower(text):
    patterns = '[A-Z]+[a-z]+$'
    if re.search(patterns, text):
        return True
    return False


def is_decimal(num):
    dec_num = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    result = dec_num.search(num)
    return bool(result)


# remove words between 1 and 3
def remove_num():
    text = "The quick brown fox jumps over the lazy dog."
    short_word = re.compile(r'\W*\b\w{1,3}\b')
    return short_word.sub('', text)


def capital_words_spaces(str1):
    # print(re.search('(\w)([A-Z])', str1))
    return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)


def starts_ae():
    text = """The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added 
    to the ArrayList and the ArrayList is trimmed accordingly"""
    list_ = re.findall("[ae]\w+", text)
    return list_


if __name__ == "__main__":
    # print(text_match("aabbbbbc"))
    # print(upper_lower("Python"))
    # print(is_decimal('123.11'), is_decimal('3.124587'))
    # print(remove_num())
    # print(capital_words_spaces("PythonExercisesPracticeSolution"))
    print(starts_ae())
