from dataclasses import dataclass, field, asdict
import time


@dataclass
class Employee:
    name: str
    email: str

    def asdict(self):
        return asdict(self)


def form_table(f):
    def wrapper(*args, **kwargs):
        print('-' * 43)
        print(f"|{'Name':^20}|{'Email':^20}|")
        print('-' * 43)
        call = f(*args, **kwargs)
        print('-' * 43)
        return call

    return wrapper


def time_it(f):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        call = f(*args, **kwargs)
        print('Execution time:\t', time.perf_counter() - start)
        return call

    return wrapper


@dataclass
class Company:
    employees: dict = field(default_factory=dict)

    def add(self, obj: Employee):
        self.employees[obj.email] = obj

    @time_it
    @form_table
    def print(self):
        for _, v in self.employees.items():
            data = v.asdict()
            print(f"|{data['name']:^20}|{data['email']:^20}|")

    @time_it
    @form_table
    def print_iter(self):
        iter_obj = iter(self.employees.items())
        for _, obj in iter_obj:
            data = obj.asdict()
            print(f"|{data['name']:^20}|{data['email']:^20}|")


if __name__ == '__main__':

    company = Company()
    for e in range(1000):
        e1 = Employee(name='emp' + str(e), email='abc@' + str(e))
        company.add(e1)
    # company.add(e)
    # company.add(e2)
    company.print()
    company.print_iter()
