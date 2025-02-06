from interfaces import IStorageProvider, ITransactionLogger
from account import BaseAccount, SavingsAccount, CurrentAccount

class UserManager:
    def __init__(self, storage_provider: IStorageProvider):
        self.storage_provider = storage_provider

    def add_user(self, user_id: str, name: str) -> None:
        users = self.storage_provider.load("users")
        users[user_id] = {
            "name": name,
            "accounts": {}
        }
        self.storage_provider.save(users, "users")

    def get_user(self, user_id: str) -> dict:
        users = self.storage_provider.load("users")
        return users.get(user_id)

class Bank:
    def __init__(self, name: str, user_manager: UserManager, storage_provider: IStorageProvider, transaction_logger: ITransactionLogger):
        self.name = name
        self.user_manager = user_manager
        self.storage_provide = storage_provider
        self.transaction_logger = transaction_logger

    def create_savings_account(self, user_id: str, account_number: str, initial_balance: float) -> SavingsAccount:
        account = SavingsAccount(account_number, user_id, initial_balance, self.transaction_logger, self.storage_provide)
        self._save_account(user_id, account)
        return account

    def create_current_account(self, user_id: str, account_number: str, initial_balance: float) -> CurrentAccount:
        account = CurrentAccount(account_number, user_id, initial_balance, self.transaction_logger, self.storage_provide)
        self._save_account(user_id, account)
        return account
    
    def _save_account(self, user_id: str, account: BaseAccount) -> None:
        users = self.storage_provide.load("users")
        if user_id not in users:
            raise ValueError("User not found")

        users[user_id]["accounts"][account.account_number] = {
            "balance": account.get_balance()
        }
        self.storage_provide.save(users, "users")
