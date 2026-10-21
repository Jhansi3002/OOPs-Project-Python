
class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0

    def check_balance(self):
        print(f"Balance: {self._balance}")

    def deposit(self, amount):
        self._balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print("Withdrawal successful")
        else:
            print("Not enough balance")


# Define this OUTSIDE the Account class
class SavingsAccount(Account):
    def calculate_interest(self):
        interest = self._balance * 0.04
        print(f"Interest: {interest}")


# Define this OUTSIDE the Account class
class CurrentAccount(Account):
    def withdraw(self, amount):
        overdraft_limit = 1000

        if self._balance + overdraft_limit >= amount:
            self._balance -= amount
            print(f"Withdrawal successful. Balance: {self._balance}")
        else:
            print("Not enough balance")


class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__account = {}

    def create_account(self, id, holder_name, account_type):
        if account_type == "savings":
            new_account = SavingsAccount(id, holder_name)
        elif account_type == "current":
            new_account = CurrentAccount(id, holder_name)
        else:
            print("Invalid account type")
            return None

        self.__account[id] = new_account
        print("Account creation successful")
        return new_account


cbk = Bank("SBI", "Tumkur")

s1 = cbk.create_account("1", "Raksha", "savings")
c1 = cbk.create_account("2", "Jhansi", "current")

s1.deposit(1000)
c1.deposit(10)
s1.withdraw(500)
s1.check_balance()
c1.withdraw(20)
s1.calculate_interest()

