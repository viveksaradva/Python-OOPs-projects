from bank import Bank
from account import SavingAccount, CurrentAccount
from utils import load_users

def display_menu():
    print("\n1. Create a new user")
    print("2. Create a new account")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Check balance")
    print("6. Exit")

if __name__ == "__main__":

    bank = Bank("MyBank")
    session_user_id = None # For user logging
    accounts = []

    while True:
        print("\nWelcome to ATM Simulator")
        display_menu()
        choice = input("Enter the choice: ")

        if choice == '1':
            if session_user_id:
                print(f"\nAlready logged in as {session_user_id}")
            else:
                session_user_id= input("Enter user_id: ")
                user_name = input("Enter user_name: ")
                bank.add_user(session_user_id, user_name)
                print(f"User {user_name} is created successfully!")

        elif choice == '2':
            if not session_user_id:
                print("Please create a user in option 1")
            else:
                account_num = input("Enter the account number: ")
                initial_balance = float(input("Enter initial deposit amount: "))
                account_type = input("Enter the account type(savings or current): ")
                if account_type.lower() == "savings":
                    account = SavingAccount(account_num, session_user_id, initial_balance)
                elif account_type.lower() == "current":
                    account = CurrentAccount(account_num, session_user_id, initial_balance)
                else: 
                    print("Invalid account type.")
                    continue

                bank.add_account(session_user_id, account)
                accounts.append(account)
                print(f"{account_type.capitalize()} account {account_num} created successfully.")

        elif choice == '3':
            if not session_user_id:
                print("Please create a user in option 1")
            else:
                amount = int(input("Enter deposit amount: "))

                print("Choose the account: ", end='\n')
                for i, account in enumerate(accounts):
                    print(f"{i+1}. {account.account_number}")

                account_sr_num = int(input("Enter the account sr number: "))
                
                account = accounts[account_sr_num - 1]
                account.deposit(amount)

                print(f"Deposited {amount} to account {account.account_number}.")
                print(f"Balance: {account.get_balance()}")

        elif choice == '4':
            if not session_user_id:
                print("Please create a user in option 1")
            else:
                amount = int(input("Enter withdraw amount: "))

                print("Choose the account: ", end='\n')
                for i, account in enumerate(accounts):
                    print(f"{i+1}. {account.account_number}")

                account_sr_num = int(input("Enter the account sr number: "))
                
                account = accounts[account_sr_num - 1]
                account.withdraw(amount)

                print(f"Withdraw {amount} from account {account.account_number}.")

        elif choice == '5':
            if not session_user_id:
                print("Please create a user in option 1")
            else:
                print("Choose the account: ", end='\n')
                for i, account in enumerate(accounts):
                    print(f"{i+1}. {account.account_number}")

                account_sr_num = int(input("Enter the account sr number: "))
                
                account = accounts[account_sr_num - 1]
                print(f"Balance: {account.get_balance()}")

        elif choice == '6':
            print(f"Logging out user {session_user_id}. Goodbye!")
            session_user_id = None  # Reset session
            break                                