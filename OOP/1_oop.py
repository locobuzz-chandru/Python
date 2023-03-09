# object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming

# class contains the blueprints or the prototype from which the objects are being created

# object is an entity that has a state and behavior associated with it

# __init__() function is called automatically every time the class is being used to create a new object
# useful to do any initialization of variables

# self parameter is a reference to the current instance of the class, and is used to access variables

class MyClass:
    def __init__(self, name):
        self.name = name


my_class = MyClass('John')
print(my_class.name)
