import csv
import load_truck as truck
import package_handler as pckg_hndl
import algo as algo

dist_data = []
dist_data_name = []

with open("csv/distance_table_data.csv") as dist_data_file:
  dist_data = list(csv.reader(dist_data_file, delimiter=','))

with open("csv/distance_table_data_name.csv") as dist_data_name_file:
  dist_data_name = list(csv.reader(dist_data_name_file, delimiter=','))

first_total_dist = 0
second_total_dist = 0
third_total_dist = 0

def updt_packages():
  pckg_hndl.updt_pkg_loc(truck.first_delivery, dist_data_name)
  pckg_hndl.updt_pkg_loc(truck.second_delivery, dist_data_name)
  pckg_hndl.updt_pkg_loc(truck.third_delivery, dist_data_name)

def find_fastest_route():
  algo.fastest_route(truck.first_delivery, "first", 0, dist_data)
  algo.fastest_route(truck.second_delivery, "second", 0, dist_data)
  algo.fastest_route(truck.third_delivery, "third", 0, dist_data)

def find_sum(row, col):
  global first_total_dist
  curr_dist = dist_data[row][col]
  if curr_dist == '':
    curr_dist = dist_data[col][row]
    first_total_dist += float(curr_dist)
    print(curr_dist, first_total_dist)
  return first_total_dist


def calc_delivery_dist():
  for i in range(len(algo.first_deliv_sorted_idx)):
    # print(algo.first_deliv_sorted_idx[i])
    try:
      first_deliv = algo.first_deliv_sorted_idx
      temp = find_sum(first_deliv[i], first_deliv[i + 1])
      # print(first_deliv[i], first_deliv[i + 1], print(temp))
    except IndexError:
      pass

def updt_pckg_algo_func():
  updt_packages()
  pckg_hndl.updt_starting_loc()
  find_fastest_route()
  calc_delivery_dist()
  # for i in range(len(algo.second_deliv_sorted_idx)):
  # 	print(algo.second_deliv_sorted_idx[i])

def total_dist():
  updt_pckg_algo_func()	
  return first_total_dist + second_total_dist + third_total_dist