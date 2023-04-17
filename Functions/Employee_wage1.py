import random


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


class Company:

    def __init__(self, company_name):
        self.company_name = company_name
        self.employee_dict = {}

    def add_emp(self, employee_object):
        self.employee_dict.update({employee_object.emp_name: employee_object})

    def get_emp(self, emp_name):
        return self.employee_dict.get(emp_name)

    # def __iter__(self):
    #     self.val = self.employee_dict.values()
    #     self.count = 1
    #     return self
    #
    # def __next__(self):
    #     if self.count <= len(self.employee_dict.values()):
    #         result = self.val

    def display_employees(self):
        print("{:<10} {:<10} {:<10}".format('Employee name', 'Working days', 'Total wage'))
        val = iter(self.employee_dict.values())
        print(next(val).as_string())


class Companies:
    def __init__(self):
        self.json_dict = {}
        self.company_dict = {}

    def get_company_object(self, company_name):
        return self.company_dict.get(company_name)

    def add_company(self, company_object):
        self.company_dict.update({company_object.company_name: company_object})


def add_employee():
    company_name = input("Enter company name : ")
    company_object = companies.get_company_object(company_name)
    if not company_object:
        company_object = Company(company_name)
        companies.add_company(company_object)
    employee_name = input("Enter employee name : ")
    employee_wage = int(input("Enter employee wage per hour : "))
    maximum_working_hrs = int(input("Enter employee work hours : "))
    maximum_working_days = int(input("Enter employee working days : "))
    emp_parameters = {"employee_name": employee_name, "employee_wage": employee_wage,
                      "maximum_working_hrs": maximum_working_hrs, "maximum_working_days": maximum_working_days}
    employee = Employee(emp_parameters)
    employee.calc_wage()
    company_object.add_emp(employee)


def display_employee():
    company_name = input("Enter company to view employees : ")
    company_object = companies.get_company_object(company_name)
    company_object.display_employees()


if __name__ == "__main__":
    companies = Companies()

    while True:
        choice = int(input("1.Add new employee\n"
                           "2.Display all employees\n"
                           "0.Exit\n"
                           "Enter your choice : "))
        choice_dict = {1: add_employee, 2: display_employee}
        if choice == 0:
            break
        elif choice > 9:
            print("Enter correct choice")
        else:
            choice_dict.get(choice)()
