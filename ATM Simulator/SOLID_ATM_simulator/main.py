import os
from storage import JsonStorageProvider
from logger import FileTransactionLogger
from bank import Bank, UserManager

def display_menu():
    print("\n=== Banking System ===")
    print("1. Create new user")
    print("2. Create new account")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Check balance")
    print("6. Exit")
    return input("Enter your choice (1-6): ")

def main():
    storage_provider = JsonStorageProvider("data")
    transaction_logger = FileTransactionLogger(storage_provider)
    user_manager = UserManager(storage_provider)
    bank = Bank("MyBank", user_manager, storage_provider, transaction_logger)

    session_user_id = None
    accounts = []

    while True:
        choice = display_menu()

        try:
            if choice == "1":
                if session_user_id:
                    print(f"\nAlready logged in as {session_user_id}")
                    continue
                user_id = input("Enter the user ID: ")
                name = input("Enter name: ")
                user_manager.add_user(user_id, name)
                session_user_id = user_id
                print(f"User {name} created successfully!")

            elif choice == '2':
                if not session_user_id:
                    print("Please create a user in option 1")
               
                else:
                    account_number = input("Enter account number: ")
                    initial_balance = float(input("Enter initial deposit amount: "))
                    account_type = input("Enter account type (savings/current): ").lower()

                    if account_type == "savings":
                        account = bank.create_savings_account(session_user_id, account_number, initial_balance)
                        accounts.append(account)
                    elif account_type == "current":
                        account = bank.create_current_account(session_user_id, account_number, initial_balance)
                        accounts.append(account)
                    else:
                        print("Invalid account type")
                        continue

            elif choice == '3':
                if not session_user_id:
                    print("Please create a user first")
                    continue
                if not accounts:
                    print("No accounts found")
                    continue

                print("\nAvailable accounts:")
                for i, account in enumerate(accounts):
                    print(f"{i+1}. Account {account.account_number}")
                        
                account_idx = int(input("Select account number: ")) - 1
                amount = float(input("Enter deposit amount: "))

                accounts[account_idx].deposite(amount)
                print(f"Successfully deposited {amount}")
                print(f"New balance: {accounts[account_idx].get_balance()}")

            elif choice == '4':
                if not session_user_id:
                    print("Please create a user first")
                    continue
                if not accounts:
                    print("No accounts found")
                    continue

                print("\nAvailable accounts:")
                for i, account in enumerate(accounts, 1):
                    print(f"{i}. Account {account.account_number}")
                        
                account_idx = int(input("Select account number: ")) - 1
                amount = float(input("Enter withdrawal amount: "))

                accounts[account_idx].withdraw(amount)
                print(f"Successfully withdrew {amount}")
                print(f"New balance: {accounts[account_idx].get_balance()}")

            elif choice == '5':
                if not session_user_id:
                    print("Please create a user first")
                    continue
                    
                if not accounts:
                    print("No accounts found")
                    continue
                    
                print("\nAvailable accounts:")
                for i, account in enumerate(accounts, 1):
                    print(f"{i}. Account {account.account_number}")
                    
                account_idx = int(input("Select account number: ")) - 1
                print(f"Current balance: {accounts[account_idx].get_balance()}")

            elif choice == "6":
                print("Thank you for using our banking system!")
                break
                
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError as e:
            print(f"Error: {str(e)}")
        except IndexError:
            print("Invalid account selection")
        except Exception as e:
            print(f"An error occured: {str(e)}")

if __name__ == "__main__":
        main()
