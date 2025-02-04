from bank import Bank
from customer import Customer
from account import SavingAccount, CurrentAccount

bank = Bank("HRS bank")

customer1 = Customer("C01", "Alice")

account1 =  CurrentAccount("A001", customer1, 200.0)

account1.deposit(500)  
account1.withdraw(300)  
account1.withdraw(2000)  # Should show "Insufficient balance!"

# Show transaction history
print("\nTransaction History:")
for transaction in account1.get_transaction_history():
    print(transaction)

# account1.deposit(500)
# account1.withdraw(20)
# print(account1.get_balance())
# account1.withdraw(800)
# print(account1.get_balance())

# print("-------------SavingAccount-------------------------")
# account2 = SavingAccount("A002", customer1, 5000)

# account2.withdraw(2000)
# print(account2.get_balance())
# print(f"The interest: {account2.calculate_interest()}")

