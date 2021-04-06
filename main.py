# Tapabrata Dey #001521455

import load_truck as truck
import read_csv as csv
import calc_dist as dist
# import package_handler as pckg_hndl

def init_prog():
  csv.read_csv_file('csv/package_file.csv')

def welcome_msg():
    print("\nWelcome to Parcel Delivery Service")
    print("----------------------------------\n")


def display_total_distance_traveled():
    print("Total miles traveled : ", dist.total_dist(), " miles\n")

def main():
    welcome_msg()
    init_prog()
    display_total_distance_traveled()

if __name__ == "__main__":
    main()
