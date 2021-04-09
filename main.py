# Tapabrata Dey #001521455

import load_truck as truck
import read_csv as csv
import calc_dist as dist
import user_input as user

def init_prog():
  csv.read_csv_file('csv/package_file.csv')

def welcome_msg():
    print("\nWelcome to Parcel Delivery Service")
    print("----------------------------------\n")

def display_total_distance_traveled():
    print("Total miles traveled : ", dist.total_dist(), " miles\n")

def user_input():
  try:
    usr_input = input("Please press 1, 2, or 3:\n\n"
                    "1. Search for a package\n"
                    "2. Delivery status at a particular time\n"
                    "3. Exit the program\n\n")
    try:
      while usr_input != 3:
        if usr_input == '3':
          print('Bye!')
          exit()
        if usr_input == "1":
          user.search_pckg()
        elif usr_input == "2":
          user.pckg_status()
        else:
          print('Invalid input')
          exit()
    except ValueError as e:
      print('Invalid input')
      exit()
  except KeyboardInterrupt:
      print('\nBye!')
      pass

def main():
    welcome_msg()
    init_prog()
    display_total_distance_traveled()
    user_input()

if __name__ == "__main__":
    main()
