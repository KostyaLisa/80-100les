class AccountBancaria:
    def __init__(self, nib, holder, balance=0.0, limit=0.0):
        # Private attributes
        self.__nib = nib
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    # Getter and Setter for NIB
    def get_nib(self):
        return self.__nib

    def set_nib(self, nib):
        self.__nib = nib

    # Getter and Setter for Holder
    def get_holder(self):
        return self.__holder

    def set_holder(self, holder):
        self.__holder = holder

    # Getter and Setter for Balance
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")

    # Getter and Setter for Limit
    def get_limit(self):
        return self.__limit

    def set_limit(self, limit):
        if limit >= 0:
            self.__limit = limit
        else:
            print("Limit cannot be negative.")


# Create an instance of AccountBancaria
account = AccountBancaria("123456789", "Alice", balance=1000.0, limit=500.0)

# Accessing attributes using getter methods
print(f"NIB: {account.get_nib()}")
print(f"Holder: {account.get_holder()}")
print(f"Balance: {account.get_balance()}")
print(f"Limit: {account.get_limit()}")

# Modifying attributes using setter methods
account.set_balance(1500.0)
account.set_limit(600.0)

# Accessing updated attributes
print("\nUpdated Information:")
print(f"Balance: {account.get_balance()}")
print(f"Limit: {account.get_limit()}")
