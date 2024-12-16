import csv
import random
from datetime import date

db_name = "SIU-Banking-System/database.csv"

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

def show_balance():
    accounts = read_database()
    #account_number = generate_account_number()
    check=(input("enter your account id: "))
    for i in accounts:
        if i[0]== check:
                    print(f"Your Current balance is {i[3]} XAF")
                    return
                   
    print("This account does not exist")
                    
tab = read_database()
# print("\n",tab)

    
    #print(f"Your balance is ${balance:.2f}")
#deposit func
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
    user_id=str(input("Enter the account ID: "))
    # while True: 
    #     try:
  
    for i in items:
                
                        
                        if i[0] == user_id:
                            
                            old_balance=float(i[3])
        
                        
                            while True:
                                try:
                                    amount= float(input("Enter the amount to be deposited: ")).strip()
                                    if(amount<0):
                                        print("The amount enterred can't be negative")

                                        continue
                                        
                                    i[3]=(old_balance+amount)
                                    save_to_database(items)
                                    print(f"the '{amount}'has been deposited successfully")
                                    return
                                    #     print(f"The transaction to {user_id} of {amount} XAF has been done successfully ")
                                    #     continue
                                    # break

                                    # while True:
                                    #     try:
                                    #         amount=(float(input("Enter the amount to be deposited: ")))
                                    #         if(amount<0):
                                    #             print("The amount enterred can't be negative")
                                    #             continue
                                #         break
                                except ValueError:
                                    print("Enter a valid amount")
        # except ValueError:
        #      print("Enter a valid  else create an account")


                

                        print(f"The Account {user_id} does not exist")
#display all Accounts 
def display_accounts():
     acct=read_database()
     if not  acct:
          print("Database is empty")
          return
     print("-"*62)
     for i in acct:
          print(f"{i[0]:<20} {i[1]:<15} {i[2]:<10} {i[3]} ")

                 
        
        
    
def get_choice(choice):
    if choice == 1:
        create_new_account()
    elif choice == 2:
        deposit_funds()
    elif choice == 3:
        print("Withdraw Funds")
    elif choice == 4:
        show_balance()
    elif choice == 5:
        print("Transfer Funds")
    elif choice == 6:
        print("Delete Account")
    elif choice == 7:
        #print("List All Accounts")
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

