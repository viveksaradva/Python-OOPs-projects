import re
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number: str, owner: str  , balance: float=0.0):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance # Private attr for encapsulation

    @abstractmethod
    def calculate_interest(self):
        """
        Abstract method for interest calculation
        """
        return 0.0

    def deposit(self, amount):
        if re.match(amount, r"^\d+$"):
            self._balance += amount
            print(f"Deposited {amount} in the account {self.account_number} successfully.")
        else:
            print("Enter valid amount(e.g., 5000, 10000)")

    def withdraw(self, amount):
        if re.match(amount, r"^\d+$"):
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrawed {amount} from the account {self.account_number} successfully.")
            else:
                print("Insufficient balance!")
        else:
            print("Enter valid amount(e.g., 5000, 10000)")

    def get_balance(self):
        return self._balance
