import random
import time
import csv


class Employee:

    def __init__(self, employee_parameters_dict):
        self.total_wage = 0
        self.total_emp_hrs = 0
        self.total_emp_days = 0
        self.emp_name = employee_parameters_dict.get("employee_name")
        self.emp_wage = employee_parameters_dict.get("employee_wage")
        self.max_working_hrs = employee_parameters_dict.get("maximum_working_hrs")
        self.max_working_days = employee_parameters_dict.get("maximum_working_days")

    def get_emp_dict(self):
        return {"Employee name": self.emp_name, "Working days": self.max_working_days, "Total wage": self.total_wage}

    def calc_wage(self):
        while self.total_emp_hrs < self.max_working_hrs and self.total_emp_days < self.max_working_days:
            self.total_emp_days = self.total_emp_days + 1
            emp_check = random.randrange(0, 3)
            emp_hrs = self.check_attendance(emp_check)
            self.total_emp_hrs += emp_hrs
            self.total_wage += emp_hrs * self.emp_wage

    def check_attendance(self, emp_check):
        switcher = {
            0: 0,
            1: 8,
            2: 4
        }
        return switcher.get(emp_check)

    def as_string(self):
        return "{:^14} {:^10} {:^14}".format(self.emp_name, self.max_working_days, self.total_wage)


class EmployeeIter:

    def __init__(self):
        self.employee_dict = {}

    def add_emp(self, employee_object):
        self.employee_dict.update({employee_object.emp_name: employee_object})

    def __iter__(self):
        self.val = list(self.employee_dict.values())
        self.count = 0
        return self

    def __next__(self):
        if self.count < len(self.val):
            result = self.val[self.count].as_string()
            self.count += 1
            return result
        else:
            raise StopIteration


class DisplayEmployee:

    def __init__(self):
        self.employee_dict = {}

    def add_emp(self, employee_object):
        self.employee_dict.update({employee_object.emp_name: employee_object})

    def display_employees(self):
        print("{:<10} {:<10} {:<10}".format('Employee name', 'Working days', 'Total wage'))
        for key, value in self.employee_dict.items():
            print(value.as_string())


def add_employee():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            emp_parameters = {"employee_name": row[0], "employee_wage": int(row[1]),
                              "maximum_working_hrs": int(row[2]), "maximum_working_days": int(row[3])}
            employee = Employee(emp_parameters)
            employee.calc_wage()
            emp.add_emp(employee)
            emp1.add_emp(employee)


def display_employee_iter():
    start = time.time()
    for i in iter(emp):
        print(i)
    end = time.time()
    print("Iter Time taken : ", end - start)
    start1 = time.time()
    emp1.display_employees()
    end1 = time.time()
    print("Function Time taken : ", end1 - start1)


if __name__ == "__main__":
    emp = EmployeeIter()
    emp1 = DisplayEmployee()
    while True:
        choice = int(input("1.Add new employee\n"
                           "2.Display all employees iter\n"
                           "0.Exit\n"
                           "Enter your choice : "))
        choice_dict = {1: add_employee, 2: display_employee_iter}
        if choice == 0:
            break
        elif choice > 9:
            print("Enter correct choice")
        else:
            choice_dict.get(choice)()
