"""
Question 1
Create a class to represent a bank account . It will need to have a balance,
a method of withdrawing money, depositing and displaying it to the screen.
Create an instance of the bank account  and check that the methods work as expected
"""


class BankAccount(object):
    """
        Attributes
        ----------
        balance = current net amount
    """
    # instance
    def __init__(self, balance=0.0):
        self.balance = balance

    # methods from here on
    def display(self):
        print(f'Your balance is {self.balance}')

    def deposit(self):
        user_deposit = float(input('How much would you like to deposit?>>> '))
        self.balance += user_deposit
        print(f'Deposit successful!'
              f'\nCurrent balance : {self.balance:.2f}')

    def withdrawal(self):
        user_withdraw = float(input('How much would you like to withdraw? >>> '))
        if user_withdraw > self.balance:
            print(f'You don\'t have enough funds: your balance is {self.balance}')
        else:
            self.balance -= user_withdraw
            print(f'Withdrawal successful!!'
                  f'\nCurrent balance : {self.balance:.2f}')


# Bank Account checkup
samir = BankAccount(100)
print(BankAccount.display(samir))
print(BankAccount.deposit(samir))
print(BankAccount.withdrawal(samir))
