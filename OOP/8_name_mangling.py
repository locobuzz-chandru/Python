# In name mangling process any identifier with two leading underscore and one trailing underscore is textually replaced
# with _classname__identifier where classname is the name of the current class

# name mangling process helps to access the class variables from outside the class.

class Student:
    def __init__(self, name):
        self.__name = name


s1 = Student("ABC")
print(s1._Student__name)
