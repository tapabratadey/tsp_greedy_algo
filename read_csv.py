#import statements
import csv
import hash_table as hash_table

# Hash table instance
my_hash = hash_table.HashTable()

# Package class that holds a package's data
class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes):
        self.id = id,
        self.address = address,
        self.city = city,
        self.state = state,
        self.zip = zip,
        self.deadline = deadline,
        self.weight = weight,
        self.notes = notes

    # __str__ func to convert data obj to string
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id,
            self.address,
            self.city,
            self.state,
            self.zip,
            self.deadline,
            self.weight,
            self.notes)

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
        
        package = Package(package_id,
                        package_address,
                        package_city,
                        package_state,
                        package_zip,
                        package_deadline,
                        package_weight,
                        package_notes)
        my_hash.add(package_id, package)

read_csv_file('csv/package_file.csv')

# get data from hash table
for i in range(len(my_hash.table) + 1):
    print("Key: {} and Movie: {}".format(i + 1, my_hash.search(i + 1)))