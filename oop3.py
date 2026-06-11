

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self,amount):
        if amount <0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")

    def withdraw(self,amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        print(f'withdrew {amount}.Balance: {self._balance}')

    def get_balance(self):
        return self._balance

acc= BankAccount("Charan",10000)
acc.deposit(5000)
acc.withdraw(3000)
print('Final:',acc.get_balance())