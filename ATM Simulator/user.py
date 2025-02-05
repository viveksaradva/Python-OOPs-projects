class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self.name = name
        self.accounts = []

    def __str__(self):
        return f"{self.name}"

    def add_account(self, account):
        """
        Link an account to the user 
        """
        self.accounts.append(account)

    def get_accounts(self):
        """
        Displays all the accounts stored
        """
        return self.accounts
