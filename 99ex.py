class AccountBancaria:
    def __init__(self, holder, balance=0.0, limit=0.0):
        self.__holder = holder
        self.__balance = max(0, balance)  # Ensure initial balance is not negative
        self.__limit = max(0, limit)  # Ensure initial limit is not negative

    # Property for holder
    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, name):
        self.__holder = name

    # Property for balance
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Error: Balance cannot be set to a negative value.")

    # Property for limit
    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, amount):
        if amount >= 0:
            self.__limit = amount
        else:
            print("Error: Limit cannot be set to a negative value.")

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance + self.__limit >= amount:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance: {self.__balance}")
            else:
                print("Withdrawal denied. Amount exceeds balance and limit.")
        else:
            print("Withdrawal amount must be positive.")


# Example usage
account = AccountBancaria("Alice", balance=1000.0, limit=500.0)

# Access and modify attributes using properties
print(f"Holder: {account.holder}")
print(f"Balance: {account.balance}")
print(f"Limit: {account.limit}")

# Deposit and withdraw operations
account.deposit(300)
account.withdraw(1200)
account.withdraw(700)  # This should be denied due to insufficient balance and limit
