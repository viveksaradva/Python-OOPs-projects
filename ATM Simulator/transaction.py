import datetime

class Transaction:
    def __init__(self, account_number, amount, transaction_type):
        self.account_number = account_number
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"{self.timestamp} - {self.transaction_type} of {self.amount} on Account {self.account_number}"
