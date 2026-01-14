"""Encapsulation example using private attributes"""

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # protected

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance


# Practice (5):
# 1) Add `withdraw(amount)` with proper checks and error handling.
# 2) Demonstrate name mangling using `__secret` and how to access it (but discourage it).
# 3) Implement property `balance` with getter and no public setter.
# 4) Add transaction history logging inside the account.
# 5) Implement transfer between two accounts ensuring atomicity (simple simulation).
#
# Sample solutions (examples):
class SafeAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError('insufficient funds')
        self._balance -= amount

# property example
class PropertyAccount(BankAccount):
    @property
    def balance(self):
        return self._balance

if __name__ == "__main__":
    acc = SafeAccount(100)
    acc.deposit(50)
    try:
        acc.withdraw(200)
    except ValueError as e:
        print('withdraw failed:', e)
    print('balance:', acc.get_balance())
