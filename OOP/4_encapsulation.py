# Encapsulation is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a
# single unit. In encapsulation, the variables of a class will be hidden from other classes, and can be accessed only
# through the methods of their current class

# Protected members -> of a class,can only be accessed within the class but cannot be accessed by anyone outside it
class Base1:
    def __init__(self):
        self._p = 78


class Derived1(Base1):
    def __init__(self):
        Base1.__init__(self)
        print("call the protected member of base class: ", self._p)

        # modifying the protected variable
        self._p = 433
        print("call the protected member of base class: ", self._p)


# obj_1 = Derived1()
# obj_2 = Base1()
# print("Access the protected member of obj_1: ", obj_1._p)
# print("Access the protected member of obj_2: ", obj_2._p)


# Private members -> should not be accessed by anyone outside the class or any base classes
class Base2:
    def __init__(self):
        self.p = "public"
        self.__q = "protected"


class Derived2(Base2):
    def __init__(self):
        Base2.__init__(self)
        print("call the private member of base class: ")
        print(self.__q)


obj_3 = Base2()
print(obj_3.p)
obj_4 = Derived2()


# name mgling