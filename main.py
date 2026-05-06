class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self._balance = balance
        self.__pin = pin

    def deposit(self, x):
        self._balance += x

    def withdraw(self, pin, x):
        if self.__pin == pin:
            self._balance -= x
        else:
            print("Wrong pin")

    def check_balance(self):
        return self._balance


b1 = BankAccount("Ali", 100, "1234")

b1.deposit(50)
print(b1.check_balance())

b1.withdraw("0000", 50)

b1.withdraw("1234", 50)
print(b1.check_balance())
