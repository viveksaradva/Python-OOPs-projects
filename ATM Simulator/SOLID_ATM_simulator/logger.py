from interfaces import IStorageProvider, Transaction, ITransactionLogger

class FileTransactionLogger(ITransactionLogger):
    def __init__(self, storage_provider: IStorageProvider):
        self.storage_provider = storage_provider

    def log_transaction(self, transaction: Transaction) -> None:
        transactions = self.storage_provider.load("transactions")
        transaction_id = f"{len(transactions) + 1}"

        transactions[transaction_id] = {
            "account_number": transaction.account_number,
            "amount": transaction.amount,
            "transaction_type": transaction.transaction_type,
            "timestamp": transaction.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }

        self.storage_provider.save(transactions, "transactions")
