# Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like
# calculate_emp_salary, emp_assign_department, and print_employee_details.

class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.id = emp_id
        self.salary = salary
        self.department = department

    def calculate_salary(self, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.salary = self.salary + (overtime * (self.salary / 50))

    def print_employee_details(self):
        return f'name: {self.name}, ID: {self.id}, Salary: {self.salary}, Department: {self.department}'


if __name__ == '__main__':
    employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
    print(employee1.print_employee_details())
    employee1.calculate_salary(52)
    print(employee1.print_employee_details())
