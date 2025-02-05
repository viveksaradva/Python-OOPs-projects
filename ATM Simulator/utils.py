import json
import os

USERS_FILE = 'data/users.json'
TRANSACTION_FILE = 'data/transactions.json'

def load_users():
    """
    Load users from the JSON file
    """
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            try: 
                return json.load(f)
            except json.JSONDecodeError:
                print("Users file is empty or corrupted. Initializing with an empty dictionary.")
                return {}
    return {}

def save_users(users):
    """
    Save users to the JSON file atomically
    """
    temp_file = USERS_FILE + ".tmp"
    with open(temp_file, 'w') as f:
        json.dump(users, f, indent=4)
    os.replace(temp_file, USERS_FILE)  # Ensure data is fully written before replacing old file

def load_transactions():
    """
    Load transactions from the JSON file
    """
    if os.path.exists(TRANSACTION_FILE):
        with open(TRANSACTION_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("ransactions file is empty or corrupted. Initializing with an empty dictionary.")
                return {}
    return {}

def save_transactions(transactions):
    """
    Saves transactions to the JSON file
    """
    with open(TRANSACTION_FILE, 'w') as f:
        json.dump(transactions, f, indent=4)
