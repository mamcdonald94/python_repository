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

account1 = BankAccount()
account2 = BankAccount()

account1.deposit(200).deposit(500).deposit(1000).withdraw(750).yield_interest().display_account_info()

account2.deposit(500).deposit(2000).withdraw(50).withdraw(800).withdraw(200).withdraw(350).yield_interest().display_account_info()
