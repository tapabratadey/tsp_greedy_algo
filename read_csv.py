#import statements
import csv
import hash_table as hash_table
import classes as Class
import load_truck as delivery

# Hash table instance
my_hash = hash_table.HashTable()

# reading csv file
def read_csv_file(filename):
    with open(filename) as package_file:
        package_data = csv.reader(package_file, delimiter=",")
        parse_data(package_data)

# parse_data and add to hash table
# O(n)
def parse_data(package_data):
    for package in package_data:
        package_id = int(package[0])
        package_address = package[1]
        package_city = package[2]
        package_state = package[3]
        package_zip = package[4]
        package_deadline = package[5]
        package_weight = package[6]
        package_notes = package[7]
        
        package = Class.Package(package_id,
                        package_address,
                        package_city,
                        package_state,
                        package_zip,
                        package_deadline,
                        package_weight,
                        package_notes)
        my_hash.add(package_id, package)
        delivery.load_trucks(package)

# search data from hash table
# for i in range(len(my_hash.table) + 1):
#     print(my_hash.search(i + 1))