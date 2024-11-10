class AccountBancaria:
    def __init__(self, holder, balance=0.0, limit=0.0):
        self.holder = holder
        self.balance = balance
        self.limit = limit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Please enter a positive amount to deposit.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance + self.limit:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds. Withdrawal amount exceeds balance and limit.")
        else:
            print("Please enter a positive amount to withdraw.")

# Create an instance of the AccountBancaria class
account = AccountBancaria("Alice", balance=1000.0, limit=500.0)

# Perform deposit and withdrawal operations
account.deposit(200)
account.withdraw(300)
account.withdraw(1500)  # This will exceed balance + limit and show an error
