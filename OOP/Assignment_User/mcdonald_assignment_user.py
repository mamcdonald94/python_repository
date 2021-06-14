class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        self.account_balance += amount  # the specific user's account increases by the amount of the value received

    def make_withdrawal(self, amount):  # decreases balance by amount specified
        self.account_balance -= amount

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"New {other_user.name} balance: ${other_user.account_balance}")
        print(f"New {self.name} balance: ${self.account_balance}")

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")


mark = User("Mark", "fakemail@realmail.com")
rebekah = User("Rebekah", "realmail@fakemail.com")
lexi = User("Lexi", "mailfake@fakemail.com")


mark.make_deposit(500)
mark.make_deposit(500)
mark.make_deposit(500)
mark.make_withdrawal(850)
mark.display_user_balance()

rebekah.make_deposit(2000)
rebekah.make_deposit(1000)
rebekah.make_withdrawal(500)
rebekah.make_withdrawal(1100)
rebekah.display_user_balance()

lexi.make_deposit(5000)
lexi.make_withdrawal(750)
lexi.make_withdrawal(50)
lexi.make_withdrawal(800)
lexi.display_user_balance()

lexi.transfer_money(mark, 500)
