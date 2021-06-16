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
        self.account = BankAccount(0.02)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self


mark = User("Mark", "fakemail@email.org")
rebekah = User("Bekah", "fakemail@realmail.org")

mark.make_deposit(100).make_withdrawal(50).display_user_balance()
rebekah.make_deposit(600).transfer_money(mark, 500).display_user_balance()
mark.display_user_balance()
