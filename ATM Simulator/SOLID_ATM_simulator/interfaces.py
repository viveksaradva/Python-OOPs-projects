from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol
from datetime import datetime

class IStorageProvider(Protocol):
    def save(self, data: dict, key: str) -> None:
        pass

    def load(self, key: str) -> dict:
        pass

class ITransactionLogger(Protocol):
    def log_transaction(self, transaction: 'Transaction') -> None:
        pass

@dataclass
class Transaction:
    account_number: str
    amount: float
    transaction_type: str
    timestamp: datetime = datetime.now()

class IAccount(ABC):
    @abstractmethod
    def deposite(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    @abstractmethod
    def get_balance(self) -> float:
        pass

