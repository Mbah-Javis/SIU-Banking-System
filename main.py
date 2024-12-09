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

