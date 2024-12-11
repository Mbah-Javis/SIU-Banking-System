def withdraw_funds():
    accounts = read_database()  
    account_id = input("Enter your Account ID: ")

    for account in accounts:
        if account[0] == account_id:
            amount = float(input("Input amount to withdraw: "))
            
    print("Account not found")
    amount=float(input("enter amount to withdraw:"))
    if amount> accounts[1]:
        print("amount is greater than account,please enter a different account.")
    elif amount <= accounts[1]:
        accounts[1]-=amount
        save_account_details=(account_id,account[1])
        print("Succesful withdrawal")

    else:
                print("an error occured,please try again.")