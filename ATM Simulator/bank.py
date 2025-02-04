class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_account(self, account):
        """
        Add a new bank account in accounts dict
        """
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        """
        Fetching the account details from account dict using account_number
        """
        return self.accounts.get(account_number, None)
