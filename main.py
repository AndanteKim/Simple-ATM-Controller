from bank_accounts import *
import getpass, sys
from unittest import TestCase



Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)

Jim = InterestRewardsAccount(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = SavingAccount(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)
""" # incomplete section
if __name__ == "__main__":
    BankAccounts = dict()
    while True:
        # This part should be replaced as API card number swipe
        decode_card_number = input("Insert your card or press Q to exit")
        if (decode_card_number == 'Q')
            break
        if decode_card_number in BankAccounts:
            password = getpass("Insert PIN number")
        else:
            print("\nCard number is invalid. Try again!")
    sys.exit()
"""

        

