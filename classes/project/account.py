from  datetime import datetime, timezone, timedelta
from classes.project.transaction import TransactionType, transaction


class Account:
    timezone = timezone(timedelta(hours=-7), 'MST')
    interest_rate = 0.5

    def __init__(self, number, holder, init_balance = 0) -> object:
        self.number = number
        self.holder = holder
        self._balance = float(init_balance)


    @property
    def balance(self):
        return self._balance


    @transaction
    def deposit(self, amount):
        if amount > 0:
            self._balance +=amount
            return TransactionType.Deposit
        else:
            return TransactionType.Declined


    @transaction
    def withdrawal(self, amount):
        if amount< self._balance:
            self._balance -= amount
            return TransactionType.Withdrawal
        else:
            return TransactionType.Declined


    @transaction
    def calc_interest(self):
        self._balance += self._balance * self.interest_rate
        return TransactionType.Interest




class AccountHolder:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        return f'{self.lastname} {self.firstname}'

john = AccountHolder('John', 'Doe')
john_account = Account('1234', john)

mike = AccountHolder('Mike', 'Doe')
mike_account = Account('74183', mike)

print(john_account.deposit(100))
print(john_account.deposit(150))

print('current balance',john_account.balance)

print(john_account.withdrawal(200))
print(john_account.withdrawal(200))
print('current balance',john_account.balance)

print('=========================================')
print(mike_account.deposit(1000))
print(mike_account.deposit(150))

print('current balance',mike_account.balance)

print(mike_account.withdrawal(200))
print(mike_account.withdrawal(200))
print('current balance',mike_account.balance)

print(mike_account.calc_interest())
print('current balance',mike_account.balance)