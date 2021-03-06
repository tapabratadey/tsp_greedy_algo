import datetime as dt
import read_csv as get_hash

# search pckg searches hash table with the id provided by the user
# it gets the start time and the status_time of the package
# asks the user to input a time to view the packages info
# calls display_time()
def search_pckg():
    usr_input_id = input("\nEnter Package id:\n")
    if (get_hash.my_hash.search(int(usr_input_id))):
      start_time = str(get_hash.my_hash.search(int(usr_input_id)).start_time)
      (h, m, s) = start_time.split(':')
      convert_sTime = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
      status_time = str(get_hash.my_hash.search(int(usr_input_id)).status)
      (h, m, s) = status_time.split(':')
      convert_status_Time = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
      usr_input_time = input("\n\nEnter a time in HH:MM:SS format: \n")
      (h, m, s) = usr_input_time.split(':')
      convert_uTime = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
      display_time(start_time, status_time, convert_sTime, convert_status_Time,
                  get_hash.my_hash.search(int(usr_input_id)), convert_uTime)
    else:
      print("Invalid Package Id")
      exit()

# pckg_status() asks user to view delivery status of all packages at a particular time
# it also loops through the all the packages and grabs information to display
def pckg_status():
    usr_time_input = input("\nTo view delivery status, please enter a time "
                      "in HH:MM:SS format\n\n")
    (h, m, s) = usr_time_input.split(':')
    convert_uTime = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    for i in range(1, 41):
      get_pckg_info(i, convert_uTime)

# gets called by pckg_status() to retreive a package's start_time and status
def get_pckg_info(i, convert_uTime):
    hash_search = get_hash.my_hash.search(i)
    start_time = str(hash_search.start_time)
    status_time = str(hash_search.status)
    convert_times(start_time, status_time, hash_search, convert_uTime)

# convert_times just converts time from string type to datetime type
def convert_times(start_time, status_time, hash_search, convert_uTime):
    (h, m, s) = start_time.split(':')
    convert_sTime = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    (h, m, s) = status_time.split(':')
    convert_status_Time = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    display_time(start_time, status_time, convert_sTime, convert_status_Time,
                hash_search, convert_uTime)

# display_time checks which checks for delivery windows based on the
# user input.
def display_time(start_time, status_time, convert_sTime, convert_status_Time,
                hash_search, convert_uTime):
  if convert_sTime >= convert_uTime:
    if_uTime_early(start_time, hash_search)
  elif convert_sTime <= convert_uTime:
    if convert_uTime < convert_status_Time:
      if_uTime_bigger(start_time, hash_search)
    else:
      all_delivered(start_time, status_time, hash_search)

# following functions displays information based on conditions from display_time()
def all_delivered(start_time, status_time, hash_search):
  status = "Delivered at " + status_time
  sTime = "Left hub at " + start_time
  view_pckg_print_statements(hash_search, status, sTime)

def if_uTime_bigger(start_time, hash_search):
  status = "En Route"
  sTime = "Left hub at " + start_time
  view_pckg_print_statements(hash_search, status, sTime)

def if_uTime_early(start_time, hash_search):
  status = "At hub"
  sTime = "Leaves hub at " + start_time
  view_pckg_print_statements(hash_search, status, sTime)

def view_pckg_print_statements(hash_search, status, sTime):
  print("\nPackage Id: ", hash_search.id, "\n"
          "Address: ", hash_search.address, "\n"
          "City: ", hash_search.city, "\n"
          "State: ", hash_search.state, "\n"
          "Zip: ", hash_search.zip, "\n"
          "Deadline: ", hash_search.deadline, "\n"
          "Weight: ", hash_search.weight, "\n"
          "Truck status: ", sTime, "\n"
          "Status: ", status, "\n")
  