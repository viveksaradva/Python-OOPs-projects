## The overall project structure is:

```bash
banking_system/
│── main.py               # Entry point for the ATM Simulator
│── bank.py               # Contains the Bank class
│── account.py            # Defines the Account base class and subclasses
│── transaction.py        # Handles transaction details
│── customer.py           # Represents customer details
│── exception_handling.py # Custom exception classes
│── utils.py              # Helper functions (e.g., logging, data validation)
│── data/                 # Stores customer and transaction data (JSON/DB)
│   ├── customers.json
│   ├── transactions.json
```

> I will add the `data/` folder in the end, because I am still lacking behind in the concept of File handling.

## Making of `bank.py`
- It manages accounts and transactions.
- I have used the concept of Encapsulation in `balance` variable. I have written `_balance` made it a protected variable that can be used within the class and its subclasses.
- `self.accounts` is a `dict` that will store the account in key → value manner i.e., account_number → Account object
- It has two methods: i) `add_account(self, account)` and ii) `get_account(self, account_number)`
    - Here in `add_account(self, account)` the `account` parameter is an instance of the class `Account` from `account.py`
- `add_account()` will add the account in `self.accounts` while `get_account()` will retrieves the account from `self.accounts`.

## Making of `account.py`
- This file manages all the account related activities.
- Here the class `Account` is the base class and there are two subclasses: i) `SavingAccount` and ii) `CurrentAccount`.
- All three classes follows some small amount of OOPs concepts:
    1. `Account` (base class):
        - **Encapsulation** → Private balance attribute.
        - **Abstract Class** → Cannot be instantiated directly.
    
    2. `SavingAccount` (subclass):
        - **Inherits from** `Account`.
        - **Polymorphism** → Implements `calculate_interest()`.

    3. `CurrentAccount` (subclass):
        - Overrides `calculate_interest()` to have no interest.
        - Implements overdraft protection.
 
## Making of `customer.py`
- This file manages the customer details.
- It takes the fields `customer_id` and `name`.
- Now one customer can have one or many(more than one) relations to `account`; one customer may have more than one accounts. These accounts will be stored in `self.accounts` list.
- There are two methods that are used i) `add_account()` to add an account to a customer's account collection and ii) `get_accounts()` that will show the create accounts that the customer have. 

## Making of `transaction.py`
- This file provides a proper schema for transaction details.
- It has a `__str__()` dunder method that returns each transaction in a desired format.

## Making of `exception_handling.py`

## Making of `util.py`
- I have add four functions:
    1. `load_users()`: This function is used to load(read) the json file using the `json` module. Also contains `try except` block with checks for `JSONDecodeError`. It return a `dict` either filled or empty.
    2. `save_users()`: This function is used to save the newly added user in the `users.json`.
    3. `load_transactions()`: Similar functionality as `load_users()` but it loads or read transactions from the `transactions.json`.
    4. `save_transactions()`: Similar functionality as `save_users()` but it saves newly added transaction to the `transactions.json`.