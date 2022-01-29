class Account:

    def __init__(self, filename):
        self.filename=filename
        with open(filename, "r") as my_file:
            self.balance=int(my_file.read())

    def withdraw(self, amount):
        self.balance=self.balance-amount

    def deposit(self, amount):
        self.balance=self.balance+amount

    def update_balance(self):
        with open(self.filename, "w") as my_file:
            my_file.write(str(self.balance))


class Checking(Account):
    """This class generates checking account objects"""

    type="checking"

    def __init__(self, filename, charges):
        Account.__init__(self, filename)
        self.charges = charges

    def transfer(self, amount):
        self.balance=self.balance-amount-self.charges


jacks_checking=Checking("jack.txt", 24)
jacks_checking.transfer(100)
jacks_checking.update_balance()
print(jacks_checking.balance)

johns_checking=Checking("john.txt", 24)
johns_checking.transfer(100)
johns_checking.update_balance()
print(johns_checking.balance)

# account=Account("balance.txt")
# account.deposit(1000100)
# account.update_balance()
# print(account.balance)
