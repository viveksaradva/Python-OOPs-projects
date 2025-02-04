import re
from abc import ABC, abstractmethod
from transaction import Transaction

# Base Class
class Account(ABC):
    def __init__(self, account_number: str, owner: str  , balance: float=0.0):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance # Private attr for encapsulation
        self.transactions = []

    def __str__(self):
        return f"Account number: {self.account_number} | Owner: {self.owner}"

    @abstractmethod
    def calculate_interest(self):
        """
        Abstract method for interest calculation
        """
        return 0.0

    def deposit(self, amount):
        if re.match(r"^\d+$", str(amount)):
            self._balance += amount
            self.transactions.append(Transaction(self.account_number, amount, "Deposit"))
            print(f"Deposited {amount} in the account {self.account_number} successfully.")
        else:
            print("Enter valid amount(e.g., 5000, 10000)")

    def withdraw(self, amount):
        if re.match(r"^\d+$", str(amount)):
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrawed {amount} from the account {self.account_number} successfully.")
            else:
                print("Insufficient balance!")
        else:
            print("Enter valid amount(e.g., 5000, 10000)")

    def get_balance(self):
        return self._balance
    
    def get_transaction_history(self):
        """
        Displaying the transaction history
        """
        return [str(t) for t in self.transactions]

# Subclass1
class SavingAccount(Account):
    INTEREST_RATE = 0.03 # 3% interest

    def calculate_interest(self):
        """
        Calculates interest for saving account
        """
        return self._balance * self.INTEREST_RATE

# Subclass2
class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 500

    def calculate_interest(self):
        """
        Current accounts do not have interest
        """
        return 0

    def withdraw(self, amount):
        """
        Allow overdraft up to a limit of 500
        """
        if re.match(r"^\d+$", str(amount)):
            if  amount <= (self._balance + self.OVERDRAFT_LIMIT):
                self._balance -= amount
                self.transactions.append(Transaction(self.account_number, amount, "Withdraw"))
                print(f"Withdrawed {amount} from the account {self.account_number} successfully.")
            else:
                print("Insufficient balance!")
        else:
            print("Enter valid amount(e.g., 5000, 10000)")
