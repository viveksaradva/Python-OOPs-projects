class Customer:
    def __init__(self, customer_id, name):
        self._customer_id = customer_id
        self.name = name
        self.accounts = []

    def __str__(self):
        return f"{self.name}"

    def add_account(self, account):
        """
        Link an account to the customer
        """
        self.accounts.append(account)

    def get_accounts(self):
        """
        Displays all the accounts stored
        """
        return self.accounts
