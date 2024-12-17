class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner            # Public attribute
        self.__balance = balance       # Private attribute, with name-mangling

    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Setter method for balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Method for withdrawal with validation
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Withdrawal amount must be positive.")

# Creating an account
account = BankAccount("Alice", 100)

# Accessing public attribute
print(account.owner)  # Output: Alice

# Using methods to interact with private balance
print(account.get_balance())  # Output: 100
account.deposit(50)           # Output: Deposited 50. New balance: 150
account.withdraw(30)          # Output: Withdrew 30. New balance: 120

