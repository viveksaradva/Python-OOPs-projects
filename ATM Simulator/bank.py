from utils import save_users, load_users, save_transactions, load_transactions
from account import SavingAccount, CurrentAccount
from transaction import Transaction
from datetime import datetime

class Bank:
    def __init__(self, name):
        self.name = name
        self.users = load_users()
        self.transactions = load_transactions()

    def add_user(self, user_id, name):
        """
        Add a user in JSON file
        """
        self.users[user_id] = {
            'name': name,
            'accounts': {}
        }
        save_users(self.users)

    def add_account(self, user_id, account):
        """
        Add an account in JSON file
        """
        if user_id in self.users:
            self.users[user_id]['accounts'][account.account_number] = {
                'balance': account._balance
            }
            
            # self.users[user_id]['balance'] = account._balance
            save_users(self.users)
        else:
            print("Customer not found")

    def get_user(self, user_id):
        """
        Fetching the user from the user JSON file
        """
        return self.users.get(user_id, None)

    def add_transaction(self, transaction):
        transaction_id = f"T{len(self.transactions) + 1}"
        self.transactions[transaction_id] = {
            "account_number": transaction.account_number,
            "amount": transaction.amount,
            "transaction_type": transaction.transaction_type,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_transactions(self.transactions)
