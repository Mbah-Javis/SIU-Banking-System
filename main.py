import csv

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

def show_balance():
    
    print(f"Your balance is ${balance:.2f}")

def deposit_funds():
    # 1. read database accounts
    # 2. take users account Id
    # 3. check if account exist. if account exist goto step 4
    # 4.1 enter amount to deposit
    # 4.2 add the amount to account balance
    # 4.3 save the account with the new balance
    # 5. Deposit completed
    #print("Create New Account")
    items=read_database()
    amount=(float(input("Ennter the amount to be deposited: ")))
    if amount<0:
        print("Please enter a valid amount")
        return 0
    else:
        
        print("Your transaction has beenn done successfully")
        return amount
balance=0
def get_choice(choice):
    if choice == 1:
        print("Create New Account")
    elif choice == 2:
        deposit_funds()
        print("Deposit Funds")
    elif choice == 3:
        print("Withdraw Funds")
    elif choice == 4:
        show_balance()
        print("Check Balance")
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
    print(f"|{'':<10}Menu{'':<10}|")
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
print(f"|{'':<5}WELCOME TO SIU BANKING SYSTEM {'':<5}|")
print("-" * 44)
while True:
    try:
        menu()
        choice = int(input("\nEnter your choice : "))
        get_choice(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
