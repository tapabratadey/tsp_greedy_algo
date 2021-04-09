import csv
import load_truck as truck
import package_handler as pckg_hndl
import algo as algo
import datetime as dt
import read_csv as get_hash

# vars
dist_data = []
dist_data_name = []
first_deliv_time = ['8:00:00']
second_deliv_time = ['9:05:00']
third_deliv_time = ['11:00:00']

# opens distance files to read in data and addresses
with open("csv/distance_table_data.csv") as dist_data_file:
  dist_data = list(csv.reader(dist_data_file, delimiter=','))

with open("csv/distance_table_data_name.csv") as dist_data_name_file:
  dist_data_name = list(csv.reader(dist_data_name_file, delimiter=','))

# calls updt_pkg_loc in package_handler module to update
# package locations
def updt_packages():
  pckg_hndl.updt_pkg_loc(truck.first_delivery, dist_data_name)
  pckg_hndl.updt_pkg_loc(truck.second_delivery, dist_data_name)
  pckg_hndl.updt_pkg_loc(truck.third_delivery, dist_data_name)

# calls fastest_route in algo module to calculate each delivery's
# delivery time
def find_fastest_route():
  algo.fastest_route(truck.first_delivery, "first", 0, dist_data)
  algo.fastest_route(truck.second_delivery, "second", 0, dist_data)
  algo.fastest_route(truck.third_delivery, "third", 0, dist_data)

# finds the sum between two addresses
def find_sum(row, col, dist_value):
  curr_dist = dist_data[row][col]
  if curr_dist == '':
    curr_dist = dist_data[col][row]
  dist_value += float(curr_dist)
  return dist_value

# calculates each delivery's time by callin find_sum
# pckg_hndl.calc_pckg_time calculates how long it take for a package
# to get delivered if the truck drives 18 miles per hour
# updates the delivery time and updaets the hash table
# in pckg_hndl.updt_del_time_n_hash()

# O(n^2) because of a 2nd loop inside calc_pkg_time
def calc_delivery_dist_sum(deliv_sorted_idx, dist_value, deliv_time_list, msg):
  for i in range(len(deliv_sorted_idx)):
    try:
      dist_value = find_sum(deliv_sorted_idx[i], deliv_sorted_idx[i + 1], dist_value)
      get_curr_dist = algo.find_current_dist_val(deliv_sorted_idx[i],
                                                deliv_sorted_idx[i + 1],
                                                dist_data)
      delivered_time = pckg_hndl.calc_pckg_time(get_curr_dist, deliv_time_list)
      if msg == "first":
        pckg_hndl.updt_del_time_n_hash(delivered_time, i, get_hash.my_hash, truck, msg)
      elif msg == "second":
        pckg_hndl.updt_del_time_n_hash(delivered_time, i, get_hash.my_hash, truck, msg)
      elif msg == "third":  
        pckg_hndl.updt_del_time_n_hash(delivered_time, i, get_hash.my_hash, truck, msg)
    except IndexError:
      pass
  return dist_value

# gets called by total_dist (refactored function)
def calc_delivery_dist():
  first_total_dist = 0
  second_total_dist = 0
  third_total_dist = 0
  first_total_dist = calc_delivery_dist_sum(algo.first_deliv_sorted_idx, 
                                            first_total_dist,
                                              first_deliv_time,
                                              "first")
  second_total_dist = calc_delivery_dist_sum(algo.second_deliv_sorted_idx, 
                                            second_total_dist,
                                            second_deliv_time,
                                            "second")
  third_total_dist = calc_delivery_dist_sum(algo.third_deliv_sorted_idx, 
                                            third_total_dist,
                                            third_deliv_time,
                                            "third")
  
  return first_total_dist + second_total_dist + third_total_dist

# updates package locations and add the starting location from the hub
# calls find_fastest route() to sort packages in each truck to find
# an optimized distance
def updt_pckg_algo_func():
  updt_packages()
  pckg_hndl.updt_starting_loc()
  find_fastest_route()

# gets called in main.py to find total delivery distance by the 3 trucks
# tota_dist() calls two funcs
def total_dist():
  updt_pckg_algo_func()
  total_dist = calc_delivery_dist()
  return total_dist
  