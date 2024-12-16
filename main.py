import csv
import random
from datetime import date

db_name = 'database.csv'

# Read database csv file
def read_database():
    with open(db_name, 'r') as file:
            reader = csv.reader(file)
            return list(reader)

# Save items to the CSV database.
def save_to_database(items):
    with open(db_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(items)

def generate_account_number():
    return ''.join(random.choices('0123456789', k=12))

def get_date():
    return date.today()

# Create New Bank Account
def create_new_account():
    accounts = read_database()
    account_number = generate_account_number()
    full_name = input("Enter Your Full Name: ")
    while True:
        try:
            initial_deposit = float(input("Enter Initial Deposit Amount: "))
            if initial_deposit < 0:
                print("Amount cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a float or int")
    date_created = get_date()
    accounts.append([account_number, full_name, str(date_created), initial_deposit])
    save_to_database(accounts)
    print(f"Account created successfully\n")
    print("-"*60)
    print(f"{'Account ID':<15} {'Name':<15} {'Date Created':<15} Balance XAF")
    print("-"*60)
    print(f"{account_number:<15} {full_name:<15} {str(date_created):<15} {initial_deposit}")
    print("\n")


# Display the current balance
def check_balance():
    accounts = read_database()
    acc =input("Enter your account ID: ")
    # search and display of Account
    for account in accounts:
        if account[0] == acc :
            print("\n Balance Sheet")
            print(f"Account ID : {account[0]}")
            print(f"Account Name: {account[1]}")
            print(f"Date Created: {account[2]}")
            print(f"Amount: {account[3]}XAF")
            
            return
        
    print(f"The account '{acc}' is not found") 

def withdraw_funds():
    accounts = read_database()
    acc_id =input("Enter your account ID: ")
    for account in accounts:
        if account[0] == acc_id:
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Amount must be greater than zero. Please try again")
                    continue
                current_balance = float(account[3])
                if amount > current_balance:
                    print("Insufficient funds")
                    return
                else:
                    account[3] = str(current_balance - amount)
                    save_to_database(accounts)
                    print(f"Withdrawal of {amount} successful!")
                    return
            except ValueError:
                print("Invalid amount. Please try again\n")
                return
    else:
        print("Account not found\n")
        return

def transfer_funds():
    print("$ Welcome to the transfer funds process $")
    print("*" *42)
    accounts = read_database()
    sender_id =input("Enter your account Id: ").strip()
    for sender_account in accounts:
        if sender_account[0] == sender_id:
            sender_balance = float(sender_account[3])
            amount = float(input("\n Enter the amount you want to send: "))
            if amount > 0 and amount <= sender_balance:
                receiver_id =input("\n Enter your receiver's Id account: ").strip()
                for  receiver_account in accounts:
                    if receiver_account[0] == receiver_id:
                        receiver_balance = float(receiver_account[3]) 
                        sender_balance = sender_balance - amount
                        receiver_balance = receiver_balance + amount
                        sender_account[3] = str(sender_balance)
                        receiver_account[3] = str(receiver_balance)
                        save_to_database(accounts)
                        print(f"\n The transfer of {amount} FCFA to {receiver_account[1]} has been completed successfully!\n")
                        return
                else:
                    print("\n Your receiver does not have an account in SIU Banking system")
                    return
            else:
                print("\n Sorry! You do not have enough money for this transaction")  
                operation = input("\n If you want to retry type 0 ,else,press any key").strip()
                if operation == 0 :
                    transfer_funds()
                else:
                    return
    else:
        print("\nYou do not have an account in SIU Banking system")  
        answer = str(input("\n If you want to create an account type 1 ,else press any key")).strip()  
        if answer ==  1 :
            create_new_account()
        else:
            return

def delete_account():
    accounts = read_database()
    account = input("Enter Account ID: ").strip()
    
    # Find and remove account
    for i, item in enumerate(accounts):
        if item[0] == account:
            del accounts[i]
            save_to_database(accounts)
            print(f"Account '{account}' deleted successfully!\n")
            return
    
    print(f"Item '{account}' not found in the database.")

def display_accounts():
    acct=read_database()
    if not  acct:
        print("Database is empty")
        return
    print("-"*62)
    for i in acct:
        print(f"{i[0]:<20} {i[1]:<15} {i[2]:<15} {i[3]} ")
        print("-"*62)
    print("\n")

def get_choice(choice):
    if choice == 1:
        create_new_account()
    elif choice == 2:
        print("Deposit Funds")
    elif choice == 3:
        withdraw_funds()
    elif choice == 4:
        check_balance()
    elif choice == 5:
        transfer_funds()
    elif choice == 6:
        delete_account()
    elif choice == 7:
        display_accounts()
    elif choice == 0:
        print("Exiting SIU Bank System. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")

# Menu Display
def menu():
    print("-" * 26)
    print(f"{'':<10}Menu{'':<10}")
    print("-" * 26)
    print("1. Create New Account")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Check Balance")
    print("5. Transfer Funds")
    print("6. Delete Account")
    print("7. List All Accounts")
    print("0. Exit")
    print("-" * 26)

print("\n")
print("-" * 44)
print(f"{'':<5}WELCOME TO SIU BANKING SYSTEM {'':<5}")
print("-" * 44)
while True:
    try:
        menu()
        choice = int(input("\nEnter Your Choice : "))
        get_choice(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")