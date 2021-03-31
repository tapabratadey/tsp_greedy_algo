import csv

with open('csv/package_file.csv') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=",")
    for row in read_csv:
        print(row)
