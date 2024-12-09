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

def create_new_account():
    print("Create New Account")

def get_choice(choice):
    if choice == 1:
        print("Create New Account")
    elif choice == 2:
        print("Deposit Funds")
    elif choice == 3:
        print("Withdraw Funds")
    elif choice == 4:
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
