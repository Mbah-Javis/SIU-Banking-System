import csv
db_name ='database.csv'
#read database csv file
def read_database():
    with open (db_name,'r') as file:
        reader=csv.reader(file)
        return list (reader)
    
#save items to csv database
def save_to_database(funds):
    with open(db_name,'w',newlines='') as file:
        writer=csv.writer(file)
        writer.writerows(funds)
        
#funds transfer
print("welcome to the funds transfer process...")

        

