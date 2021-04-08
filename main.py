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
    while True:
      usr_input = input("Please press 1, 2, or 3:\n\n"
                      "1. Search for a package\n"
                      "2. Delivery status at a particular time\n"
                      "3. Exit the program\n\n")
      try:
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

# def search_pckg():
#   return

# def pckg_status():
#     usr_time_input = input("\nTo view delivery status, please enter a time "
#                       "in HH:MM:SS format\n\n")
#     (h, m, s) = usr_time_input.split(':')
#     convert_uTime = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
#     for i in range(1, 41):
#       get_pckg_info(i, convert_uTime)

# def get_pckg_info(i, convert_uTime):
#     hash_search = get_hash.my_hash.search(i)
#     start_time = str(hash_search.start_time)
#     status_time = str(hash_search.status)
#     convert_times(start_time, status_time, hash_search, convert_uTime)



# def convert_times(start_time, status_time, hash_search, convert_uTime):
#     (h, m, s) = start_time.split(':')
#     convert_sTime = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
#     (h, m, s) = status_time.split(':')
#     convert_status_Time = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
#     display_time(start_time, status_time, convert_sTime, convert_status_Time,
#                 hash_search, convert_uTime)

# def display_time(start_time, status_time, convert_sTime, convert_status_Time,
#                 hash_search, convert_uTime):
#   if convert_sTime >= convert_uTime:
#     if_uTime_early(start_time, hash_search)
#   elif convert_sTime <= convert_uTime:
#     if convert_uTime < convert_status_Time:
#       if_uTime_bigger(start_time, hash_search)
#     else:
#       all_delivered(start_time, status_time, hash_search)

# def all_delivered(start_time, status_time, hash_search):
#   status = "Delivered at " + status_time
#   sTime = "Left hub at " + start_time
#   view_pckg_print_statements(hash_search, status, sTime)

# def if_uTime_bigger(start_time, hash_search):
#   status = "En Route"
#   sTime = "Left hub at " + start_time
#   view_pckg_print_statements(hash_search, status, sTime)

# def if_uTime_early(start_time, hash_search):
#   status = "At hub"
#   sTime = "Leaves hub at " + start_time
#   view_pckg_print_statements(hash_search, status, sTime)

# def view_pckg_print_statements(hash_search, status, sTime):
#   print("\nPackage Id: ", hash_search.id, "\n"
#           "Address: ", hash_search.address, "\n"
#           "City: ", hash_search.city, "\n"
#           "State: ", hash_search.state, "\n"
#           "Zip: ", hash_search.zip, "\n"
#           "Deadline: ", hash_search.deadline, "\n"
#           "Weight: ", hash_search.weight, "\n"
#           "Truck status: ", sTime, "\n"
#           "Status: ", status, "\n")
  

def main():
    welcome_msg()
    init_prog()
    display_total_distance_traveled()
    user_input()

if __name__ == "__main__":
    main()
