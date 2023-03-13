# Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and
# methods like deposit, withdraw, and check_balance.
class BankAccount:
    def __init__(self, account_number, date_of_opening, balance, customer_name):
        self.account_number = account_number
        self.date_of_opening = date_of_opening
        self.balance = balance
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance = self.balance + amount
        return f"{amount} Rs. deposited"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance = self.balance - amount
            return f"{amount}Rs. withdrawn"

    def check_balance(self):
        return f"Current balance is {self.balance}Rs."

    def print_customer_details(self):
        return f'Name: {self.customer_name}, \nAccount Number: {self.account_number}, ' \
               f'\nDate of opening: {self.date_of_opening}, \nBalance: {self.balance} Rs.'


if __name__ == '__main__':
    ac_no_1 = BankAccount(2345, "01-01-2023", 1000, "A")
    print(ac_no_1.print_customer_details())
    print(ac_no_1.deposit(1050))
    print()
    print(ac_no_1.check_balance())
    print()
    print(ac_no_1.withdraw(200))
