# basic encaptulation

# class
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance     # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# obj
acc = BankAccount("GaAs", 5000)
acc.deposit(2000)
print(acc.get_balance())  

print(acc.__balance)  # this can not be accesssed
