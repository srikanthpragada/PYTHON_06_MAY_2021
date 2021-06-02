class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance

    def __str__(self):
        return f"Insufficient balance {self.balance} for withdraw of {self.amount}"


class Account:
    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # object attributes
        self.acno = acno
        self.ahname = ahname
        self.__balance = balance  # Private attribute

    # Methods
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise InsufficientFundsError(amount, self.__balance)

    def getbalance(self):
        return self.__balance


a1 = Account(1, "Steve")  # Create an object
a1.deposit(10000)  # Call method
try:
    a1.withdraw(50000)
    print("Shopping!")
except InsufficientFundsError as ex:
    print(ex)

print(a1.getbalance())
