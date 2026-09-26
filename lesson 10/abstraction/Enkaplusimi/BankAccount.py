class BankAccount:

    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance = amount

    def get_balance(self):
        return self.__balance


account = BankAccount("donjeta",100)
:
print(account.get_balance())
account.deposit(50)

print(account.get_balance())