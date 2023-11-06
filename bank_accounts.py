# Object Oriented Programming design
class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, account_name):
        self.balance = initial_amount
        self.name = account_name
        print(f"\nAccount '{self.name }' created. \nBalance = ${self.balance}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance > amount:
            return
        else:
            raise BalanceException(
            f"\nSorry, account '{self.name}' only has a balance of ${self.balance}")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n*************** \n\nBeginning Transfer...')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete! \n\n***************")
        except BalanceException as error:
            print(f'\nTransfer interrupted. {error}')

class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()

class SavingAccount(InterestRewardsAccount):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 5

    # override
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

