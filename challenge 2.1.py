class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if amount > 0 and self.__account_balance >= amount:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
        elif amount <= 0:
            return "Withdrawal amount must be greater than zero."
        else:
            return "Insufficient funds for withdrawal."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ${self.__account_balance}"


my_account = BankAccount("12345", "John Doe", 1000.0)


print(my_account.display_balance())
print(my_account.deposit(500))
print(my_account.withdraw(200))
print(my_account.withdraw(1500))