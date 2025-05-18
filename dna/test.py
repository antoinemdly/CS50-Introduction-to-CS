import csv
import sys

# TODO: Check for command-line usage
if len(sys.argv) != 2:
    sys.exit("Usage: python program.py DATABASE_FILE")

# TODO: Read database file into a variable
database = {}
STR = []

with open(sys.argv[1], 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        name = row['name']
        database[name] = []

        for column in row:
            if column != 'name':
                if column not in STR:
                    STR.append(column)
                database[name].append(row[column])
# Print the database
for person, details in database.items():  # Use items() to iterate over dictionary items
    print(f"{person}: {details}")
