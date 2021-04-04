# Tapabrata Dey #001521455

import load_truck as truck
import read_csv as csv
import calc_dist as dist
# import package_handler as pckg_hndl

def init_prog():
  csv.read_csv_file('csv/package_file.csv')
  dist.read_distance_data('csv/distance_table_data.csv', "data")
  dist.read_distance_data('csv/distance_table_data_name.csv', "name")
  # pckg_hndl.update_delivery_start_time()

def welcome_msg():
    print("\nWelcome to Parcel Delivery Service")
    print("----------------------------------\n")


def display_total_distance_traveled():
    print("Total mileage traveled by all trucks : [X] miles\n")


def testing():
    # for i in range(len(truck.first_delivery)):
    #   print(truck.first_delivery[i].start_time)

    # print(truck.first_delivery[1].address)
    print("first: ", len(truck.first_delivery))
    print("second: ", len(truck.second_delivery))
    print("third: ", len(truck.third_delivery))
    print("total: ", len(truck.first_delivery) + \
        len(truck.second_delivery) + len(truck.third_delivery))

def main():
    welcome_msg()
    init_prog()
    display_total_distance_traveled()
    testing()

if __name__ == "__main__":
    main()
