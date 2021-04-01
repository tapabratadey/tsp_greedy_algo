import csv

with open('csv/package_file.csv') as package_file:
    read_file = csv.reader(package_file, delimiter=",")
    for row in read_file:
        print(row)
