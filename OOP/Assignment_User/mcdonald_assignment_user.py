class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        self.account_balance += amount  # the specific user's account increases by the amount of the value received
        return self

    def make_withdrawal(self, amount):  # decreases balance by amount specified
        self.account_balance -= amount
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"New {other_user.name} balance: ${other_user.account_balance}")
        print(f"New {self.name} balance: ${self.account_balance}")
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self


mark = User("Mark", "fakemail@realmail.com")
rebekah = User("Rebekah", "realmail@fakemail.com")
lexi = User("Lexi", "mailfake@fakemail.com")


mark.make_deposit(500).make_deposit(500).make_deposit(500).make_withdrawal(850).display_user_balance()

rebekah.make_deposit(2000).make_deposit(1000).make_withdrawal(500).make_withdrawal(1100).display_user_balance()

lexi.make_deposit(5000).make_withdrawal(750).make_withdrawal(50).make_withdrawal(800).display_user_balance().transfer_money(mark, 500)
