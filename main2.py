def transfer_funds():
    print("$ Welcome to the transfer funds process $")
    print("*" *42)
    accounts = read_database()
    sender_id =input("enter your account Id: ").strip()
    for sender_account in accounts:
            if sender_account[0] == sender_id and len(sender_account) > 0:
                 sender_balance = float(sender_account[3])
                 amount = float(input("\n enter the amount you want to send"))
                 if amount > 0 and amount <= sender_balance:
                    receiver_id =str(input("\n enter your receiver's Id account")).strip()
                    receiver_id = read_database()
                    for  receiver_account in accounts:
                         if receiver_account[0] == receiver_id and len(receiver_account) > 0:
                            receiver_balance = float(receiver_account[3]) 
                            sender_balance = sender_balance - amount
                            receiver_balance = receiver_balance + amount
                            sender = [sender_account[0], sender_account[1], sender_account[2], str(sender_balance)]
                            receiver = [receiver_account[0], receiver_account[1], receiver_account[2], str(receiver_balance)]
                            save_to_database(sender)
                            save_to_database(receiver)
                            print("\n The transfer completed successfully")   
                    else:
                        print("\n Your receiver does not have an account in SIU Banking system") 
                 else:
                     print("\n Sorry! You do not have enough money for this transaction")  
                     operation =str(input("\n If you want to retry type 0 ,else,press any key")).strip()
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
