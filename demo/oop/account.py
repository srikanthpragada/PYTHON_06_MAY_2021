class Account:
    # Constructor
    def __init__(self, acno, ahname):
        # object attributes
        self.acno = acno
        self.ahname = ahname
        self.__balance = 0     # Private attribute

    # Methods
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def getbalance(self):
        return self.__balance


a1 = Account(1, "Steve")   # Create an object
a1.deposit(10000)          # Call method
a1.withdraw(5000)
print(a1.ahname)
print(a1.__balance)
print(a1.getbalance())
a2 = Account(2, "Bob")
