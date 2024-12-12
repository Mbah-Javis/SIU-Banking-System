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
    account_system = read_database()
    acc =input("Enter your account ID")
 # search and display of Account
    for account in account_system:
         if account[0].isdigit==str(acc):
          print("\n Balance Sheet")
          print(f"Account ID : {account[0]}")
          print(f"Account Name: {account[1]}")
          print(f"Amount in Account : {account[2]}XAF")

         return

    print(f"The account '{acc}' is not found") 

def get_choice(choice):
    if choice == 1:
        create_new_account()
    elif choice == 2:
        print("Deposit Funds")
    elif choice == 3:
        print("Withdraw Funds")
    elif choice == 4:
        check_balance()
    elif choice == 5:
        print("Transfer Funds")
    elif choice == 6:
        print("Delete Account")
    elif choice == 7:
        print("List All Accounts")
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
