class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance >= 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print("Error: negative balance detected")
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account += amount
        return self

    def make_withdrawal(self, amount):
        self.account -= amount
        return self

    def transfer_money(self, other_user, amount):
        self.account -= amount
        other_user.account += amount
        print(f"New {other_user.name} balance: ${other_user.account}")
        print(f"New {self.name} balance: ${self.account}")
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account}")
        return self



mamcdonald94 = User("Mark", "fakemail@email.org")


mamcdonald94.account.deposit(1000).display_account_info().yield_interest().display_account_info()