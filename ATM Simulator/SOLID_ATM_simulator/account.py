from interfaces import IAccount, IStorageProvider, ITransactionLogger, Transaction 

class BaseAccount(IAccount):
    def __init__(self, account_number: str, owner: str, balance: float, transaction_logger: ITransactionLogger, storage_provider: IStorageProvider):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance
        self._transaction_logger = transaction_logger
        self.storage_provider = storage_provider

    def deposite(self, amount: float) -> None:
        users = self.storage_provider.load("users")

        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount
        self._transaction_logger.log_transaction(
            Transaction(self.account_number, amount, "Deposite")
        )
        users[self.owner]['accounts'][self.account_number]['balance'] = self._balance
        self.storage_provider.save(users, "users")

    def withdraw(self, amount: float) -> None:
        users = self.storage_provider.load("users")
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount
        self._transaction_logger.log_transaction(
            Transaction(self.account_number, amount, "Withdraw")
        )
        users[self.owner]['accounts'][self.account_number]['balance'] = self._balance
        self.storage_provider.save(users, "users")

    def get_balance(self) -> float:
        return self._balance

class SavingsAccount(BaseAccount):
    def __init__(self, account_number: str, owner: str, balance: float, transaction_logger: ITransactionLogger, storage_provider: IStorageProvider, interest_rate: float = 0.03):
        super().__init__(account_number, owner, balance, transaction_logger, storage_provider)
        self.interest_rate = interest_rate

    def calculate_interest(self) -> float:
        return self._balance * self.interest_rate

class CurrentAccount(BaseAccount):
    def __init__(self, account_number: str, owner: str, balance: float, transaction_logger: ITransactionLogger, storage_provider: IStorageProvider, overdraft_limit: float = 500):
        super().__init__(account_number, owner, balance, transaction_logger, storage_provider)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        users = self.storage_provider.load("users") 
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > (self._balance + self.overdraft_limit):
            raise ValueError("Amount exceeds overdraft limit")

        self._balance -= amount
        self._transaction_logger.log_transaction(
            Transaction(self.account_number, amount, "Withdraw")
        )
        users[self.owner]['accounts'][self.account_number]['balance'] = self._balance
        self.storage_provider.save(users, "users")