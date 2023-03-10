# "In the class Employee, implement the instance attributes as firstname, lastname and salary.
#
# Create the method from_string() which parses a string containing these attributes and assigns them to the correct
# properties. Properties will be separated by a dash.
#
# Examples
# emp1 = Employee(""Mary"", ""Sue"", 60000)
# emp2 = Employee.from_string(""John-Smith-55000"")
# emp1.firstname ➞ ""Mary""
#
# emp1.salary ➞ 60000
#
# emp2.firstname ➞ ""John""
#
# emp2.salary ➞ 55000"

class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @classmethod
    def from_string(cls, str1):
        a = str1.split('-')
        return cls(firstname=a[0], lastname=a[1], salary=a[2])


emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string(str1='John-Smith-55000')
print(emp1.firstname)
print(emp2.salary)
print(emp2.firstname)
print(emp2.lastname)

