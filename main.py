# Tapabrata Dey #001521455

import load_truck as truck
import read_csv as csv

csv.read_csv_file('csv/package_file.csv')

def welcome_msg():
    print("\nWelcome to Parcel Delivery Service")
    print("----------------------------------\n")


def display_total_distance_traveled():
    print("Total mileage traveled by all trucks : [X] miles\n")


def testing():
    # print(truck.first_delivery[1].address[0])
    print("first: ", len(truck.first_delivery))
    print("second: ", len(truck.second_delivery))
    print("third: ", len(truck.third_delivery))
    print("total: ", len(truck.first_delivery) + \
        len(truck.second_delivery) + len(truck.third_delivery))

def main():
    welcome_msg()
    display_total_distance_traveled()
    testing()

if __name__ == "__main__":
    main()
