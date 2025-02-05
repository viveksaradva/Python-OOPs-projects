import re
from utils import save_users, load_users, save_transactions, load_transactions
from abc import ABC, abstractmethod
from transaction import Transaction

# Base Class
class Account(ABC):
    def __init__(self, account_number: str, owner: str  , balance: float=0.0):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance # Private attr for encapsulation
        self.transactions = load_transactions()
        self.user_accounts = load_users()

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
            self.add_transaction(Transaction(self.account_number, amount, "Deposit"))
            self.user_accounts[self.owner]['balance'] = self._balance
            save_users(self.bank.users)
            print(f"Deposited {amount} in the account {self.account_number} successfully.")
        else:
            print("Enter valid amount(e.g., 5000, 10000)")

    def withdraw(self, amount):
        if re.match(r"^\d+$", str(amount)):
            if amount <= self._balance:
                self._balance -= amount
                self.add_transaction(Transaction(self.account_number, amount, "Withdraw"))
                print(f"Withdrawed {amount} from the account {self.account_number} successfully.")
            else:
                print("Insufficient balance!")
        else:
            print("Enter valid amount(e.g., 5000, 10000)")

    def add_transaction(self, transaction):
        self.transactions = load_transactions()
        transaction_id = f"T{len(self.transactions) + 1}"
        self.transactions[transaction_id] = {
            "account_number": transaction.account_number,
            "amount": transaction.amount,
            "transaction_type": transaction.transaction_type,
            "timestamp": transaction.timestamp
        }
        save_transactions(self.transactions)
        print(f"Transaction saved: {self.transactions}")

    def get_balance(self):
        return self._balance
    
    def get_transaction_history(self):
        """
        Displaying the transaction history
        """
        for transaction_id, transaction_record in self.transactions.items():
            print(f"{transaction_record['timestamp']} - {transaction_record['transaction_id']}: {transaction_record['transaction_type']} of {transaction_record['amount']} on Account {transaction_record['account_number']}")

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
                super().withdraw(amount)
            else:
                print("Insufficient balance!")
        else:
            print("Enter valid amount(e.g., 5000, 10000)")
