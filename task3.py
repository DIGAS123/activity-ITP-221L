class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account balance: {self.balance}")

account = BankAccount("1234567890", "Jeffrey digas", 100000)

account.display_balance()
account.deposit(5000)
account.withdraw(4000)
account.withdraw(10000)  
account.display_balance()
