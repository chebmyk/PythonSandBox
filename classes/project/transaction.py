from  datetime import datetime, timezone, timedelta
from enum import Enum

from classes.project.account import Account


class TransactionType(Enum):
    Deposit ='D'
    Withdrawal = 'W'
    Interest = 'I'
    Declined = 'X'


class Trx:
    i = 0
    @classmethod
    def nextid(cls):
        while True:
            cls.i += 1
            yield cls.i

    @classmethod
    def current_time(cls):
        return datetime.now(timezone.utc)

    @classmethod
    def transaction_code(self, transactionType,  account_number):
        return f"{transactionType.value}-{account_number}-{self.current_time().strftime('%Y%m%d%H%M%S')}-{next(Trx.nextid())}"


def transaction(fn):
    def id(*args, **kwargs):
        account = args[0]
        if isinstance(account, Account):
            account_number = account.number
            transactionType = fn(*args, **kwargs)
            return Trx.transaction_code(transactionType, account_number)
        else:
            raise Exception("Unsupported trx")
    return id